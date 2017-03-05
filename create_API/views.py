from django.shortcuts import render, render_to_response

# Create your views here.


def list(request):
    return render_to_response("list.html")


def detail(request):
    return render_to_response("detail.html")


def createNew(request):
    return render_to_response("create.html")
