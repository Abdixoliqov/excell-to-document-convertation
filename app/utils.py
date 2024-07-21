
def file_path(instance, filename):
    return f"{filename}"

def handle_uploaded_file(f):  
    with open('/tel_senter/media/upload/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)  