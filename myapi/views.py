from django.shortcuts import render, redirect
from faker import Faker
from rest_framework.response import Response
fake = Faker()
import pycountry
import random
from django.utils.crypto import get_random_string
from .serializer import UserSerializer
from .models import User, Activity
from rest_framework.views import APIView

# API VIEW
class userList(APIView):

    def get(self,request):
        queryset = User.objects.all().order_by('id')
        serializer = UserSerializer(queryset,many=True)
        member = serializer.data
        return Response({'ok':True,'members':member})

# PAGE FOR ADDING NEW MEMBERS
def UserView(request):
    unum = User.objects.all().count()
    context = {
        'unum': unum,
    }
    return render(request,'userform.html',context)


# LOGIC AND QUERIES FOR ADDING SPECIFIED NUMBER OF USERS AND ACTIVITIES
def AddView(request):
    data = request.POST.copy()
    unum = data.get('user_number')
    anum = data.get('activity_number')
    context = {}
    unum = int(unum)
    anum = int(anum)
    for x in range(unum):
        name = fake.name()
        r = random.randint(0,248)
        tz = list(pycountry.countries)[r].name
        user = User()
        user.real_name = name
        user.tz = tz
        user.save()
        for y in range(anum):
            activity = Activity()
            activity.start_time = fake.date_time()
            activity.end_time = fake.date_time()
            auser = User.objects.get(real_name=user.real_name,tz=user.tz)
            activity.user = auser
            activity.save()

    return redirect('home')


# HOMEPAGE
def home(request):
    num = User.objects.all().count()
    context = {
        'num': num
    }
    return render(request,'home.html',context)


# TABLE FOR SHOWING LIST OF USERS
def AllUserView(request):
    user = User.objects.all()
    context = {
        'user':user
    }
    return render(request,'alluser.html',context)