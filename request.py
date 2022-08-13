import json
import requests


url= requests.get("http://saral.navgurukul.org/api/courses")
bmy_file= url.json()
with open("swari.json","w") as couses:
    json.dump(bmy_file,couses,indent=4)
    
print("serial_number...course_name ...id_number")

def request():
    serial_number= 1
    id_list= []
    for index in bmy_file["availableCourses"]:
        print(serial_number, index["name"],":", index["id"])
        id_list.append(index["id"])
        serial_number += 1

    user = int(input("enter your serial number:"))
    number=1
    url1 = requests.get("http://saral.navgurukul.org/api/courses/"+id_list[user]+"/exercises")
    file = url1.json()

    list1 = []
    for index in file["data"]:
        print(number,index["slug"])
        list1.append(index["slug"])
        number += 1

    user2 = int(input("enter the slug number:"))
    url3= requests.get("http://saral.navgurukul.org/api/courses/"+str(user)+"/exercise/getBySlug?slug=" +list1[user2])
    file1 = url3.json()
    print(file1)

    print(" you want enter \n up / next/ previous/exit =")

    index=0
    while index < len(list1):
        user3=input("enter your next step = ")
        if user3=="up":
            url3=requests.get("http://saral.navgurukul.org/api/courses/"+str(user)+"/exercise/getBySlug?slug="+list1[user2-1])
            file1=url3.json()
            print(user2-1,"content",file1["content"])
        if user3=="next":
            url3=requests.get("http://saral.navgurukul.org/api/courses/"+str(user)+"/exercise/getBySlug?slug="+list1[user2+1])
            file1=url3.json()
            print(user2+1,"content",file1["content"])
        if user3=="previous":
            url3=requests.get("http://saral.navgurukul.org/api/courses/"+str(user)+"/exercise/getBySlug?slug="+list1[user2])
            file1=url3.json()
            print(user2,"content",file1["content"])
        if user3=="exit":
            index+=1
            request()
request()



