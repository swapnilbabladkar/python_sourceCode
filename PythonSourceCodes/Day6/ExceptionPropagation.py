def f():
    try:
        x = int("five")
    except ValueError:
        print "Handled the error within the function"

try:
    f()
except ValueError:
    print "Received error from the called function"
    
        
