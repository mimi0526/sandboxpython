class Employee:
        
    first_name = "n/a"
    last_name = "n/a"
    uid = "n/a"
    
    def __init__(self, fn, ln, uid):
	self.first_name = fn
	self.last_name = ln
        self.uid = uid

       
def main():
    e = Employee("nathan", "kevin", "012"))
    print(e.first_name)
    print(e.last_name)
    print(e.uid)
    
main()
