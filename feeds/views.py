from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Feed
from .forms import FeedForm


def feed_list(request):
    form = FeedForm()

    if request.method=="POST":
        form = FeedForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('feeds:index')
        
        else:
            messages.error(request, 'Unable to upload the Post')

    feeds = Feed.objects.all().order_by('-pub_date')

    context=  {'form': form, 'feeds': feeds}
    return render(request, 'feeds/feed_list.html', context)
