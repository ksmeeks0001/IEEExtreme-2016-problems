#Food Truck SMS problem
import math

from datetime import datetime as dt

class food_truck():

    def __init__(self):

        file = open("data.txt")
        self.coord = [] #madhu latitude
        self.long = 0 #madhu longitude
        self.radius = 0 #desired sms radius
        self.numbers = {}
        self.final = []
        self.set_info(file) #read the first 2 lines extract coords and radius
        file.readline() #skip the line with the headings
        self.customers(file)
        for phone in self.numbers.keys():
            self.final.append(phone)
        self.final.sort()
        for i in range(0,len(self.final)):
            if i < len(self.final) -1:
                       print(self.final[i] , ',',sep='',end='')
            else:
                       print(self.final[i])
                

    def set_info(self,file):
            data = file.readline()
            self.coord = data.split(',')
            self.lat = float(self.coord[0])
            self.long = float(self.coord[1])
            self.radius = float(file.readline())
            self.lat = math.radians(self.lat)
            self.long = math.radians(self.long)
            #print(self.lat,self.long,self.radius)
            
            

    def customers(self,file):
        while file:
            try:
                time = dt.strptime(file.read(16),'%m/%d/%Y %H:%M')
            except:
                break
            data = file.readline()
            data = data.split(',')
            lat = float(data[1])
            long = float(data[2])
            phone = int(data[3])
            add = self.range(lat,long)
            #print(time,lat,long,phone)
            if add:
                self.numbers[phone] = time
            else:
                self.verify(phone,time)

    def range(self,lat2,long2):
        
        lat2 = math.radians(lat2)
        long2 = math.radians(long2)
        
     
        d = 2 * 6378.137 * math.asin (math.sqrt (math.sin ((self.lat - lat2)/2)**2
                        + math.cos(self.lat) * math.cos(lat2)
                        * math.sin((self.long - long2)/2)**2))

        if d <= self.radius:
            return True
        else:
            return False

    def verify(self,phone,time):

        if phone in self.numbers.keys():
            if self.numbers[phone] < time:
                del self.numbers[phone]
        

        
madhu = food_truck()



