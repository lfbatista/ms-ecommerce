import django
import json
import os
import pika

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

from products.models import Product

params = pika.URLParameters("amqps://ojohqejq:RjVTZELllNh37ut3sNGyUieWF_RpX1oe@rattlesnake.rmq.cloudamqp.com/ojohqejq")
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue="admin")


def callback(ch, mth, properties, body):
    id = json.loads(body)
    product = Product.objects.get(id=id)
    product.likes = product.likes + 1
    product.save()
    print("Product liked")


channel.basic_consume(queue="admin", on_message_callback=callback, auto_ack=True)

print("Starting consumer...")
channel.start_consuming()
channel.close()
