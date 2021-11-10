from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import reverse

from . import forms
from . import models


@login_required
def create_task(request):
    if request.method == "POST":
        form = forms.TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
        i    task.save()
        return redirect('tasks:list')

    return render(request, "tasks/create.html", {"form": forms.TaskForm()})


def list_task(request):
    return render(request, "tasks/list.html", {"tasks": models.Task.objects.all()})

