from django.http import HttpResponseForbidden
from django.contrib.auth.models import Group
from functools import wraps
from django.shortcuts import render, redirect
from django.contrib import messages

def check_group_permission(groups_name):

    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            has_access = False

            for group in groups_name:
                if request.user.groups.filter(name=group).exists():
                    has_access = True
                    break   

            if not has_access:
                messages.error(request,"Você não tem permissão para acessar este recurso.")
                return redirect("home")
            
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator



def login_required_custom(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/login/') 
        return view_func(request, *args, **kwargs)
    return _wrapped_view