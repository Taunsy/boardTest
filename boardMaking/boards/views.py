from django.shortcuts import render, redirect
from .models import Board


def write(request):
    return render(request, 'boards/write.html')


def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    level = request.GET.get('level')
    board = Board()
    board.title = title
    board.content = content
    board.level = level
    board.save()
    return redirect('/boards/lists/')


def lists(request):
    boards = Board.objects.all()
    context = {'boards': boards}
    return render(request, 'boards/lists.html', context)


def read(request, num):
    board = Board.objects.get(pk=num)
    context = {'board': board}
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
