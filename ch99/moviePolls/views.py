from django.shortcuts import render
from moviePolls.models import User
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.http import HttpResponse
import datetime

# Create your views here.
def index(request):
    latest_user_list = User.objects.all()
    context = { 'latest_user_list': latest_user_list }
    return render(request, 'moviePolls/index.html', context)

@csrf_exempt
def user_add_data(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        hobby = request.POST.get('hobby')
        movie = request.POST.get('movie')

        date = datetime.date.today()

        User.objects.create(userName=name, userEmail=email, hobby=hobby, favorite_movie=movie, date=date)

    return HttpResponse()

def test(request):
    return print("성공")