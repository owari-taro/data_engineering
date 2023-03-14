from celery import shared_task
from sample.models import Record
import time

@shared_task
def save(desc:str):
    time.sleep(20)   
    print("calling.....................")
    record=Record.objects.create(desc=desc)
    print(record)
