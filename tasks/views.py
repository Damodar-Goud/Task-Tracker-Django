from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Task
from .forms import TaskForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully!")
            return redirect("task_list")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})


@login_required
def task_list(request):
    query = request.GET.get("q")
    if query in [None, "", "None"]:
        query = None

    task_list = Task.objects.filter(user=request.user)

    if query:
        task_list = task_list.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )

    paginator = Paginator(task_list, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request, "tasks/task_list.html", {"page_obj": page_obj, "query": query}
    )


@login_required
def create_task(request):
    form = TaskForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        task = form.save(commit=False)
        task.user = request.user
        task.save()
        messages.success(request, "Task created successfully!")
        return redirect("task_list")
    return render(request, "tasks/create_task.html", {"form": form})


def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    form = TaskForm(request.POST or None, instance=task)
    task = get_object_or_404(Task, pk=pk, user=request.user)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Task updated successfully!")
        return redirect("task_list")
    return render(request, "tasks/update_task.html", {"form": form})


def delete_task(request, pk):
    # task = get_object_or_404(Task, pk=pk)
    task = get_object_or_404(Task, pk=pk, user=request.user)

    if request.method == "POST":
        task.delete()
        messages.success(request, "Task deleted successfully!")
        return redirect("task_list")
    return render(request, "tasks/delete_task.html", {"task": task})


"""
# CBV EXAMPLE       
from django.views.generic.edit import CreateView
from .models import Task

class TaskCreateView(CreateView):
    model = Task
    fields = ['title', 'description', 'completed']
    template_name = 'tasks/create_task.html'
    success_url = '/'

"""


@login_required
def dashboard(request):
    total = Task.objects.filter(user=request.user).count()
    completed = Task.objects.filter(user=request.user, completed=True).count()
    pending = Task.objects.filter(user=request.user, completed=False).count()

    context = {
        "total": total,
        "completed": completed,
        "pending": pending,
    }
    return render(request, "tasks/dashboard.html", context)
