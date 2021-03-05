
class student:
    """ A class representing a student"""
    def __init__ (self,n,a,g,s,t):
        self.full_name=n
        self.age=a
        self.gender=g
        self.status=s
        self.alamat=t
     
   
    def get_age(self):
        return self.age
    def get_gender(self):
        return self.gender
    def get_status(self):
        return self.status
    def get_alamat(self):
        return self.alamat
     
f = student ("titania emaniar", 20, "Female", "Mahasiswa", "Bogor")
print ("Nama :", f.full_name)
print ("Umur :", f.get_age())
print ("gender :", f.get_gender()) 
print ("status :", f.get_status())
print ("alamat :", f.get_alamat())
