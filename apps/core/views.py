from django.shortcuts import render, redirect
from .models import Uploaded
from .forms import Upload_Form
from django.http import JsonResponse

import fitz
import PIL.Image
import io
import os

import easyocr
import csv
import json

# Create your views here.
def index(request):
    files = Uploaded.objects.all()
    return render(request, "core/index.html", {
        "files": files
    })

def upload_file(request):
    form = Upload_Form(request.POST, request.FILES)
    if request.method == 'POST':
        files = request.FILES.getlist('file')
        for file in files:
            file_to_save = Uploaded(file = file)
            file_to_save.save()
        return redirect('index')
    return render(request, "core/upload.html", {
        "form": Upload_Form()
    })

def Extract(request, file_id):
    uploaded_files = Uploaded.objects.get(pk=file_id)
    file_path = uploaded_files.file.path

    pdf = fitz.open(file_path)
    counter = 1
    
    output_folder = os.path.join('media', 'extracted_images')

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    reader = easyocr.Reader(['en'])
    
    ocr_list = []
    for i in range(len(pdf)):
        page = pdf[i]
        images = page.get_images()
        for image in images:
            base_img = pdf.extract_image(image[0])
            print(base_img)
            image_data = base_img['image']
            img = PIL.Image.open(io.BytesIO(image_data))
            extension = base_img['ext']
            img_path = os.path.join(output_folder, f"image{counter}.{extension}")
            img.save(open(img_path, "wb"))
            counter+=1
    
            # OCR processing
            result = reader.readtext(img_path)
            print(result)

            for item in result:
                print(item[1])

                ocr_list.append(item[1])

            counter += 1
    ocr_json = {"ocr_text": ocr_list}
    print(ocr_json)

    # Create a CSV file and write OCR data to it
    csv_file_path = os.path.join('media', 'extracted_images', 'ocr_results.csv')
    # csv_file_path = csv_file_path.replace("\\","/")
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['OCR Result'])
        print("CSV File Path:", csv_file_path)

        for result in ocr_list:
            csv_writer.writerow([result])

    return render(request, "core/ocr.html", {
        "ocr_list": ocr_list,
        "csv_file_path": csv_file_path,
        "json": ocr_json
    })