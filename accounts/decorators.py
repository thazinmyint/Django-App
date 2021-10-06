from django.shortcuts import redirect


def authenicated_user(view_fun):
    def wrapper(request):
        if not request.user.is_authenticated:
          return  view_fun(request)
        else:
          return  redirect('/')
    return wrapper;

