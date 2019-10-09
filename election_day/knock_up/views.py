from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def add_voter(request):
    return HttpResponse("ask for voter number")

def check_voter(request):
    return HttpResponse("review ")

def delete_voter(request):
    return HttpResponse("which one was entered wrongly")

def list_voters(request):
    """
    Admin View
    Promised votes who haven't yet actually voted
    """
    return HttpResponse("admin sees voters to assign to knockers")

def assign_voters(request):
    return HttpResponse("admin assigns voters to knockers")

def knocker_list (request):
    return HttpResponse("list of people to knock up")

def knocker_delete (request):
    return HttpResponse("don't knock these voters again")

