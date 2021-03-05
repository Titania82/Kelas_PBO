
class student:
    """ A class representing a student"""
    def __init__ (self,n,a,g,h,s):
        self.full_name=n
        self.age=a
        self.gender=g
        self.height=h
        self.status=s
   
    def get_age(self):
        return self.age
    def get_gender(self):
        return self.gender
    def get_height(self):
        return self.height
    def get_status(self):
        return self.status
f = student ("titania emaniar", 20, "Female", 159, "Mahasiswa")
print (f.full_name)
print (f.get_age())
print (f.get_gender()) 
print (f.get_height())
print (f.get_status())