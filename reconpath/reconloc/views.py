from django.shortcuts import render
from forms import ImageUploadForm
from reconloc.models import ImgReferencia
from django.http import HttpResponse
from django.http import HttpResponseForbidden
import cv2
from django.views.decorators.csrf import csrf_exempt
from reconpath import settings

@csrf_exempt
def upload_pic(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            m = ImgReferencia()
            m.imagen = form.cleaned_data['image']
            m.save()
            rutatotal = settings.MEDIA_ROOT+"/"+str(m.imagen)
            img = cv2.imread(rutatotal)
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            m = ImgReferencia()
            m.imagen = form.cleaned_data['image']
            m.save()
            imggris = settings.MEDIA_ROOT+"/gray/"+str(m.imagen)
            cv2.imwrite(imggris,gray_image)
            return HttpResponse('image upload success')
    return HttpResponseForbidden('allowed only via POST')

def imagen(request):
	return render(request, 'formimg.html')
