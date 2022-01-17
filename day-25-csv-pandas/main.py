import csv
import pandas


# with open("weather_data.csv") as file:
#     contents_list = file.readlines()

# for line in contents_list:
#     print(line)


with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures =[]
    
    for row in data:
        print(row)
        
        if row[1] != "temp":
            temperatures.append(row[1])
            
    print(temperatures)
    
