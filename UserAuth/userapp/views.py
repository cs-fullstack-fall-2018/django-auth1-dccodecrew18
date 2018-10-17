from django.shortcuts import render

from .models import userModel

def index(request):
    user_list= userModel.objects.all()
    context = {'user_list':user_list}
    return render (request,'registration/index',context)#templatesareawhere index is
from django.contrib.auth.decorators import login_required
def userIndex(request):
    filtereduser_list = userModel.objects.filter(username=request.user)
    context = {'filtereduser_list':filtereduser_list}
    return render (request,'userapptemp/index',context)
# Create your views here.
