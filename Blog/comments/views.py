from django.shortcuts import render,get_object_or_404,redirect

from APP.models import Post

from .forms import CommentForm
from .models import Comment
# Create your views here.


def post_comment(request,post_pk):
    post = get_object_or_404(Post,pk=post_pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit= False)
            comment.post = post
            comment.save()
            return redirect(post)
        else:
            comment_list = post.comment_set.all()
            context = {'post':post,'form':form,'comment_list':comment_list}
            return render(request,'APP/detail.html',context)

    return redirect(post)

