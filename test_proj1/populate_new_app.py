import os
# Set up Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_proj1.settings')  # Fixed settings module

import django
django.setup()

import random
from faker import Faker
from model.practice import Topic, AccessRecord, Webpage  # Corrected import statement


fakegen = Faker()
topics = ['Social', 'Search', 'Networking', 'Astronomy']  # Fixed topic names

def add_topic():
    topic_name = random.choice(topics)
    t, created = Topic.objects.get_or_create(topic_name=topic_name)
    return t

def populate(N=5):
    for _ in range(N):
        top = add_topic()

        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

if __name__ == "__main__":  # Fixed main check
    print("populating scripts")
    populate()
    print("populating complete")    
