from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render

from . import forms
from . import models


def create_update_circles(request, context):
    form = forms.CircleForm(request.POST or None)

    if form.is_valid():
        circle = form.save(commit=False)
        circle.user = request.user
        circle.save()

    context["create_circle"] = form


def list_objects(request, context):
    context["circles"] = models.Circle.objects.filter(user=request.user)


def delete_objects(request, context):
    id_to_delete = request.POST.get("id")

    if id_to_delete and id_to_delete.isdigit():
        models.Circle.objects.filter(id=id_to_delete).delete()
    elif id_to_delete == "all":
        models.Circle.objects.all().delete()


@login_required
def main(request):
    context = {}
    list_objects(request, context)
    create_update_circles(request, context)
    delete_objects(request, context)

    if request.method == "POST":
        return redirect(request.META.get('HTTP_REFERER'))
    return render(request, "circles/main.html", context)