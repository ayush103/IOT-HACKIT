import threading 

def print_cube(num): 
	""" 
	function to print cube of given num 
	"""
	print("Cube: {}".format(num * num * num)) 

def print_square(num): 
	""" 
	function to print square of given num 
	"""
	print("Square: {}".format(num * num)) 

def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

	t1 = threading.Thread(target=print_square, args=(10,)) 
	t2 = threading.Thread(target=print_cube, args=(10,)) 

	# starting thread 1 
	t1.start() 
	# starting thread 2 
	t2.start() 

	# wait until thread 1 is completely executed 
	t1.join() 
	# wait until thread 2 is completely executed 
	t2.join() 
    threading.start_new_thread( print_time, ("Thread-1", 2, ) )
    threading.start_new_thread( print_time, ("Thread-2", 4, ) )
    print "Error: unable to start thread"
    while 1:
        pass
	print("Done!") 
