from django.shortcuts import redirect

from comment.forms import AddCommentForm
from route.models import Route


def addComment(request, id):
    if request.method == 'POST':
        form = AddCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.route = Route.objects.get(id=id)
            comment.save()
    return redirect(f'/routes/{id}')
