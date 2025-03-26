from django.shortcuts import render

def index(request):
    return render(request, "index.html")  # Ensure index.html exists in templates folder
