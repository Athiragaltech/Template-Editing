from django.shortcuts import render,HttpResponse,redirect
from . models import mobiles
from django.utils import timezone
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.shortcuts import render, redirect
from .models import mobiles
from django.contrib import messages
from django.http import HttpResponse


# Create your views here.
def index(request):
    data={
        'mob':mobiles.objects.all()

    }
    return render(request,'index.html',data)
def about(request):
    return render(request,'about.html')
def recent(request):
    return render(request,'recent.html')
def continu(request, id):
    mobile = mobiles.objects.filter(id=id)
    return render(request, 'continue_reading.html', {'mobiles': mobile})
    
def update(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        des = request.POST.get('des')
        img_file = request.FILES.get('img')
        edit = mobiles.objects.get(id=id)
        if edit.img:
            default_storage.delete(edit.img.name)
        if img_file:
            file_path = f"uploads/{img_file.name}"
            default_storage.save(file_path, ContentFile(img_file.read()))
        else:
            file_path = None  

        edit.name = name
        edit.des = des
        edit.img = file_path
        edit.date = timezone.now().date()
        
        edit.save()
        icon = '✏️'  # Unicode pencil symbol
        return HttpResponse(f'<script>alert("{icon} File updated successfully!"); window.location.href = "/";</script>')
        return redirect("/") 
    
    
def add(request):
    return render(request,'add.html')   
def insert(request):
    if request.method == "POST":
        name = request.POST.get('name')
        des = request.POST.get('des')
        img_file = request.FILES.get('img')
        if img_file:
            file_path = f"uploads/{img_file.name}"
            default_storage.save(file_path, ContentFile(img_file.read()))
            date = timezone.now().date()
            query = mobiles(name=name, des=des, img=file_path, date=date)
            query.save()
           
            icon = '\u2714'  # Unicode checkmark symbol
            return HttpResponse(f'<script>alert("{icon} File Added successfully!"); window.location.href = "/";</script>')

           
        return render(request, 'index.html')

    return HttpResponse("Method Not Allowed", status=405)
def delete(request,id):
    dlt=mobiles.objects.get(id=id)
    dlt.delete()
    icon = '\U0001F5D1'  # Unicode trash can symbol
    return HttpResponse(f'<script>alert("{icon} File Deleted successfully!"); window.location.href = "/";</script>')

    return redirect("/")   
def edit(request,id):
    data={"data":mobiles.objects.get(id=id)}
    return render(request,'edit.html',data)








