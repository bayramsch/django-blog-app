from django.shortcuts import redirect, render
from users.forms import UserForm, UserProfileForm, UserUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import  login, logout



def register(request):
    form = UserForm(request.POST or None)
    if request.user.is_authenticated:
        messages.warning(request, "You already have an account!")
        return redirect("blog:postlist")
    if form.is_valid():
        form.save()
        name = form.cleaned_data["username"]
        messages.success(request, f"Account created for {name}")
        return redirect("users:login")

    context = {
        'form':form
    }
    return render(request, 'users/register.html', context )


def profile(request):
    profile_form = UserProfileForm(request.POST or None, request.FILES, instance=request.user.profile)    
    user_form = UserUpdateForm(request.POST or None, instance=request.user)
    
    if profile_form.is_valid() and user_form.is_valid():
        user_form.save()
        profile_form.save()
        messages.success(request, "Your profile has been updated!")
        return redirect(request.path)
    
    context = {
        "user_form":user_form,
        "profile_form":profile_form
    }
    
    return render(request, "users/profile.html", context)    



def user_login(request):
    form = AuthenticationForm(request, data=request.POST)

    if form.is_valid():
        user = form.get_user()
        if user:
            messages.success(request, "Login successfull")
            login(request, user)
            return redirect('blog:postlist')
        else:
            messages.error(request, 'Login Failed!')
            return redirect('users:login')
    return render(request, 'users/login.html', {"form": form})


def user_logout(request):
    messages.success(request, 'You logged out succesfly')
    logout(request)
    return redirect('blog:postlist')