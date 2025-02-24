import matplotlib.pyplot as plt
import pandas as pd

def graph_percentage_pie(dictionare, title):
    plt.pie(dictionare.values(), autopct="%1.1f%%") 
    plt.title(title)
    plt.legend(dictionare.keys())
    plt.show()

def determinatePrices(data, item_schema, schema2Search):

    fivePercent = []
    tenPercent = []

    for item in data:   
        if item.get(item_schema) is not None:
            for itemObtained in item.get(item_schema):
                if item["percentage"] == 5:
                    fivePercent.append(
                        {
                            schema2Search: itemObtained[schema2Search],
                            "price": itemObtained["price"]
                        }
                    )
                elif item["percentage"] == 10:
                    tenPercent.append(
                        {
                            schema2Search: itemObtained[schema2Search],
                            "price": itemObtained["price"]
                        }
                    )
    return fivePercent, tenPercent

def create_barplot_zero(data, itemSchema, schema2Search, title, color):
    zeroPercent = []
    
    for item in data:
            if item.get(itemSchema) is not None:
                for itemObtained in item.get(itemSchema):
                    if item["percentage"] == 0:
                        zeroPercent.append(
                            {
                                schema2Search: itemObtained[schema2Search],
                                "price": itemObtained["price"]
                            }
                        )
    zero_dataFrame = pd.DataFrame(zeroPercent)

    zeroGroup = zero_dataFrame.groupby(schema2Search)["price"].mean()

    zeroGroup.plot(kind="bar", color=color)
    plt.title(title)

def create_barplot_mean(main_data, item_schema, schema2Search, title, color):
    
    five, ten = determinatePrices(main_data, item_schema, schema2Search)

    five_df = pd.DataFrame(five)
    ten_df = pd.DataFrame(ten)

    grouped_fiveFood = five_df.groupby(schema2Search)["price"].mean()
    grouped_tenFood = ten_df.groupby(schema2Search)["price"].mean()
    grouped_tenFood.plot(kind="bar", color=color[0])
    grouped_fiveFood.plot(kind="bar", color=color[1])
    plt.xlabel(schema2Search)
    plt.ylabel("price")
    plt.title(f"Promedio de precios por {title} en restaurantes que cobran servicios del 5% ({color[1]}) y del 10% ({color[0]})")
    
def compare_service_availability(df, services):
    
    service_availability = df.groupby('municipe')[services].sum()
    service_availability.plot(kind='bar', figsize=(10, 6))
    plt.title('Disponibilidad de Servicios por Municipio')
    plt.xlabel('Municipio')
    plt.ylabel('Cantidad de Restaurantes')
    plt.xticks(rotation=75)