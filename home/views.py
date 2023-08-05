from django.shortcuts import render, redirect
from .models import Email

# Create your views here.
def index(request):
    if request.method == 'POST':
        email = request.POST['email']
        
        
        msg = Email.objects.create(email=email)
        msg.save();
        
        return redirect('success')
        
    else:
        return render(request, 'index.html')


def success(request):
    return render(request, 'success.html')