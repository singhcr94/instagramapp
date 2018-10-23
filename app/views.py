from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from app.forms import signupform
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from .models import profilelist,image
# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = signupform(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('http://127.0.0.1:8000/login')
    else:
        form = signupform()
    return render(request, 'signup.html', {'form': form})
def myview(request):
    username=request.user
    p = image.objects.filter(postpics__exact='').get(user=request.user)
    user1=User.objects.all().exclude(username=username)
    foll = profilelist.objects.all().filter(followers=username)
    foll = (list(foll.values_list('following__username', flat=True)))
    x = User.objects.all().values_list('username', flat=True).exclude(username=username)
    x = list(x)
    y=image.objects.all().exclude(user=request.user)
    if request.method=='POST':
        value=request.POST
        val=list(value.values())
        print(val)
        id=User.objects.get(username__in=val)
        print(id)
        if profilelist.objects.filter(followers=username,following=id):
            upd=profilelist.objects.filter(followers=username,following=id).delete()
            return redirect('http://127.0.0.1:8000/accounts/profile/')
        else:
            update=profilelist.objects.get_or_create(following=id,followers=username)
            return redirect('http://127.0.0.1:8000/accounts/profile/')
    return render(request,'view.html',{'user1':user1,'x':x,'foll':foll,'p':p,'y':y})

def profile(request):
    use=User.objects.get(username=request.user)
    print(use)
    p=image.objects.filter(user=request.user)
    p=list(p)
    print(p)
    y=image.objects.filter(postpics__exact='').get(user=request.user)
    following=profilelist.objects.filter(followers=request.user).exclude(following=request.user).count()
    followers=profilelist.objects.filter(following=request.user).exclude(followers=request.user).count()
    return render(request,'profile.html',{'use':use,'following':following,'followers':followers,'y':y})

def reqprofile(request,username):
    req=User.objects.get(username=username)
    following=profilelist.objects.filter(followers=req).count()
    followers=profilelist.objects.filter(following=req).count()
    return render(request,'reqprofile.html',{'req':req,'following':following,'followers':followers})

def following(request,username):
    obj = User.objects.get(username=username)
    y = request.user
    print(obj)
    following = profilelist.objects.all().filter(following=obj).values_list('following__username', flat=True)
    following = list(following)
    print(following)
    x = profilelist.objects.all().filter(following=obj).values_list('followers__username', flat=True)
    x = list(following)
    foll = profilelist.objects.filter(followers=request.user).values_list('following__username', flat=True)
    if request.method == "POST":
        value = request.POST
        valueslist = list(value.values())
        user = User.objects.get(username__in=valueslist)
        if profilelist.objects.filter(followers=request.user, following=user):
            update = profilelist.objects.filter(followers=request.user, following=user).delete()
            return redirect('http://127.0.0.1:8000/accounts/profile/rehani/followers')
        else:
            update = profilelist.objects.get_or_create(following=user, followers=request.user)
    return render(request,'following.html',{'following':following},{'foll':foll})
def followers(request,username):
    obj=User.objects.get(username=username)
    y=request.user
    print(obj)
    following= profilelist.objects.all().filter(following=obj).values_list('followers__username', flat=True)
    following=list(following)
    print(following)
    x = profilelist.objects.all().filter(following=obj).values_list('followers__username', flat=True)
    x = list(following)
    foll=profilelist.objects.filter(followers=request.user).values_list('following__username',flat=True)
    if request.method=="POST":
        value=request.POST
        valueslist=list(value.values())
        user=User.objects.get(username__in=valueslist)
        if profilelist.objects.filter(followers=request.user,following=user):
            update=profilelist.objects.filter(followers=request.user,following=user).delete()
            return redirect('http://127.0.0.1:8000/accounts/profile/rehani/followers')
        else:
            update=profilelist.objects.get_or_create(following=user,followers=request.user)
    return render(request,'followers.html',{'following':following[1:],'foll':foll,'x':x[0]})
def myfollowers(request):
    username=request.user
    x = User.objects.all().values_list('username', flat=True).exclude(username=username)
    x = list(x)
    print(x)
    following=profilelist.objects.filter(followers=username).values_list('following__username',flat=True)
    foll=profilelist.objects.filter(following=username).exclude(followers=username)
    foll = (list(foll.values_list('followers__username', flat=True)))
    profile=image.objects.all()
    if request.method=="POST":
        value=request.POST
        valuelist=list(value.values())
        user=User.objects.get(username__in=valuelist)
        print(user)
        if profilelist.objects.filter(followers=request.user,following=user):
            upd=profilelist.objects.filter(followers=request.user,following=user).delete()
            return redirect('http://127.0.0.1:8000/accounts/profile/')
        else:
            update=profilelist.objects.get_or_create(following=user,followers=request.user)
            return redirect('http://127.0.0.1:8000/accounts/profile/')

    return render(request,'myfollowers.html',{'foll':foll,'following':following,'profile':profile})
def myfollowing(request):
    foll=User.objects.get(username=request.user)
    following=profilelist.objects.filter(followers=foll).exclude(following=request.user).values_list('following__username',flat=True)
    profile=image.objects.all()
    if request.method=="POST":
        value=request.POST
        li=list(value.values())
        id=User.objects.get(username__in=li)
        update=profilelist.objects.filter(following=id,followers=request.user).delete()
    return render(request,'myfollowing.html',{'following':following,'profile':profile})