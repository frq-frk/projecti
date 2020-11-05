from django.shortcuts import render,get_list_or_404,redirect
from .models import Task
from django.contrib.auth.decorators import login_required
from .forms import StatusFormSet
from django.contrib.auth.models import User
from django.db.models import Q


# Create your views here.
@login_required(login_url='login')
def home(request):
    template = 'base/home.html'
    
    try:
        obj = Task.objects.filter(user = request.user)
    except:
        obj = 'none'
   
    # obj = get_list_or_404(Task,user = request.user)
    users = User.objects.filter(~Q(id = 1))
    return render(request,template,{'obj': obj,'users' : users})

def updatestatus(request,pk):
    obj = Task.objects.get(pk = pk)
    if obj.done:
        Task.objects.filter(pk = pk).update(done= False)
    else:
        Task.objects.filter(pk = pk).update(done = True)
    return redirect(home)

def usertaskstatus(request,id):
    template = 'base/usertaskstatus.html'
    # value_list = Task.objects.values_list(
    #     'user', flat=True
    #     ).distinct()
    # print(value_list)
    # group_by_value = {}
    # for value in value_list:
    #     group_by_value[value] = Task.objects.filter(user=value)
    # print(group_by_value)

    
    obj = Task.objects.filter(user = id)
    
    return render(request,template,{'obj' : obj})