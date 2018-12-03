class MyException(Exception):
    def __init__(self,val):
        self.param = val
    def __str__(self):
        return repr(self.param)


try:
    raise MyException("My own exception.")
except MyException,ErrorMsg:
    print "Rcvd: ", ErrorMsg
    
