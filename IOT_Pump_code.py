	import RPi.GPIO as GPIO                    	#Import GPIO library
	import time                              	#Import time library
	
	#below section is commented out. If you register on pushetta mobile app based notifications can be triggered 
	#from pushetta import Pushetta
	#API_KEY="426bf4f0ba39332fa4ad3ff7f859bcc5af7d6ff3" # API Key created from pushetta
	#CHANNEL_NAME="CHANNEL_NAME"			 	# channel name created from pushetta
	#p=Pushetta(API_KEY)

	GPIO.setmode(GPIO.BCM)                   	#Set GPIO pin numbering

	TRIG = 23                                	#Associate pin 23 to TRIG
	ECHO = 24                                	#Associate pin 24 to ECHO

	print("Distance measurement in progress")
	 
	GPIO.setup(TRIG,GPIO.OUT)                  	#Set pin as GPIO out
	GPIO.setup(ECHO,GPIO.IN)                   	#Set pin as GPIO in

	GPIO.setup(26, GPIO.OUT) 
	GPIO.output(26, GPIO.LOW)

	distance = 0
	while True:
	 
	  GPIO.output(TRIG, False)                 	#Set TRIG as LOW
	  print("Waitng For Sensor To Settle")
	  time.sleep(2)                            	#Delay of 2 seconds
	 
	  GPIO.output(TRIG, True)                  	#Set TRIG as HIGH
	  time.sleep(0.00001)                      	#Delay of 0.00001 seconds
	  GPIO.output(TRIG, False)                 	#Set TRIG as LOW
	 
	  while GPIO.input(ECHO)==0:               	#Check whether the ECHO is LOW
		pulse_start = time.time()              	#Saves the last known time of LOW pulse
	 
	  while GPIO.input(ECHO)==1:               	#Check whether the ECHO is HIGH
		pulse_end = time.time()                	#Saves the last known time of HIGH pulse
	 
	  pulse_duration = pulse_end - pulse_start 			#Get pulse duration to a variable
	 
	  distance = pulse_duration * 17150        	#Multiply pulse duration by 17150 to get distance
	  distance = round(distance, 2)            	#Round to two decimal points
	  print("Distance: " + str(distance) + "cm")
	 
	  if distance > 15.3:						# distance in CM's - set MINIMUM level for water in tank
		  print(" WATER PUMP -- STARTED ")
		  GPIO.output(26, GPIO.HIGH)
		  
		  # p.pushMessage(CHANNEL_NAME, "The pump has been STARTED ")
		  


	  if distance < 15.25:						#distance in CM's - set MAXIMUM level for water in tank
		  print(" WATER PUMP -- STOPPED")
		  GPIO.output(26, GPIO.LOW)
		  # p.pushMessage(CHANNEL_NAME, "The pump has been STOPPED ")
	 
	  time.sleep(2)
	 
