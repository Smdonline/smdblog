from django.urls import path,include,reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.views import (PasswordChangeDoneView,LogoutView)
from . import views
urlpatterns = [
    path('regToConfirm',TemplateView.as_view(template_name='registration/reg_to_confirm.html'),name='regToConfirm'),
    path('regConfirmed',TemplateView.as_view(template_name='registration/reg_confirmed.html'),name='regConfirmed'),
    #path('profile/',TemplateView.as_view(template_name='registration/profil.html'),name='profil'),
    path('login/',views.UserLoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page=reverse_lazy('profil')),name='logout'),
    path('changePass/',views.UserChangePassword.as_view(),name='change_password'),
    path('passwordChangeDone/',views.UserChangePasswordDone.as_view(),name='password_change_done'),
    path('passwordReset/',views.UserPasswordResetView.as_view(),name='password_reset'),
    path('passwordResetDone/',views.UserPasswordResetDoneView.as_view(),name='password_reset_done_view'),
    path('passwordResetConfirm/<uidb64>/<token>/',views.UserPasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('passwordResetComplete/',views.UserPasswordResetCompleteView.as_view(),name='password_reset_complete_view'),
    path('create/',views.signup,name='registration'),
    path('activate/<str:uidb64>/<str:token>', views.activate, name='activate'),
    path('profile/',views.user_profile,name='profil'),
    path('profile/Edit',views.user_profile_edit,name='profile_edit'),
]