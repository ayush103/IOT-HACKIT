import threading
import time
import csv
import pika

# Define a function for the thread
def send_data(threadName, delay, botNo):
	connection = pika.BlockingConnection(
	pika.ConnectionParameters(host='localhost'))
	channel = connection.channel()
	channel.exchange_declare(exchange='topic_logs', exchange_type='topic')
	routing_key = 'Bot' + str(botNo)
	with open('IoT'+ str(botNo%8) +'.csv', newline='') as File:  
		reader = csv.reader(File)
		for row in reader:
			time.sleep(delay)
			message = str(row)
			channel.basic_publish(
				exchange='topic_logs', routing_key=routing_key, body=message)
			print(routing_key, ": ", message)
	

t = [None] * 50
i=-1
read_file = [None] * 50
while i!= 49:
	t[i] = threading.Thread( target=send_data, args=("Bot-"+str(i), 0.5, i, ))
	i += 1

i = 0

while i!= 49:
	t[i].start()
	i += 1
while 1:
	pass
