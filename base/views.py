from django.shortcuts import render,get_list_or_404
from .models import Task
from django.contrib.auth.decorators import login_required

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
