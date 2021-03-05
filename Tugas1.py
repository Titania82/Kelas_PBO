
class student:
    """ A class representing a student"""
    def __init__ (self,n,a,g,s,u,t):
        self.full_name=n
        self.age=a
        self.gender=g
        self.status=s
        self.universitas=u
        self.alamat=t
    def get_age(self):
        return self.age
    def get_gender(self):
        return self.gender
    def get_status(self):
        return self.status
    def get_universitas(self):
        return self.universitas
    def get_alamat(self):
        return self.alamat
     
f = student ("Titania Emaniar", 21, "Perempuan", "Mahasiswa","UPI", "Bogor")
print ("Nama        :", f.full_name)
print ("Umur        :", f.get_age())
print ("Gender      :", f.get_gender()) 
print ("Status      :", f.get_status())
print ("Universitas :", f.get_universitas())
print ("Alamat Asal :", f.get_alamat())
