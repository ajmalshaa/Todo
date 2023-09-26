from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Q
from django.core.paginator import Paginator,InvalidPage,EmptyPage



# Create your views here.
from todoapp.models import Tasks


def home(request):
    if request.user.is_authenticated:
        created_user = request.user.username
        taskdisplay=Tasks.objects.filter(CreatedBy=request.user.username,IsActive=True,IsDelete=0).order_by('-CreatedDate')
        paginator=Paginator(taskdisplay,6)
        try:
            page=int(request.GET.get('page','1'))
        except:
            page='1'
        try:
            tasks=paginator.page(page)
        except(InvalidPage,EmptyPage):
            tasks=paginator.page(paginator.num_pages)
        return render(request,'index.html',{'task':tasks,'created_user':created_user,'name':'Home'})

    else:
        return redirect('signin')

def signup(request):
    print('in signup')
    if request.method == 'POST':
        name=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=name):
                messages.info(request,'Username already Taken')
                return redirect('signup')
            elif User.objects.filter(email=email):
                messages.info(request,'Email already in use')
                return redirect('signup')
            else:
                newuser=User.objects.create_user(username=name,email=email,password=password2)
                newuser.save()
                messages.info(request,'User created Successfully')
                return redirect('/')
        else:
            messages.info(request,'Passwords doesnot match')
            return redirect('signup')
    else:
        return render(request,'signup.html')
def signin(request):
    if request.method=='POST':
        username=request.POST['FirstName']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.error(request,'User is not registered')
            return redirect('signin')


    return render(request,'signin.html')
def update(request,update_id):

    updateTask=Tasks.objects.get(id=update_id)

    print(updateTask.IsActive)
    updateTask.IsActive='False'
    updateTask.save()
    return redirect('/')

def delete_update(request,delup_id):
    Delupdt=Tasks.objects.get(id=delup_id)
    Delupdt.IsDelete='1'
    Delupdt.save()
    return redirect('/')

def delete(request,del_id):
    print('delete def')
    Tasks.objects.filter(id=del_id).delete()
    return redirect('Deleted')

def edit(request):
    # EditTask=Tasks.objects.get(id=edit_id)
    return render(request,'update.html')

def complete(request):
    if request.user.is_authenticated:
        CompleteTask=Tasks.objects.filter(IsActive=False).order_by('-CreatedDate')
        created_user = request.user.username
        return render(request,'edit.html',{'comp':CompleteTask,'created_user':created_user})
    else:
        return redirect('/')
def signout(request):
    auth.logout(request)
    return redirect('/')

def Deleted(request):
    if request.user.is_authenticated:
        DeletedTask=Tasks.objects.filter(CreatedBy=request.user.username,IsDelete=1).order_by('-CreatedDate')
        created_user = request.user.username



    return render(request,'deletedTasks.html',{'DeletedTask':DeletedTask,'created_user':created_user})
def save(request):
    if request.user.is_authenticated:

        # print(created_user)
        if request.method=="POST":
            task= request.POST['task']
            date= request.POST['date']
            CreatedBy=request.user.username
            s=Tasks(Task=task,Date=date,CreatedBy=CreatedBy)
            s.save()
            task=date=""
            print('item added')
            return redirect('/')

def search(request):
    if request.user.is_authenticated:
        tasks=query=None
        if 'q' in request.GET:
            query=request.GET['q']
            tasks=Tasks.objects.all().filter(Q(Task__contains=query))
            created_user = request.user.username
            #paginator=Paginator(taskssearch,6)
            # try:
            #     page=int(request.GET.get('page','1'))
            # except:
            #     page='1'
            # try:
            #     tasks=paginator.page(page)
            # except(InvalidPage,EmptyPage):
            #     tasks=paginator.page(paginator.num_pages)


        return render(request,'search.html',{'query':query,'tasks':tasks,'created_user':created_user})

def retrieve(request,ret_id):

    updateTask=Tasks.objects.get(id=ret_id)


    updateTask.IsDelete='0'
    updateTask.save()
    return redirect('Deleted')

def open(request,open_id):

    updateTask=Tasks.objects.get(id=open_id)


    updateTask.IsActive='True'
    updateTask.save()
    return redirect('complete')
def Sessionout(request):
    return render(request,'SessionTimeout.html')




def pie_chart(request):
    if request.user.is_authenticated:
        opentasks=Tasks.objects.filter(CreatedBy=request.user.username,IsActive=0,IsDelete=0).count()
        Comptask=Tasks.objects.filter(CreatedBy=request.user.username,IsActive=1,IsDelete=0).count()
        deltasks=Tasks.objects.filter(CreatedBy=request.user.username,IsDelete=1).count()
#    print(Tasks.objects.filter(CreatedBy=request.user.username).count())
        labels = ['Open Tasks','Completed Tasks','Deleted Tasks']
        data = [int(opentasks),int(Comptask),int(deltasks)]

        queryset = Tasks.objects.order_by('-CreatedDate')[:5]
    # for task in queryset:
    #     labels.append(task.Task)
    #     data.append(task.CreatedDate)

        return render(request, 'pie_chart.html', {
            'labels': labels,
            'data': data,
        })