from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from models import LoginForm

def login(request):

    # Make sure 'Matt' username exists
    u = User.objects.get(username__exact='matt')
    if u is None:
        u = User.objects.create_user('matt', 'mmeisinger@gmail.com', 'test')


    if request.method == 'POST': # If the form has been submitted...
        form = LoginForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None and user.is_active:
                login(request)
                return HttpResponse("Successfully logged in")
            else:
                return HttpResponseRedirect('/') # Redirect after POST
    else:
        form = LoginForm() # An unbound form

    return render(request, 'account/login.html', {
        'form': form,
    })


@login_required(login_url='/account/login/')
def logout(request):
    return render(request, 'account/logout.html');
