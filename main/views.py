from django.shortcuts import redirect, render, get_object_or_404
from .models import Event, Contact
from django.contrib import messages
from .fusioncharts import FusionCharts
import uuid


# Create your views here.
def index(request):
    title = 'Landing Page'
    context = {'title':title}
    return render(request, 'index.html', context)

def reservation(request):

    if request.method == 'GET':
        title = 'Reservations'
        poster = 'Book A Hall'
        desc = ' Our booking platform offers an array of choices whether you are looking for a professional host for your business conference or just want to bring your friends for a casual party.'
        context = {'title':title, 'poster':poster, 'desc':desc}
        return render(request, 'reservation.html', context)

    else:
        owner_first_name = request.POST['fname'] 
        owner_last_name = request.POST['lname']
        email = request.POST['email']
        name = request.POST['name']
        date = request.POST['date']
        hall = request.POST['hall']

        if Event.objects.filter(date=date):
            messages.error(request, 'Date is Already Booked')
            return redirect('reservation')
        else:
            event = Event.objects.create(owner_first_name=owner_first_name, owner_last_name=owner_last_name, email=email, name=name, date=date, hall=hall, id=str(uuid.uuid4())[:5])
            event.save()
            return redirect('index')
    

def about(request):
    title = 'About'
    poster = 'About Atlantis'
    desc = ' Atlantis is the ideal destination for any occasion, be it a business meeting or a special event. We offer an extensive range of options to cater to your needs.'
    context = {'title':title, 'poster':poster, 'desc':desc}
    return render(request, 'about.html', context)

def contact(request):
    if request.method == 'GET':
        title = 'Contact'
        poster = 'Contact'
        desc = "We would love to hear from you, so please don't hesitate to get in touch."
        context = {'title':title, 'poster':poster, 'desc':desc}
        return render(request, 'contact.html', context)
    
    else:
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        contact = Contact.objects.create(fname=fname, lname=lname, email=email, subject=subject, message=message)
        contact.save()
        return redirect('index')

def adminPage(request):
    title = 'Admin Dashboard'

    events = Event.objects.all()


    dataSource = {}
    dataSource['chart'] = {
        "caption":'Traffic',
        "subCaption":'Atlantis',
        "xAxisName":"Events",
        "yAxisName":'Frequency',
        "theme":"fusion"
    }

    dataSource['data']=[]

    for key in events:
        data={}
        data['label'] = key.name
        data['value'] = Event.objects.filter(name=key.name).count()
        dataSource['data'].append(data)

    column2d = FusionCharts('column2D', 'ex1', '600', '350', 'chart', 'json', dataSource)

    context = {'title':title, 'chart':column2d.render(), 'events':events}
    return render(request, 'adminbase.html', context)

def updateStatus(request, id):
    event = Event.objects.get(id=id)
    
    if request.method == 'GET':
        title = 'Edit Event'
        poster = 'Book A Hall'
        desc = ' Our booking platform offers an array of choices whether you are looking for a professional host for your business conference or just want to bring your friends for a casual party.'
        context = {'title':title, 'event':event, 'poster':poster, 'desc':desc}

        return render(request, 'update.html', context)

    else:
        event.owner_first_name = request.POST['fname'] 
        event.owner_last_name = request.POST['lname']
        event.email = request.POST['email']
        event.name = request.POST['name']
        event.date = request.POST['date']
        event.hall = request.POST['hall']
        event.status = request.POST['status']
        event.save()
        return redirect('admin-page')



def deleteEvent(request,id):
    event = Event.objects.get(id=id)
    event.delete()
    return redirect('admin-page')
