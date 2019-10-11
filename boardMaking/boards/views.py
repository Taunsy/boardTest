from django.shortcuts import render, redirect
from .models import Board


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
    num = int(num)
    board = Board.objects.get(pk=num)
    title = board.title
    content = board.content
    context = {'title': title, 'content': content}
    return render(request, 'boards/read.html', context)
