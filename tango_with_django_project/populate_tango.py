import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings') # set the Django environment variable

import django
django.setup() # call django.setup() to import the django settings

from MyStreet.models import Street

def populate():
    add_Street(name = "Buchanan Street",
    average_safety_rate = "4",
    average_business_rate = "3",
    average_infrastructure_rate = "4",
    average_rate = "4",
    location = "Buchanan Street G1 Glasgow UK",
    image = "2.png")

    add_Street(name = "Yourkhill Street",
    average_safety_rate = "4",
    average_business_rate = "3",
    average_infrastructure_rate = "4",
    average_rate = "4",
    location = "Yourkhill Street G1 Glasgow UK",
    image = "1.png")

    add_Street(name = "Partick Street",
    average_safety_rate = "4",
    average_business_rate = "3",
    average_infrastructure_rate = "4",
    average_rate = "4",
    location = "Partick Street G1 Glasgow UK",
    image = "3.png")


def add_Street(name, average_safety_rate,average_business_rate ,average_infrastructure_rate,average_rate,location,image):
    S = Street.objects.get_or_create(name=name)[0]
    S.average_safety_rate = average_safety_rate
    S.average_rate=average_rate
    S.average_business_rate=average_business_rate
    S.average_infrastructure_rate = average_infrastructure_rate
    S.location=location
    S.image=image
    S.name=name
    return S
if __name__ == '__main__':
    print "Starting Street population script ..."
    populate()