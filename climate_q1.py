import matplotlib.pyplot as plt
        
db = open('climate.csv', mode='r')

years = []
co2 = []
temp = []

for line in db:
    a = line.strip("\n").split(",")
    years.append(a[0])
    co2.append(a[1])
    temp.append(a[2])
db.close()

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp_1.png") 
