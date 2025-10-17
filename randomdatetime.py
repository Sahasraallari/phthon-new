import random
import time
def getRandomDate(sD , eD):
    print("Printing random date between" , sD ,"and" ,eD)  
    randomGenerator = random.random()
    dateFormat = '%m/%d/%Y'
    sT = time.mktime(time.strptime(sD , dateFormat))
    eT = time.mktime(time.strptime(eD , dateFormat))
    rT = sT + randomGenerator * (eT - sT)
    rD = time.strftime(dateFormat, time.localtime(rT) )
    return rD
print("rD =" ,  getRandomDate("1/1/2016" , "12/12/2018"))


  