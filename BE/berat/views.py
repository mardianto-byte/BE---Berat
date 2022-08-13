from django.shortcuts import render, redirect
from .forms import BeratForm
from .models import Berat

# Create your views here.
def berat_form(request):
 
    # create object of form
    if request.method == "GET":
        form = BeratForm()
        return render(request, "berat_register/berat_form.html", {"form": form})