# my_dict = {'a': 123, 'b': 2, 'c': 3}

# # เปลี่ยน Dictionary เป็น Tuple โดยใช้ฟังก์ชัน items() แล้วเก็บไว้ในลิสต์
# tuple_list = list(my_dict.items())

# # แปลงลิสต์ที่มี Tuple ไปเป็น Tuple เดี่ยว
# my_tuple = tuple(my_dict.values())
# new_data = (1000,)+my_tuple
# print(my_tuple)
# print(new_data)

# def generate_data_tuple(data, id):
#     data_tuple = tuple(data.values())
#     id += 1
#     return (id,) + data_tuple 

# data = generate_data_tuple(my_dict,1)
# print(f"data : {data}")