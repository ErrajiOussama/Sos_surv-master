from django.shortcuts import render

def IndexView(request):
    return render(request, 'index.html')

def FormView(request):
    return render(request, 'form.html')
