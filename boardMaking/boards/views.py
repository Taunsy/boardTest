from django.shortcuts import render, redirect
from .models import Board, Comment, ReComment


def write(request):
    return render(request, 'boards/write.html')


def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    board = Board()
    board.title = title
    board.content = content
    board.save()
    return redirect('/boards/lists/')


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


def displayUpdate(request, boardId):
    board = Board.objects.get(pk=boardId)
    context = {'board': board}
    return render(request, 'boards/update.html', context)


def update(request, boardId):
    board = Board.objects.get(pk=boardId)
    title = request.GET.get('title')
    content = request.GET.get('content')
    board.title = title
    board.content = content
    board.save()
    return redirect(f'/boards/read/{boardId}/')


def delete(request, boardId):
    board = Board.objects.get(pk=boardId)
    board.delete()
    return redirect('/boards/lists/')


def createComment(request, boardId):
    content = request.GET.get('commentContent')
    userName = request.GET.get('commentUserName')
    comment = Comment()
    comment.board = Board.objects.get(pk=boardId)
    comment.content = content
    comment.userName = userName
    comment.save()
    return redirect(f'/boards/read/{boardId}/')


def deleteComment(request, boardId, commentId):
    board = Board.objects.get(pk=boardId)
    comment = Comment.objects.filter(board__id=boardId, pk=commentId)
    comment.delete()
    return redirect(f'/boards/read/{boardId}/')


def createReComment(request, boardId, commentId):
    userName = request.GET.get('reCommentUserName')
    content = request.GET.get('reCommentContent')
    recomment = ReComment()
    recomment.comment = Comment.objects.get(pk=commentId)
    recomment.userName = userName
    recomment.content = content
    recomment.save()
    return redirect(f'/boards/read/{boardId}/')


def deleteReComment(request, boardId, commentId, reCommentId):
    board = Board.objects.get(pk=boardId)
    comment = Comment.objects.filter(board__id=boardId, pk=commentId)
    recomment = ReComment.objects.filter(
        comment__id=commentId, pk=reCommentId)
    recomment.delete()
    return redirect(f'/boards/read/{boardId}/')
