my_dict = {"key1": "value1", "key2": "value1", "key3": "value1", "key4": "value3", "key5": "value2"}
check={}
for key,value in my_dict.items():
    if value not in check.values():
        check[key]=value
print(check) 