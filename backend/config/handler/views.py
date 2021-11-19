from abc import ABC

from circles import forms as circles_forms
from circles import models as circles_models
from django.shortcuts import redirect
from django.shortcuts import render
from tasks import forms as tasks_forms
from tasks import models as tasks_models


class CRUD(ABC):
    def __init__(self, name, request, ObjectForm, ObjectModel):
        self.context = {}
        self.name = name
        self.request = request
        self.ObjectForm = ObjectForm
        self.ObjectModel = ObjectModel

    def template_method(self):
        self.create_update()
        self.get_list()
        self.delete()
        return self.context

    def create_update(self):
        form = self.ObjectForm(self.request.POST or None)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = self.request.user
            obj.save()
        else:
            print(form.errors)

        self.context["create_" + self.name] = form

    def get_list(self):
        self.context[self.name] = self.ObjectModel.objects.filter(user=self.request.user)

    def delete(self):
        id_to_delete = self.request.POST.get("id")

        if id_to_delete and id_to_delete.isdigit():
            self.ObjectModel.objects.filter(id=id_to_delete).delete()
        elif id_to_delete == "all":
            self.ObjectModel.objects.all().delete()


def main(request):
    if not request.user.is_authenticated:
        return render(request, "timer_tasks/index.html")

    tasks = CRUD(
        name="tasks",
        request=request,
        ObjectModel=tasks_models.Task,
        ObjectForm=tasks_forms.TaskForm,
    ).template_method()

    circles = CRUD(
        name="circles",
        request=request,
        ObjectModel=circles_models.Circle,
        ObjectForm=circles_forms.CircleForm,
    ).template_method()

    if request.method == "POST":
        return redirect(request.META.get('HTTP_REFERER'))

    return render(request, "timer_tasks/main.html", tasks | circles)
