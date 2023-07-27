from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import Todo
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy


class TodoDeleteView(DeleteView):
    model = Todo
    template_name = "todo_delete.html"
    success_url = reverse_lazy("home")


def home_view(request):
    todos = Todo.objects.all()

    if request.method == "POST":
        form = TodoForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = TodoForm()
    

    return render(
        request,
        "index.html",
        {
            "section": "home",
            "form": form,
            "todos": todos,
        },
    )