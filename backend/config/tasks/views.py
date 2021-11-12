from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render

from . import forms
from . import models


def create_update_task(request, context):
    form = forms.TaskForm(request.POST or None)

    if form.is_valid():
        task = form.save(commit=False)
        task.user = request.user
        task.save()

    context["create_form"] = form


def list_task(request, context):
    context["tasks"] = models.Task.objects.filter(user=request.user)


def delete_task(request, context):
    id_to_delete = request.POST.get("id")

    if id_to_delete and id_to_delete.isdigit():
        models.Task.objects.filter(id=id_to_delete).delete()
    elif id_to_delete == "all":
        models.Task.objects.all().delete()


@login_required
def main(request):
    context = {}
    list_task(request, context)
    create_update_task(request, context)
    delete_task(request, context)

    if request.method == "POST":
        return redirect(request.META.get('HTTP_REFERER'))
    return render(request, "tasks/main.html", context)
