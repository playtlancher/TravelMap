from django.shortcuts import render, redirect
from django.http import JsonResponse
from route.forms import AddRouteForm
from .models import Route, Waypoint
import json


def mainPage(request):
    routes = Route.objects.all()
    context = {"routes": routes}
    return render(request, 'route/mainPage.html', context)


def routeDetail(request, id):
    route = Route.objects.get(id=id)
    context = {"route": route,
               "start_longitude": route.start["longitude"],
               "start_latitude": route.start["latitude"],}
    if request.method == 'GET':
        waypoints = Waypoint.objects.filter(route=route)
        context["waypoints"] = waypoints
        return render(request, "route/route.html", context)
    return render(request, "route/route.html")


def addRoute(request):
    form = AddRouteForm()
    context = {"form": form}
    if request.method == 'GET':
        return render(request, "route/addRouteForm.html",context)
    if request.method == 'POST':
        form = AddRouteForm(request.POST)
        if form.is_valid():
            route = form.save(commit=False)
            waypoints_data = request.POST.getlist('waypoints[]')
            route.start = json.loads(waypoints_data.pop(0))
            route.end = json.loads(waypoints_data.pop(-1))
            route.user = request.user
            route.save()
            for waypoint_data in waypoints_data:
                waypoint = json.loads(waypoint_data)
                Waypoint.objects.create(
                    route=route,
                    location=waypoint['location'],
                    latitude=waypoint['latitude'],
                    longitude=waypoint['longitude']
                )

            return JsonResponse({'status': 'success'})
        else:
            print(form.errors)
    return JsonResponse({'status': 'error'}, status=400)