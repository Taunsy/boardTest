from django.shortcuts import render, redirect
from .models import Board, Comment, ReComment
from .forms import BoardForm, CommentForm, ReCommentForm


def create(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save()
            board.save()
            return redirect('/boards/lists/')
        else:
            form = BoardForm()
            error = '엄한거 처넣지 말고 제대로 써라'
            return render(request, 'boards/write.html', {'form': form, 'error': error})
    else:
        form = BoardForm()
        error = ''
        return render(request, 'boards/write.html', {'form': form, 'error': error})


def lists(request):
    boards = Board.objects.all()
    context = {'boards': boards}
    return render(request, 'boards/lists.html', context)


def read(request, boardId):
    board = Board.objects.get(pk=boardId)
    comments = Comment.objects.filter(board__id=boardId)
    recomments = ReComment.objects.filter(comment__board__id=boardId)
    context = {'board': board, 'comments': comments, 'recomments': recomments}
    return render(request, 'boards/read.html', context)


def update(request, boardId):
    board = Board.objects.get(pk=boardId)
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board.title = form.cleaned_data['title']
            board.content = form.cleaned_data['content']
            board.save()
            return redirect(f'/boards/read/{boardId}/')
    else:
        form = BoardForm()
        context = {'form': form, 'board': board}
        return render(request, 'boards/update.html', context)


def delete(request, boardId):
    board = Board.objects.get(pk=boardId)
    board.delete()
    return redirect('/boards/lists/')


def createComment(request, boardId):
    board = Board.objects.get(pk=boardId)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            comment.board = board
            comment.save()
            return redirect(f'/boards/read/{boardId}')
        return redirect(f'/boards/read/{boardId}/')


def deleteComment(request, boardId, commentId):
    comment = Comment.objects.filter(board__id=boardId, pk=commentId)
    comment.delete()
    return redirect(f'/boards/read/{boardId}/')


def createReComment(request, boardId, commentId):
    comment = Comment.objects.get(pk=commentId)
    if request.method == 'POST':
        form = ReCommentForm(request.POST)
        if form.is_valid():
            recomment = form.save()
            recomment.comment = comment
            recomment.save()
        return redirect(f'/boards/read/{boardId}/')


def deleteReComment(request, boardId, commentId, reCommentId):
    recomment = ReComment.objects.filter(
        comment__id=commentId, pk=reCommentId)
    recomment.delete()
    return redirect(f'/boards/read/{boardId}/')
