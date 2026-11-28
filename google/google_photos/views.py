from django.shortcuts import render, redirect
from .models import Googlephotos

def home(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.FILES.get('image')
        if image:
            Googlephotos.objects.create(title=title, image=image)
            return redirect('Googlephotos_home')
    
    Googlephotos = Googlephotos.objects.all().order_by('-uploaded_at')
    return render(request, 'Googlephotos/home.html', {'Googlephotoss': Googlephotos})