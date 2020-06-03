from django.shortcuts import render
from .models import Destination

# Create your views here.

def home(request):
    # dest1 = Destination(name='Mumbai', desc='The City That Never Sleeps.', price = 500, img='destination_1.jpg')
    # dest2 = Destination(name='Indonesia', desc='Nulla pretium tincidunt felis, nec.', price = 679, img='destination_2.jpg', offer=True)
    # dest3 = Destination(name='San Francisco', desc='Industrial City', price = 800, img='destination_3.jpg')
    
    destinations = Destination.objects.all()

    print('Destination : ', destinations)

    # destinations = [dest1, dest2, dest3]

    return render(request, 'index.html', {'destinations' : destinations})
