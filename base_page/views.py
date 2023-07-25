from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect

def base_page(request):

    return HttpResponseRedirect(reverse('users:index',))