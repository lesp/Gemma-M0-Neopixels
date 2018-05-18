import board, neopixel, time
pixpin = board.D1
numpix = 16

pixels = neopixel.NeoPixel(pixpin, numpix, brightness=.3)

while True:
    for i in range(numpix):
        pixels[i] = (255,0,0)
        time.sleep(0.01)
    pixels.write()

    for i in range(numpix):
        pixels[i] = (0,255,0)
        time.sleep(0.01)
    pixels.write()

    for i in range(numpix):
        pixels[i] = (0,0,255)
        time.sleep(0.01)
    pixels.write()

  
