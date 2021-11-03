import requests   # import humai allowance dyta hai request ko use krna ko is ka andar ka sara cheezu ko
import json   #import allows us to use the things which comes under it.
get_link=requests.get("https://api.merakilearn.org/courses")  #request.get() is one of the method of http in request to fetch a data.
course_url=get_link.json()    # to convert link data into json i stored it in a var named course_url.

with open("topic_mearaki.json","w") as file: # i create a new file here for storing a link's data in a write mode.
    json.dump(course_url,file,indent=4)  # Then i dumped link data in my file above.

sr_no=1          # initialize kamliye eak varaible liye hai.
for i in course_url:  # maina eak loop chalaya jis mai maina  get_link.json() ko store kiye tha.
    print(sr_no,i["name"],i["id"])  # print kiye name or id ko ans sr_no ko jo upr initialize kiye hai. for giving sr no. to  the data.
    sr_no+=1     # increment diye hai uppr initialize ko.

course=int(input("Enter your id you want: "))  # this is input for id , ehich course you want to choose.


print(course_url[course-1]["name"])   #course_url[course-1]["name"] jo user choose kra ga usay pura data sa minus kra ga doubra na aana ka liye.
identity=course_url[course-1]["id"]   # yah id ka liye hai jo id user choose kra usay minus kra ga pura data sa.


topic_link=requests.get("https://api.merakilearn.org/courses/"+str(identity)+"/exercises")  # from this link i get the parent child data.i stored it in a variable namely topic_link. request.get ()is the method of http method.
topic_url=topic_link.json()   # i converted above links data into  json.
with open("parent_data.json","w") as file1:  # i create a file named parent_data.json in a write mode then i dump all data in a file.
    x=json.dump(topic_url,file1,indent=4)  # dump kiye hai data file mai.
    # print(x)       # check kra k data ayia hai k nhi. print(x) use kiye hai esliye.
    srno2=1        # foe giving serial number
    list1=[]   # empty list liye hai null data append krna ka liye name.
    list2=[]    # empty list liye hai  content append krna ka liye.
for j in topic_url["course"]["exercises"]: # for loop chala hai jis mai linkka data ko convert kiye hai json mai.topic_url ka cousre or exercises ka liye.
    if j["parent_exercise_id"]==None:   # None is a keyword in python used to define a null value .none  is a data type of its own.
        print( srno2,j["name"])      
        print("  ","1.",j["slug"])
        srno2+=1
        new_no=1
        list1.append(j)
        list2.append(j)
        continue
    if j["parent_exercise_id"]==j["id"]:  #if parent_exercise_id is equal to id then it will print srno2  and name of the id.
        print(srno2,j["name"])
        srno2+=1
        new_no=1
        list1.append(j)
    for  k in topic_url["course"]["exercises"]: # loop topic_url pa chalahai jis mai maina link ka data convert krna ka liye json mai dala hai.
        if j["parent_exercise_id"]!=j["id"]:  #when parent_exercise_id != id then print new_no is srno for its child and name of the id.
            print(" ",new_no,j["name"])
            new_no+=1    #  increment for srno of child
            list2.append(j)   # above i take a empty list named list2 then i append the j in it ,j is the datafrom the parent_data file .
            break
# print(list1)
with open("child.json","w") as f:
    json.dump(list1,f,indent=4)
    parent_user=int(input("enter which parent topic you want. "))
for l in list1:
    if l["parent_exercise_id"]==l["id"]:
        print(list1[parent_user-1]["name"])
        parent_id=list1[parent_user-1]["id"]
        break
list3=[]
list4=[]
newno2=1
for m in list2:
    if m["parent_exercise_id"]==parent_id:
        print(" ",newno2,m["name"])
        list3.append(m["name"])
        list4.append(m["content"])
        newno2+=1
child_user=int(input("enter you child topic: "))
new_no3=1
for n in range(len(list3)):
    if child_user==new_no3:
        print(list3[n])
        print(list4[n])
        new_no3+=1
        break
