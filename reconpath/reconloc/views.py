from django.shortcuts import render
from forms import ImageUploadForm
from reconloc.models import ImgReferencia
from reconloc.models import ImgBusqueda
from django.http import HttpResponse
from django.http import HttpResponseForbidden
import cv2
from django.views.decorators.csrf import csrf_exempt
from reconpath import settings
import numpy as np

@csrf_exempt
def upload_pic(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            m = ImgReferencia()
            m.imagen = form.cleaned_data['image']
            m.nombre = form.cleaned_data['nombre']
            m.save()
            rutatotal = settings.MEDIA_ROOT+"/"+str(m.imagen)
            img = cv2.imread(rutatotal)
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            imggris = settings.MEDIA_ROOT+"/gray/"+str(m.imagen)
            cv2.imwrite(imggris,gray_image)
            m.gris = "gray/"+str(m.imagen)

            orb = cv2.ORB()
            kp1, des1 = orb.detectAndCompute(gray_image,None)
            imgdes = settings.MEDIA_ROOT+"/des/"+str(m.imagen)
            np.save(imgdes, des1)

            m.des = "des/"+str(m.imagen)+".npy"

            m.save()
            return HttpResponse('image upload success')
    return HttpResponseForbidden('allowed only via POST')

def imagen(request):
	return render(request, 'formimg.html')

def comparar(request):
    return render(request, 'formcomp.html')

@csrf_exempt
def compara(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            m = ImgBusqueda()
            m.imagen = form.cleaned_data['image']
            m.nombre = form.cleaned_data['nombre']
            m.save()
            rutatotal = settings.MEDIA_ROOT+"/"+str(m.imagen)
            img = cv2.imread(rutatotal)
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            imggris = settings.MEDIA_ROOT+"/gray/"+str(m.imagen)
            cv2.imwrite(imggris,gray_image)
            m.gris = "gray/"+str(m.imagen)

            orb = cv2.ORB()
            kp1, des1 = orb.detectAndCompute(gray_image,None)
            imgdes = settings.MEDIA_ROOT+"/des/"+str(m.imagen)
            np.save(imgdes, des1)

            m.des = "des/"+str(m.imagen)+".npy"

            m.save()
            return HttpResponse('image upload success')
    return HttpResponseForbidden('allowed only via POST')
