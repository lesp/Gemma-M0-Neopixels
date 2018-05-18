import board, neopixel, time, random
pixpin = board.D1
numpix = 16

pixels = neopixel.NeoPixel(pixpin, numpix, brightness=.3)

while True:
    r = random.randint(0,128)
    g = random.randint(0,128)
    b = random.randint(0,128)
    for i in range(numpix):
        pixels[i] = (r, g, b)
        time.sleep(0.1)
    pixels.write()
    time.sleep(3)
  
