import datetime

# try:
#   print(x)
# except:
#   print("Something went wrong")
# else:
#   print("Nothing went wrong")

# try:
#   print(x)
# except:
#   print("Something went wrong")
# finally:
#   print("The 'try except' is finished")

try:
  f = open("demo.txt",'a') # exception if use default setting
  f.write("\nnow is " + str(datetime.datetime.now()))
except:
  print("Something went wrong when writing to the file")
finally:
  f.close()