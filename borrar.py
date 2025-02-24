import matplotlib.pyplot as plt

dicc= {
    "ninos": 10,
    "ninas": 15
}

plt.pie(dicc.values())
plt.title("cant ninos vs cant ninas")
plt.legend(dicc.keys())
plt.show()





# import pandas as pd
# lista =[
#     {
#         "lugar": "Comunidad",
#         "ninos": 15,
#         "ninas": 10,
#         "adolescentes": 45,
#         "adultos": 100
#     },
#     {
#         "lugar": "Comunidad",
#         "ninos": 20,
#         "ninas": 16,
#         "adolescentes": 56,
#         "adultos": 127
#     }
# ]

# df = pd.DataFrame(lista)
# rdd = df.groupby("lugar").mean()

# rdd.plot(kind="bar")
# plt.show()


# import pandas as pd
# import matplotlib.pyplot as plt


# filtered_list = []

# for i in range(len(data)):
#     for j in data[i]["menu"]:
#         if data[i].get("menu") is not None:  
#             if j["type"] == "appetizer":
#                 filtered_list.append(
#                     {
#                         "municipality": data[i]["municipe"], 
#                         "price": j["price"]
#                     }
#                 )


# data_frame = pd.DataFrame(filtered_list)  


# grouped_data = data_frame.groupby("municipality")["price"].mean()  

# grouped_data.plot(kind="barh", color="pink")  
# plt.xlabel("Promrdio de precios")  
# plt.ylabel("Municipios")  
# plt.title("Promedio de precios de los entrantes por municipios ")  
# plt.show()