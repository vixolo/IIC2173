from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse

from .models import Comment
# Create your views here.

def commenter(request):
    return render(request, 'comments/commenter.html')

def comment(request):
    text = request.POST['commentText']
    if text == '':
        text = "///empty_commment///"
    comment = Comment(comment_text=text,
                      sender_ip=request.META['REMOTE_ADDR'],
                      time_sent=timezone.now())
    comment.save()
    return HttpResponseRedirect(reverse('comments:log'))

def log(request):
    latest_comments_list = Comment.objects.order_by('-time_sent')[:10]
    context = {'latest_comments_list': latest_comments_list}
    return render(request, 'comments/log.html', context)
