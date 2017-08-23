# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.
import time
import math
import random

from neopixel import *
from ctypes import *


# LED strip configuration:
LED_COUNT      = 300      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 100     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0
LED_STRIP      = ws.SK6812_STRIP_RGBW	
#LED_STRIP      = ws.SK6812W_STRIP

def colorSet(strip, color):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
    strip.show()

# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
	"""Wipe color across display a pixel at a time."""
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.show()
		time.sleep(wait_ms/1000.0)

def theaterChase(strip, color, wait_ms=50, iterations=10):
	"""Movie theater light style chaser animation."""
	for j in range(iterations):
		for q in range(3):
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, color)
			strip.show()
			time.sleep(wait_ms/1000.0)
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, 0)

def wheel(pos):
	"""Generate rainbow colors across 0-255 positions."""
	if pos < 85:
		return Color(pos * 3, 255 - pos * 3, 0)
	elif pos < 170:
		pos -= 85
		return Color(255 - pos * 3, 0, pos * 3)
	else:
		pos -= 170
		return Color(0, pos * 3, 255 - pos * 3)

def rainbow(strip, wait_ms=20, iterations=1):
	"""Draw rainbow that fades across all pixels at once."""
	for j in range(256*iterations):
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, wheel((i+j) & 255))
		strip.show()
		time.sleep(wait_ms/1000.0)

def rainbowCycle(strip, wait_ms=10, iterations=2):
	"""Draw rainbow that uniformly distributes itself across all pixels."""
	for j in range(256*iterations):
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, wheel(((i * 256 / strip.numPixels()) + j) & 255))
		strip.show()
		time.sleep(wait_ms/20000.0)

def theaterChaseRainbow(strip, wait_ms=50):
	"""Rainbow movie theater light style chaser animation."""
	for j in range(256):
		for q in range(4):
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, wheel((i+j) % 255))
			strip.show()
			time.sleep(wait_ms/1000.0)
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, 0)

def greenBrightness(pos):
	if pos == 0:
		return 0xDD0000
	elif pos == 1:
		return 0xBB0000
	elif pos == 2:
		return 0x990000 

def greenDrive(strip, wait_ms=20):
	for j in range(256):
		for q in range(3):
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, greenBrightness(q))
			strip.show()
			time.sleep(wait_ms/1000.0)
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, 0)
			colorSet(strip, 0x00ABCD)

#### Kelly's methods ####
#this function is the same as cyclone aka cylon except the bar goes back and forth instead of one direction
def jamrecords(strip, width, wait_ms=20):
	reverse = 0
	if width < 3:
		width = 3
	if width > 255:
		width = 255
#	width_factor = int(255/width)
#	if width_factor == 0:
#		width_factor = 1
#	print('Width factor set to %d', width_factor)
	for i in range(0, strip.numPixels()):
#		print('Process LED %d' % i)
		if i < width:
			for j in range(0, width):
				strip.setPixelColor(i+j, wheel(i+j))
#				print('Set LED %d to %d',i+j, Color(0, width_factor*j, 0))
			strip.show()
			time.sleep(wait_ms/1000.0)
		elif i == strip.numPixels():
			for j in range(width,0):
				strip.setPixelColor(i+j, wheel(i+j))
##				print('Set LED %d to %d',i+j, Color(0, width_factor*j, 0))
			strip.show()
			time.sleep(wait_ms/1000.0)
		else:
			for j in range (0-width, 0+width):
				if (j == (0-width)):
					strip.setPixelColor(i+j, 0)
				elif (j == (0+width)):
					strip.setPixelColor(i+j, 0)
				else:
					if i < 256:
						strip.setPixelColor(i+j, wheel(i))
					else:
						strip.setPixelColor(i+j, wheel(i % 256))
#				print('Set LED %d to %d',i+j, Color(0, width_factor*j, 0))
			strip.show()
			time.sleep(wait_ms/1000.0)
	for i in range(strip.numPixels(), 0, -1): 
		if i < width:
			for j in range(0, width):
				strip.setPixelColor(i+j, wheel(i+j))
#				print('Set LED %d to %d',i+j, Color(0, width_factor*j, 0))
			strip.show()
			time.sleep(wait_ms/1000.0)
		elif i == strip.numPixels():
			for j in range(width,0):
				strip.setPixelColor(i+j, wheel(i+j))
#				print('Set LED %d to %d',i+j, Color(0, width_factor*j, 0))
			strip.show()
			time.sleep(wait_ms/1000.0)
			reverse = 1
		else:
			for j in range (0-width, 0+width):
				if (j == (0-width)):
					strip.setPixelColor(i+j, 0)
				elif (j == (width-1)):
					strip.setPixelColor(i+j, 0)
				else:
					if i < 256:
						strip.setPixelColor(i+j, wheel(i))
					else:
						strip.setPixelColor(i+j, wheel(i % 256))
#				print('Set LED %d to %d',i+j, Color(0, width_factor*j, 0))
			strip.show()
			time.sleep(wait_ms/1000.0)
			
def cyclone(strip, width, wait_ms=20):
	reverse = 0
	if width < 3:
		width = 3
	if width > 255:
		width = 255
#	width_factor = int(255/width)
#	if width_factor == 0:
#		width_factor = 1
#	print('Width factor set to %d', width_factor)
	for i in range(0, strip.numPixels()):
#		print('Process LED %d' % i)
		if i < width:
			for j in range(0, width):
				strip.setPixelColor(i+j, wheel(i+j))
#				print('Set LED %d to %d',i+j, Color(0, width_factor*j, 0))
			strip.show()
			time.sleep(wait_ms/1000.0)
		elif i == strip.numPixels():
			for j in range(width,0):
				strip.setPixelColor(i+j, wheel(i+j))
#				print('Set LED %d to %d',i+j, Color(0, width_factor*j, 0))
			strip.show()
			time.sleep(wait_ms/1000.0)
		else:
			for j in range (0-width, 0+width):
				if (j == (0-width)):
					strip.setPixelColor(i+j, 0)
				elif (j == (0+width)):
					strip.setPixelColor(i+j, 0)
				else:
					if i < 256:
						strip.setPixelColor(i+j, wheel(i))
					else:
						strip.setPixelColor(i+j, wheel(i % 256))
#				print('Set LED %d to %d',i+j, Color(0, width_factor*j, 0))
			strip.show()
			time.sleep(wait_ms/1000.0)

#### Sam's Methods ####  

def twinkleLoop(strip):
	while True:
		rainbowTwinkle(strip, 100, 30)	

def rainbowTwinkle(strip, count, speedDelay):	
	colorSet(strip, Color(0,0,0))
	i = 0
	for i in range (0, count):
		pixel = random.randint(0,LED_COUNT)	 
		strip.setPixelColor(pixel, Color(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
		strip.show()
		time.sleep(speedDelay/1000.0)
		i += 1

def rainbowWhiteOutLoop(strip):
	while True:
		rainbowWhiteOut(strip, 3)
		
def rainbowWhiteOut(strip, cycleLength):
		for i in range (0, cycleLength): 	
			rainbowCycle(strip)
		LED_BRIGHTNESS = 50
		colorWipe(strip, Color(0, 0, 0, 255))
		LED_BRIGHTNESS = 100

def sparkleLoop(strip):
	for i in range (0, LED_COUNT / 2):
		DiamondSparkle(strip, 0x10, 0x10, 0x10, 40, random.randint(100,1000))
 
def DiamondSparkle(strip, red, green, blue, SparkleDelay, SpeedDelay):
      colorSet(strip, Color(red,green,blue))
      #rainbow(strip)
      pixel = random.randint(0,LED_COUNT)
      pixel1 = random.randint(0,LED_COUNT)
      pixel2 = random.randint(0,LED_COUNT)


      strip.setPixelColor(pixel, Color(0xff,0xff,0xff))
      strip.setPixelColor(pixel1, Color(0xff,0xff,0xff))
      strip.setPixelColor(pixel2, Color(0xff,0xff,0xff))


      strip.show()
      time.sleep(SparkleDelay/1000.0)
      strip.setPixelColor(pixel, Color(red,green,blue))
      strip.setPixelColor(pixel1, Color(red,green,blue))
      strip.setPixelColor(pixel2, Color(red,green,blue))
      strip.show()
      time.sleep(SpeedDelay/1000.0)
      
def kellySamInfiniteLoop(strip):
	while True:
		for a in range (0, 2):
			#jamrecords(strip, width, wait_ms=20)
			jamrecords(strip, 15)
			
		#DTF(strip,20) //not going to use
		theaterChaseRainbow(strip)
			
		
		for b in range (0, 45):
			#DiamondSparkle(strip, red, green, blue, SparkleDelay, SpeedDelay)
			#increase sparkleDelay for slower sparkles
			#decrease speedDelay for faster cycles
			DiamondSparkle(strip, 0x10, 0x10, 0x10, 40, random.randint(100,1000))
			
			
		for c in range (0, 15):
			#rainbowTwinkle(strip, count, speedDelay)
			#increase count for more colored pixels per cycle
			#decrease speedDelay for faster cycles
			rainbowTwinkle(strip, 100, 30)	
			
			
		for d in range (0, 2):
			#rainbowWhiteOut(strip, cycleLength):
			#increase cycleLength to make rainbow longer
			rainbowWhiteOut(strip, 3)

############## end ##################

def cylon(strip, width, wait_ms=20):
        if  width < 3:
	        width = 3
	if width > 255:
		width = 255
#	width_factor = int(255/width)
#	if width_factor == 0:
#		width_factor = 1
#	print('Width factor set to %d', width_factor)
	for i in range(0, strip.numPixels()):
#		print('Process LED %d' % i)
		if i < width:
			for j in range(0, width):
				strip.setPixelColor(i+j, wheel(i+j))
#				print('Set LED %d to %d',i+j, Color(0, width_factor*j, 0))
			strip.show()
			time.sleep(wait_ms/1000.0)
		elif i == strip.numPixels():
			for j in range(width,0):
				strip.setPixelColor(i+j, wheel(i+j))
#				print('Set LED %d to %d',i+j, Color(0, width_factor*j, 0))
			strip.show()
			time.sleep(wait_ms/1000.0)
		else:
			for j in range (0-width, 0+width):
				if (j == (0-width)):
					strip.setPixelColor(i+j, 0)
				elif (j == (0+width)):
					strip.setPixelColor(i+j, 0)
				else:
					if i < 256:
						strip.setPixelColor(i+j, wheel(i))
					else:
						strip.setPixelColor(i+j, wheel(i % 256))
#				print('Set LED %d to %d',i+j, Color(0, width_factor*j, 0))
			strip.show()
			time.sleep(wait_ms/1000.0)

def white_test(strip):
    for i in range (0, 10):
        strip.setPixelColor(i, 0x0)


# Main program logic follows:
if __name__ == '__main__':
	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
	# Intialize the library (must be called once before other functions).
	strip.begin()

	print ('Press Ctrl-C to quit.')
	while True:
#		# Color wipe animations.
#		colorWipe(strip, Color(255, 0, 0))  # Red wipe
#		colorWipe(strip, Color(0, 255, 0))  # Blue wipe
#		colorWipe(strip, Color(0, 0, 255))  # Green wipe
#		colorWipe(strip, Color(0, 0, 0, 255))  # White wipe
#		colorWipe(strip, Color(255, 255, 255))  # Composite White wipe
#	        colorWipe(strip, Color(255, 255, 255, 255))  # Composite White + White LED wipe
		# Theater chase animations.
#		theaterChase(strip, Color(127, 0, 0))  # Red theater chase
#	        theaterChase(strip, Color(0, 127, 0))  # Green theater chase
#		theaterChase(strip, Color(0, 0, 127))  # Blue theater chase
#		theaterChase(strip, Color(0, 0, 0, 127))  # White theater chase
#		theaterChase(strip, Color(127, 127, 127, 0))  # Composite White theater chase
#	        theaterChase(strip, Color(127, 127, 127, 127))  # Composite White + White theater chase
		# Rainbow animations.
	#	rainbow(strip)
	#	rainbowCycle(strip)
#		theaterChaseRainbow(strip)
	#	colorSet(strip, Color(0,0,0))
	#	cylon(strip, 10)
	#	greenDrive(strip)
              #sparkleLoop(strip)
		#twinkleLoop(strip)
	#	rainbowWhiteOutLoop(strip)	
		kellySamInfiniteLoop(strip)
#white_test(strip)
