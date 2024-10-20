from django.contrib import messages
from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request,"index.html")
# myapp/views.py
from django.shortcuts import render, redirect
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Submit Succsesfully")
            return redirect('Main:home')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})



def about(request):
    return render(request,"about.html")



