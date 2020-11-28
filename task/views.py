from django.shortcuts import render, redirect
from .models import TODO
from datetime import datetime
from django.views.decorators.csrf import csrf_protect, csrf_exempt

def home(request):
    tasks = TODO.objects.all().order_by('-id')
    context = {'tasks': tasks}
    return render(request, 'index.html', context)


@csrf_exempt
def add(request):
    title = request.POST['title']
    new_date = datetime.now()

    add_new = TODO(title=title, added_date=new_date)
    add_new.save()

    return redirect('/')


@csrf_exempt
def delete(request, pk):
    item = TODO.objects.get(id=pk)
    item.delete()
    return redirect('/')
     