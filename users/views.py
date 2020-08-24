from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile, FollowUser
from videos.models import video

def register(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, 'Your account is created '+username)
            return redirect('login')
    else:
        form = CreateUserForm()
    context = {'form':form}
    return render(request, 'users/register.html', context)

def login_user(request):
    if request.method == "POST":
      form = AuthenticationForm(request=request, data=request.POST)
      if form.is_valid():
        uname = form.cleaned_data['username']
        upass = form.cleaned_data['password']
        user = authenticate(username=uname, password=upass)
        login(request, user)
        
        messages.success(request, 'Logged in successfully !!')
        request.session['user'] = request.user.id
        return redirect('homepage')
    else:
        form = AuthenticationForm()
    context = {'form':form}
    return render(request, 'users/login.html',context)

def profile(request):

    user_profile = Profile.objects.get(user_id=request.user.id)
    user_video_count = video.objects.filter(user_id=request.user.id).count()
    print(user_video_count)
    context = {
        'user_profile':user_profile,
        'user_video_count':user_video_count
    }
    return render(request, 'users/profile.html',context)

def user_logout(request):
    logout(request)
    return redirect('login')

def dashboard(request):
    return render(request, 'users/dashboard.html')

def user_profiles(request):
    search_q = request.GET.get("search")
    if search_q == None:
        search_q = ""
    user_profiles =None
    user_profiles = Profile.objects.filter(user__username__icontains=search_q)

    if user_profiles:
        user_profiles = Profile.objects.filter(user__username__icontains=search_q)
    else:
        return render(request, 'users/not_found_user.html')

    
    for profile in user_profiles:
        profile.followed = False
        ob = FollowUser.objects.filter(profile = profile,followed_by=request.user.profile)
        if ob:
            profile.followed = True

    context = {
        'user_profiles':user_profiles
    }
    return render(request, 'users/all_profiles.html',context)

def subscribe(request, pk):
    user = Profile.objects.get(pk=pk)
    print(request.user.profile)
    FollowUser.objects.create(profile=user,followed_by=request.user.profile)
    return redirect('user_profiles')


def unsubscribe(request, pk):
    user = Profile.objects.get(pk=pk)
    FollowUser.objects.filter(profile=user, followed_by=request.user.profile).delete()
    return redirect('user_profiles')

def subscribed_videos(request):
    # print(request.user.profile)
    followedList = FollowUser.objects.filter(followed_by =request.user.profile)
    followedList2 = [] #it contain profile id of other user which followed by logged user
    print(followedList2)
    for e in followedList:
        followedList2.append(e.profile_id)
    all_videos = video.objects.filter(user_id__profile__in = followedList2).order_by('-id')

    context= {'all_videos':all_videos,  }
    return render(request, 'users/subscribed_videos.html',context)
