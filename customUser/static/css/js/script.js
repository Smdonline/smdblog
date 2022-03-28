/**
 * Created by Daniel on 11/5/2021.
 */
$(document).ready(function(){

    $('#lang-link').click(function () {
        var  sir=window.location.href.split('/');p
        var final=sir[sir.length-2];
        if(final==="contact"){
            $(this).attr('href',$(this).attr('href')+''+final);
        }

    });


});