import json

import pika

params = pika.URLParameters("amqps://ojohqejq:RjVTZELllNh37ut3sNGyUieWF_RpX1oe@rattlesnake.rmq.cloudamqp.com/ojohqejq")
connection = pika.BlockingConnection(params)
channel = connection.channel()


def publish(mth, body):
    properties = pika.BasicProperties(mth)
    channel.basic_publish(exchange="", routing_key="main", body=json.dumps(body), properties=properties)
