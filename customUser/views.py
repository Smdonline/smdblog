from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib.auth.views import (
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    LoginView
)

from .models import Profil
from .forms import (
    UserCreationForm,
    BootsrapFormMixin,
    MyLoginForm,
    MyPasswordResetForm,
    SetPasswordForm,
    MyPasswordChangeForm,
    ChangeUserProfile
)
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes,force_text
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.
def signup(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = "A activate your account"
            message = render_to_string('registration/acc_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })

            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
                    )
            email.send()
            return redirect('regToConfirm')



    else:
        form = UserCreationForm()
    return render(request,'registration/create.html',{'form':form})


def activate(request, uidb64, token):
    if request.user.is_authenticated:
        logout(request)
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = get_user_model().objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token) and not user.is_active:
        user.is_active = True
        user.save()
        return redirect('regConfirmed')
    else:
        return HttpResponse('Activation link is invalid!')


class UserChangePassword(PasswordChangeView):
    template_name = 'registration/password_change.html'
    form_class = MyPasswordChangeForm
    success_url = reverse_lazy('password_change_done')


class UserChangePasswordDone(PasswordChangeDoneView,BootsrapFormMixin):
    template_name = 'registration/password_change_done.html'
    extra_context = {'error':'password changed'}


class UserPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset.html'
    form_class = MyPasswordResetForm
    success_url = reverse_lazy('password_reset_done_view')


class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = "registration/password_reset_done_view.html"


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm_view.html'
    form_class = SetPasswordForm


class UserPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'registration/password_reset_complete_view.html'
class UserLoginView(LoginView):
    template_name = 'registration/login.html'
    form_class = MyLoginForm

@login_required
def user_profile(request):
    profil = request.user.get_user_profile()

    return render(request,'registration/profil.html',{'profil':profil})
@login_required
def user_profile_edit(request):
    instance=None
    try:
        instance=Profil.objects.get(user=request.user)
    except Profil.DoesNotExist:
        pass
    if request.method == 'POST':
        form=ChangeUserProfile(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            profil = form.save(commit=False)
            profil.user = request.user
            profil.save()
            return redirect('profil')
    else:
        form=ChangeUserProfile(instance=instance)
    return render(request,"registration/profile_edit.html",{'form':form})



