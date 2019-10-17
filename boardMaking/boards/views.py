from django.shortcuts import render, redirect
from .models import Board, Comment


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


def read(request, num):
    board = Board.objects.get(pk=num)
    comments = Comment.objects.filter(board__id=num)
    context = {'board': board, 'comments': comments}
    return render(request, 'boards/read.html', context)


def displayUpdate(request, num):
    board = Board.objects.get(pk=num)
    context = {'board': board}
    return render(request, 'boards/update.html', context)


def update(request, num):
    board = Board.objects.get(pk=num)
    title = request.GET.get('title')
    content = request.GET.get('content')
    board.title = title
    board.content = content
    board.save()
    return redirect(f'/boards/read/{num}/')


def delete(request, num):
    board = Board.objects.get(pk=num)
    board.delete()
    return redirect('/boards/lists/')


def createComment(request, num):
    content = request.GET.get('commentContent')
    userName = request.GET.get('commentUserName')
    comment = Comment()
    comment.board = Board.objects.get(pk=num)
    comment.content = content
    comment.userName = userName
    comment.save()
    return redirect(f'/boards/read/{num}')


def deleteComment(request, num1, num2):
    board = Board.objects.get(pk=num1)
    comment = Comment.objects.filter(board__id=num1, pk=num2)
    comment.delete()
    return redirect(f'/boards/read/{num1}')
