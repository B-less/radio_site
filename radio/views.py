from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import RadioStation
from .forms import RadioStationForm


@login_required
def create_station(request):
    if request.method == "POST":
        form = RadioStationForm(request.POST, request.FILES)
        if form.is_valid():
            station = form.save(commit=False)
            station.owner = request.user  # request.user is guaranteed to be a User instance
            station.save()
            return redirect('home')
    else:
        form = RadioStationForm()
    return render(request, 'radio/create_station.html', {'form': form})

@login_required
def create_station(request):
    if request.method == 'POST':
        form = RadioStationForm(request.POST, request.FILES)
        if form.is_valid():
            station = form.save(commit=False)
            station.owner = request.user  # Ensures the station is linked to the account
            station.save()
            return redirect('dashboard_stations')
    else:
        form = RadioStationForm()
    return render(request, 'radio/create_station.html', {'form': form})




def home(request):
    stations = RadioStation.objects.all()
    return render(request, 'radio/home.html', {'stations': stations})
@login_required
def create_station(request):
    if request.method == "POST":
        form = RadioStationForm(request.POST, request.FILES)
        if form.is_valid():
            station = RadioStation.objects.filter(owner=request.user)
            station = form.save(commit=False)
            station.owner = request.user
            station.save()
            return redirect('home')
    else:
        form = RadioStationForm()
    return render(request, 'radio/create_station.html', {'form': form})


from django.shortcuts import render
from .models import RadioStation

def home(request):
    if request.user.is_authenticated:
        stations = RadioStation.objects.all()
    else:
        # For non-authenticated users, show only a limited number of stations
        stations = RadioStation.objects.all()[:5]
    return render(request, 'radio/home.html', {'stations': stations})


from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')  # Redirect to login page after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})



from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def dashboard_view(request):
    # Add any data you want to display on the dashboard
    context = {
        'stations_count': 10,  # Example data
        'listeners_count': 500,
    }
    return render(request, 'radio/dashboard.html', context)


from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.db.models import Sum


@login_required
def dashboard_home(request):
    # Sum of all current listeners across stations
    total_listeners = RadioStation.objects.aggregate(
        total=Sum('current_listeners')
    )['total'] or 0



    # Number of stations that are considered "active"
    # (You might define "active" as current_listeners > 0, or something else)
    active_stations = RadioStation.objects.filter(current_listeners__gt=0).count()

    # Sum of monthly plays across all stations
    monthly_plays = RadioStation.objects.aggregate(
        total=Sum('monthly_plays')
    )['total'] or 0

    context = {
        'total_listeners': total_listeners,
        'active_stations': active_stations,
        'monthly_plays': monthly_plays,
    }
    return render(request, 'radio/dashboard_home.html', context)





@login_required
def dashboard_view(request):
    # Dashboard Home
    context = {'stations_count': 10, 'listeners_count': 500}
    return render(request, 'radio/dashboard_home.html', context)

@login_required
def dashboard_analytics(request):
    # Dashboard Analytics
    context = {'analytics_data': 'Your analytics data here'}
    return render(request, 'radio/dashboard_analytics.html', context)

@login_required
def dashboard_stations(request):
    # Adjust this query based on your filtering needs.
    stations = RadioStation.objects.filter(owner=request.user)
    return render(request, 'radio/dashboard_stations.html', {'stations': stations})

@login_required
def dashboard_profile(request):
    # Dashboard Profile
    context = {'user': request.user}
    return render(request, 'radio/dashboard_profile.html', context)

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')


from django.shortcuts import render, get_object_or_404
from .models import  RadioStation

def station_detail(request, station_id):
    station = get_object_or_404(RadioStation, id=station_id)
    return render(request, 'radio/station_detail.html', {'station': station})


from django.shortcuts import render, get_object_or_404
from .models import RadioStation

def station_detail(request, station_id):
    station = get_object_or_404(RadioStation, id=station_id)
    return render(request, 'radio/station_detail.html', {'station': station})



@login_required
def create_station(request):
    if request.method == 'POST':
        form = RadioStationForm(request.POST, request.FILES)
        if form.is_valid():
            station = form.save(commit=False)
            station.owner = request.user
            station.save()
            return redirect('home')  # or wherever you want to go after creation
    else:
        form = RadioStationForm()
    return render(request, 'radio/create_station.html', {'form': form})


import requests

def update_station_listeners():
    # Suppose you have a dictionary of station_name -> current_listeners from your streaming server
    data = requests.get("http://localhost:8000/admin/stats").json()
    for station_data in data["stations"]:
        station_name = station_data["name"]
        listeners = station_data["listeners"]
        RadioStation.objects.filter(name=station_name).update(current_listeners=listeners)
