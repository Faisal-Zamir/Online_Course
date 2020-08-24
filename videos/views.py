from django.shortcuts import render , redirect
from .models import video
from .forms import VideoForm
from users.models import Profile
from users.models import FollowUser
def home(request):
    if request.user.is_anonymous:
        return redirect('login')
    else:
            
        # print(request.user.profile)
        followedList = FollowUser.objects.filter(followed_by =request.user.profile)
        followedList2 = [] #it contain profile id of other user which followed by logged user
        print(followedList2)
        for e in followedList:
            followedList2.append(e.profile_id)
        all_videos = video.objects.filter(user_id__profile__in = followedList2).order_by('-id')

        context= {'all_videos':all_videos,  }
        return render(request, 'videos/index.html',context)


def upload_form(request):


    form= VideoForm(request.POST , request.FILES )
    if form.is_valid():
        user = form.save(commit=False)
        user.user_id = request.user.id
        user.save()
        return redirect('upload')

        

    
    user_videos= video.objects.filter(user_id=request.user.id)
    
    context= {'user_videos':user_videos,
              'form': form
              }
    
      
    return render(request, 'videos/upload_form.html', context)

def video_details(request, id):
    single_videos = video.objects.get(id=id)
    context= {'single_videos':single_videos,
              
              }
    return render(request, 'videos/video_details.html',context)

