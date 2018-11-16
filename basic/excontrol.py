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
  f = open("demo.txt",'w') # exception if use default setting
  f.write("\nnow is " + str(datetime.datetime.now()))
except Exception as e:
  print("ex msg:"+str(e))
finally:
  f.close()

try:
  raise EOFError
except NameError as e: # get exception instance
  print("Name Error:"+str(e))
except Exception: # no exception instance
  print("Other Error:")