import cv2
import numpy as np
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from rembg import remove

def remove_background(image_path):
    # Load the image
    img = cv2.imread(image_path)
    # Remove the background using rembg
    result = remove(img)
    return result

def convert_to_greyscale(image):
    # Convert image to greyscale
    grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return grey

def process_image(image_path):
    # Remove background
    bg_removed = remove_background(image_path)
    # Convert the background removed image to greyscale
    greyscale = convert_to_greyscale(bg_removed)
    
    # Save the processed images
    bg_removed_path = 'media/bg_removed.png'
    greyscale_path = 'media/greyscale.png'
    
    cv2.imwrite(bg_removed_path, bg_removed)
    cv2.imwrite(greyscale_path, greyscale)
    
    return bg_removed_path, greyscale_path

def upload_image(request):
    if request.method == 'POST' and request.FILES['image']:
        image = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        uploaded_file_url = fs.url(filename)
        
        # Process the uploaded image
        bg_removed_path, greyscale_path = process_image(fs.path(filename))
        bg_removed_url = fs.url('bg_removed.png')
        greyscale_url = fs.url('greyscale.png')

        return render(request, 'index.html', {
            'uploaded_file_url': uploaded_file_url,
            'bg_removed_url': bg_removed_url,
            'greyscale_url': greyscale_url
        })
    return render(request, 'index.html')
