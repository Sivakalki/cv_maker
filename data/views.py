from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

from django.http import HttpResponse

def initial(request):                
    return render(request,'home.html')

def fill_details(request):
    if request.method=="POST" and request.FILES.get('profile'):
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        stream=request.POST['stream']
        objective=request.POST['objective']
        phone=request.POST['phone']
        mail=request.POST['mail']
        address=request.POST['address']
        
        skills=int(request.POST['skills'])
        skill_list = [request.POST.get(f'skill{i}', '') for i in range(0, skills + 1)]

            
        languages=int(request.POST['languages'])
        lang_list = [request.POST.get(f'lang{i}', '') for i in range(0, languages + 1)]
            
        certificates = int(request.POST['certificates'])
        certificate_list = [request.POST.get(f'certificate{i}', '') for i in range(0, certificates + 1)]
            
        projects = int(request.POST['projects'])
        pro_list = [request.POST.get(f'project{i}', '') for i in range(0, projects + 1)]
        
        degree=request.POST['degree']
        college=request.POST['college']
        year=request.POST['year']
        u_percentile = request.POST['u_percentile']
        inter_percentile=request.POST['inter_percentile']   
        tenth_percentile = request.POST['tenth_percentile']
        
        myphoto = request.FILES['profile']
        if myphoto.content_type=='image/png' :
            fs=FileSystemStorage()
            myphoto2 = fs.save(myphoto.name,myphoto)
            myphoto2_url = fs.url(myphoto2)
        else:
            return HttpResponse("please upload a PNG image")
        
        
        return render(request,'final.html',{
            'firstname':firstname.upper(),
            'lastname':lastname.upper(),
            'stream':stream.upper(),
            'objective':objective,
            'phone':phone,
            'mail':mail,
            'address':address,
            'skills':skills,
            'skill_list':skill_list,
            'languages':languages,
            'lang_list':lang_list,
            "certificates":certificates,
            'certificate_list':certificate_list,
            'projects':projects,
            'project_list':pro_list,
            'degree':degree,
            'college':college,
            'year':year,
            'u_percentile':u_percentile,
            'inter_percentile':inter_percentile,
            'tenth_percentile':tenth_percentile,
            'my_photo_url':myphoto2_url,
        })         
    return HttpResponse("details not saved")

# Create your views here.
