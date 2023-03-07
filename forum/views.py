from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from .models import Responses, Thread
from .forms import ThreadForm


def thread_list(request):
    thread_list = Thread.objects.all()
    context = {'thread_list' : thread_list}
    return render(request, 'forum/thread_list.html', context)

def thread(request, pk):
    thread = Thread.objects.get(id=pk)
    thread_responses = thread.responses_set.all()
    participants = thread.participants.all()
    if request.method == 'POST':
        response = Responses.objects.create(
            user = request.user,
            thread = thread,
            body = request.POST.get('body')
        )
        thread.participants.add(request.user)
        return redirect('thread', pk = thread.id)
    
    context = {'thread' : thread, 'thread_responses' : thread_responses, 'participants' : participants}

    return render(request, 'forum/thread.html', context)

@login_required(login_url='user:login')
def createThread(request):
    form =  ThreadForm()
    if request.method == 'POST':
        
        Thread.objects.create(
            host=request.user,
            question=request.POST.get('question'),
            topic=request.POST.get('topic'),
            name=request.POST.get('name'),
            description=request.POST.get('description'),
        )
        return redirect('forum:forum_list')

    context = {'form': form}
    return render(request, 'forum/thread_form.html', context)