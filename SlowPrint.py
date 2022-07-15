import time

   
def slowprint(text, pause):
  for i in range (len(text)):
    print(text[i], end = '', flush = True)
    time.sleep(pause)
  print("")