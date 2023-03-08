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
    participants = thread.participant.all()[0:3]
    if request.method == 'POST':
        response = Responses.objects.create(
            responder = request.user,
            thread = thread,
            body = request.POST.get('body')
        )
        thread.participant.add(request.user)
        return redirect('forum:thread', pk = thread.id)
    
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
            description=request.POST.get('description'),
        )
        return redirect('forum:thread_list')

    context = {'form': form}
    return render(request, 'forum/thread_form.html', context)