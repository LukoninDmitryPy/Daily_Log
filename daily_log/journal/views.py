from django.shortcuts import render
from .models import Note
from django.shortcuts import get_object_or_404, redirect
from .forms import PostForm


def index(request):
    notes = Note.objects.all()
    return render(request, 'journal/index.html', context={'notes':notes})

def add_note(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.save()
        return redirect('journal:add_note')
    return render(request, 'journal/add_note.html', context={'form': form})