from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from .models import Task
from .forms import TaskForm
# Create your views here.

class Index(View):

    def get(self, request):
        form = TaskForm()
        tasks = Task.objects.all()

        context = {
            'form': form,
            'tasks': tasks
        }

        return render(request, 'tasks.html', context)

    def post(self, request):
        form = TaskForm(request.POST)

        if form.is_valid():
            cleaned_data = form.cleaned_data
            t = Task.objects.create(**cleaned_data)
            t.save()
            return redirect('index')

