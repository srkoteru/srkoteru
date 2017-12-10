
try:
   f= open("test_file.txt")
   if (f.name== "corrept_file.txt"):
    raise exception 
   #a = asdf
except FileNotFoundError as a:
        print(a)
except Exception as e:
  print("error")
else:
   print(f.read()) 
finally:

    f.close()
    
   