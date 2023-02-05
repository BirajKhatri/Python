student={
    "first_name":"Ram",
    "last_name":"khatri",
    "age":21
}


print(student.get("first_name"))
print(student.get("last_name"))
print(student["age"])

# adding list into dictionary

items={
    "new_val":2,
    "value":[1,2,3,4]
}
print(items["value"])


# nested dictionary-> dictionary inside dictionary
nested_dis={
   "key2":{
    "key3":{
        "key4":"finalValue2"
    }
   }
}

print(nested_dis["key2"]["key3"]["key4"])
