from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticatedUser(view_func):
    def wrapper_func(request,*args, **kwargs):
        if request.user.is_authenticated:
            return redirect('store')
        else:
            return view_func(request,*args,**kwargs)
    return wrapper_func

def allowed_users(view_func):
    def wrapper_func(request,*args, **kwargs):
        if request.user.is_nursery_manager:
            return view_func(request,*args,**kwargs)
        else:
            return redirect('store')    
    return wrapper_func
