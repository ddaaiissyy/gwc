import json

question = ["Type name: ", "What's your favorite hobby: ", "What's your favorite fast food?: ", "What's a crazy talent of your?: ", "Favorite movie?: ", "DOB?: "]
keys = ['name', 'name of hobby', 'name of fast food', 'name of crazy talent', 'name of favorite movie', 'her dob']

# for k, v in question():
#  answer = input(v)
#  dict_data [keys] = answer

dict_data = {}
dict_data_list = []

for i in range(len(keys)):
    answer = input(question[i])
    dict_data[keys[i]] = answer

dict_data_list.append(dict_data)
print(dict_data)



# user_name = input("Type name: ")
# dict_data['name'] = user_name

# # print(dict_data)

# # fav_hobby = {}

# user_hobby = input("What's your favorite hobby?: ")
# dict_data['name of hobby'] = user_hobby

# # print(fav_hobby)

# # fast_food = {}

# user_food = input("What's your favorite fast food?: ")
# dict_data['name of fast food'] = user_food

# # print(fast_food)

# # crazy_talent = {}

# user_talent = input("What's a crazy talent of your?: ")
# dict_data['name of crazy talent'] = user_talent

# user_movie = input("Favorite movie?: ")
# dict_data['name of favorite movie'] = user_movie 

# user_dob = input("DOB?: ")
# dict_data['her dob'] = user_dob

f = open("data.json", "r")
olddata = json.load(f)
dict_data_list.extend(olddata)
f.close()

with open("data.json", "w+") as outfile:
    json.dump(dict_data_list, outfile,)





# print(crazy_talent)

# a = ['user_name', 'user_hobby', 'user_food', 'user_talent']
# for a in (user_name):
#     print(a)


