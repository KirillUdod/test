from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.core.context_processors import csrf
from loginsys.forms import MyRegistrationForm
# Create your views here.

def login(request):
    
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            if 'last_article' in request.COOKIES:
                back_url = request.COOKIES.get('last_article')
                response = redirect(back_url)
                response.delete_cookie('last_article')
                return response
            else:
                return redirect('/')
        else:
            args['login_error'] = "User is not found"
            return render_to_response('login.html', args)
    else:
        return render_to_response('login.html', args)
        
        
def logout(request):
    back_url = request.META['HTTP_REFERER']
    auth.logout(request)
    return redirect(back_url)
    
def register(request):
    args = {}
    args.update(csrf(request))
    args['form'] = MyRegistrationForm()
    if request.POST:
        newuser_form = MyRegistrationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username=newuser_form.cleaned_data['username'], password=newuser_form.cleaned_data['password2'])
            auth.login(request, newuser)
            return redirect('/')
        else:
            args['form'] = newuser_form
    return render_to_response('register.html', args)
