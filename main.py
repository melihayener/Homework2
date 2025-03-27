import requests

baseurl = "http://localhost:3000"

class Category:
    def __init__(self):
        self.url = f"{baseurl}/Categories"

    def get_all(self):
        response = requests.get(self.url)
        return response.json()
  
    def create(self,data):
        categories = self.get_all()

        for category in categories:
            if category["name"] == data["name"]:
                print("Bu kategori adı mevcut. Başka bir kategori adı belirieyin.")
                return   
        response = requests.post(self.url, json = data)
        return response.json()
    
    def deleteCategory(self, id):
        response = requests.delete(self.url+"/"+str(id))
        return response.json()
    
    def putCategory(self,data):
        categories = self.get_all()

        for ctgry in categories:
            if ctgry["id"] != data["id"] and ctgry["name"] == data["name"]:
                print("Bu kategori zaten mevcut.")
                return

        response = requests.put(self.url+"/"+str(data["id"]), json=data)
        return response.json()  
    
    def patchCategory(self,data):
        categories = self.get_all()

        if "name" in data:
            for ctgry in categories:
                if ctgry["id"] != id and ctgry["name"] == data["name"]:
                    print("Bu kategori adı mevcut.")
                    return

        response = requests.patch(self.url+"/"+str(data["id"]), json=data)
        return response.json() 
  
category1 = Category()
# GET DENEME
# for categories in category1.get_all():
#     print(categories)

# CREATE DENEME
# data={"name":"Calculus", "description":"İleri seviye matematik"}
# category1.create({"name":"Calculus", "description":"İleri seviye matematik"})
# Hata aldım

# DELETE DENEME
#category1.deleteCategory(3)
#for categories in category1.get_all():
#    print(categories)

# PUT YENİ BİR KATEGORİ ADI İLE DENENDİ
# data2 = {"id":"1","name":"Cybersecurity Update", "description":"Security and ethical hacking and update"}
# category1.putCategory(data2)

# PUT HATA MESAJI DENEME
# data3 = {"id":2,"name": "Cloud Computing", "description":"Var olan bir kategori adını vermeye çalışıyorum."}
# category1.putCategory(data3)
#hata mesajını aldım.


# PATCH DENEME
# data4 = {"id":2,"description":"Veri bilimi dersleri anlatılır"}
# category1.patchCategory(data4)

# PATCH HATA MESAJI DENEME
# data5 = {"id":6,"name": "Cloud Computing", "description":"Patch hata mesajı denemesi"}
# category1.patchCategory(data5)  #Hata mesajı alındı

class Courses:
    def __init__(self):
        self.url = f"{baseurl}/Courses"

    def getCourses(self):
        response = requests.get(self.url)
        return response.json()
    
    def createCourse(self,data):
        response = requests.post(self.url, json=data)
        return response.json()
    
    def deleteCourse(self,id):
        response = requests.delete(self.url+"/"+str(id))
        return response.json()
    
    def putCourse(self,data):
        response = requests.put(self.url +"/"+ str([data[id]], json=data))
        return response.json()
    
    def patchCourse(self,data):
        response = requests.patch(self.url +"/"+ str(data[id]), json=data)
        return response.json()

class Lessons:
    def __init__(self):
        self.url=f"{baseurl}/Lessons"
    
    def getStudents(self):
        response = requests.get(self.url)
        return response.json()

    def createStudent(self,data):
        students = self.getStudents()

        for student in students:
            if student["name"] == data["name"]:  # Ad kontrolü
                print("Bu isimle bir öğrenci zaten mevcut. Lütfen başka bir isim kullanın.")
                return
        
        response = requests.post(self.url, json=data)
        return response.json()
    
    def deleteStudent(self,id):
        response = requests.delete(self.url+"/"+str(id))
        return response.json()

    def putStudent(self, data):
        students = self.getStudents()

        for student in students:
            if student["id"] != data["id"] and student["name"] == data["name"]:  # Ad kontrolü
                print("Bu isimle bir öğrenci mevcut.")
                return

        response = requests.put(self.url+"/"+str(data["id"]), json=data)
        return response.json()

    def patchStudent(self, data):
        response = requests.patch(self.url+"/"+str(data["id"]), json=data)
        return response.json()

class Students:
    def __init__(self):
        self.url = f"{baseurl}/Students"

    def getStudents(self):
        response = requests.get(self.url)
        return response.json()

    def createStudent(self,data):
        students = self.getStudents()

        for student in students:
            if student["name"].lower() == data["name"].lower() and student["id"] != data["id"]:  # Ad kontrolü
                print("Bu isimle bir öğrenci zaten mevcut. Lütfen başka bir isim kullanın.")
                return
            
        response = requests.post(self.url, json=data)
        return response.json()
        
    def deleteStudent(self,id):
        response = requests.delete(self.url+"/"+str(id))
        return response.json()

    def putStudent(self, data):
        students = self.getStudents()

        for student in students:
            if student["id"] != data["id"] and student["name"].lower() == data["name"].lower():  # Ad kontrolü
                print("Bu isimle bir öğrenci mevcut.")
                return

        response = requests.put(self.url+"/"+str(data["id"]), json=student)
        return response.json()

    def patchStudent(self,data):
        students = self.getStudents()

        if "name" in students:
            for student in students:
                if student["id"] != data["id"] and student["name"].lower() == data["name"].lower():
                    print(f"'{data["name"]}'Bu öğrenci adı mevcut.")
                    return

        response = requests.patch(self.url+"/"+str(data["id"]), json=data)
        return response.json()

class Enrollments:
    def __init__(self):
        self.url = f"{baseurl}/Enrollments"

    def getEnrollments(self):
        response = requests.get(self.url)
        return response.json()

    def createEnrollment(self,data):
        response = requests.post(self.url, json=data)
        return response.json()
    
    def deleteEnrollment(self,id):
        response = requests.delete(self.url + "/" + str(id))
        return response.json()

    def putEnrollment(self, data):
        response = requests.put(self.url + "/" + str(data["id"]), json=data)
        return response.json()

    def patchEnrollment(self, data):
        response = requests.patch(self.url + "/" + str(data["id"]), json=data)
        return response.json()

class Payments:
    def __init__(self):
        self.url = f"{baseurl}/Payments"

    def getPayments(self):
        response = requests.get(self.url)
        return response.json()

    def createPayment(self,data):
        response = requests.post(self.url, json=data)
        return response.json()

    def deletePayment(self,id):
        response = requests.delete(self.url + "/" + str(id))
        return response.json()
    
    def putPayment(self, data):
        response = requests.put(self.url + "/" + str(data["id"]), json=data)
        return response.json()

    def patchPayment(self, data):
        response = requests.patch(self.url + "/" + str(data["id"]), json=data)
        return response.json()

    