student_data ={
    "id1" :{
        "name":"sara",
        "class":"fifth",
        "subject":["math,english,french"]
    },
    "id2" :{
        "name":"johnny",
        "class":"fifth",
        "subject":["math,english,french"]
    },"id3" :{
        "name":"sara",
        "class":"fifth",
        "subject":["math,english,french"]
    },"id4" :{
        "name":"pierre",
        "class":"fifth",
        "subject":["math,english,french"]
    },
}

result = {}
for key , value in student_data.items():
    if value not in result.values():
        result [key] = value
print(result)