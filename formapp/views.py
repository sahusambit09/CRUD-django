from django.shortcuts import render, redirect
from .forms import UserForm
from django.http import HttpResponse
from .models import User
import os
from os import path
from django.core.files.storage import FileSystemStorage


def showall(request):
    user = User.objects.all()
    return render(request, 'show.html', {"user": user})


def form_view(request):
    form = UserForm(request.POST, request.FILES)
    domain = request.build_absolute_uri()
    if form.is_valid():
        username = request.POST['username']
        email = request.POST['email']
        mobile = request.POST['mobile']
        # image = domain + 'media/profile/'+str(username) + str(request.FILES['image'])
        image = request.FILES['image']
        print(type(image))
        filename = image.name
        filename = "Img.jpeg"
        fs = FileSystemStorage(location='media/profile')
        image_file = fs.save(username + filename, image)
        document = request.FILES['document']
        imgUrl = domain + 'media/profile/' + image_file
        user = User(username=username, email=email, mobile=mobile, image=imgUrl, document=document)
        user.save()
        return redirect('/showall/')
    return render(request, 'index.html', {'form': form})


def edit(request, id):
    user = User.objects.get(id=id)
    return render(request, 'edit.html', {'user': user})


def update(request, id):
    user = User.objects.get(id=id)
    print(user.username)
    form = UserForm(request.POST, request.FILES, instance=user)

    if form.is_valid():
        form.save()
    return redirect("/showall/")

    return render(request, 'edit.html', {'user': user})


def destroy(request, id):
    user = User.objects.get(id=id)
    image = user.image
    image_path = str(image).split('/', 3)[3]
    if path.exists(image_path):
        os.remove(image_path)
    user.delete()
    return redirect("/showall/")
