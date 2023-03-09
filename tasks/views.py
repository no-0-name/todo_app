from django.shortcuts import render, redirect

from .models import *
from .forms import *


def TaskList(request):
    tasks = Task.objects.all().order_by("created")

    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    
    return render(request, "list.html", {"tasks": tasks, "form": form})


def TaskUpdate(request, pk):
    task = Task.objects.get(pk=pk)

    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect("/")
    
    return render(request, "update_task.html", {"form": form})


def TaskDelete(request, pk):
    task = Task.objects.get(pk=pk)

    if request.method == "POST":
        task.delete()
        return redirect("/")
    
    return render(request, "delete_task.html", {"task": task})