import pika
import sys
import datetime
import time

data_ex = []
split_arr = []
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue

binding_keys = 'Bot-.*'

for binding_key in binding_keys:
    channel.queue_bind(
        exchange='topic_logs', queue=queue_name, routing_key=binding_key)

print(' [*] Waiting for logs. To exit press CTRL+C')

def compress(split_arr):
    print("Zipping")
    df.to_parquet('df.parquet.gzip', compression='gzip')

def callback(ch, method, properties, body):
    now_plus_5 = datetime.datetime.now() + datetime.timedelta(minutes = 5)
    
    arr = str(body)
    arr = arr[3:len(arr) - 3]
    split_arr = arr.split(", ")
    print(split_arr)
    data_ex.append(split_arr)

channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
compress(split_arr)
split_arr = split_arr[0:1]