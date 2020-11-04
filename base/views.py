from django.shortcuts import render,get_list_or_404,redirect
from .models import Task
from django.contrib.auth.decorators import login_required
from .forms import StatusFormSet


# Create your views here.
@login_required(login_url='login')
def home(request):
    template = 'base/home.html'
    
    try:
        obj = Task.objects.filter(user = request.user)
    except:
        obj = 'none'
   
    # obj = get_list_or_404(Task,user = request.user)
    return render(request,template,{'obj': obj})

def updatestatus(request,pk):
    obj = Task.objects.get(pk = pk)    
    if obj.done:
        obj.done = 'False'
    else:
        obj.done = 'True'
    obj.save()
    return redirect(home)

def usertaskstatus(request):
    template = 'base/usertaskstatus.html'
    # value_list = Task.objects.values_list(
    #     'user', flat=True
    #     ).distinct()
    # print(value_list)
    # group_by_value = {}
    # for value in value_list:
    #     group_by_value[value] = Task.objects.filter(user=value)
    # print(group_by_value)

    obj = Task.objects.all()
    
    return render(request,template,{'obj' : obj})