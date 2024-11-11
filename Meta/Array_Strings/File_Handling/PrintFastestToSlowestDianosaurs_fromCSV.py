"""


2 CSV files are provided. The first file contains statistics about various dinosaurs. The second file contains additional data.
Write a program to read in the data from files, Print the names of only the bipedal dinosaurs from fastest to slowest. Do not print any other information.
speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g)
Where g = 9.8 m/s^2 (gravitational constant)

$ cat dataset1.csv
NAME,LEG_LENGTH,DIET
Hadrosaurus,1.4,herbivore
Struthiomimus,0.72,omnivore
Velociraptor,1.8,carnivore
Triceratops,0.47,herbivore
Euoplocephalus,2.6,herbivore
Stegosaurus,1.50,herbivore
Tyrannosaurus Rex,6.5,carnivore

$ cat dataset2.csv
NAME,STRIDE_LENGTH,STANCE
Euoplocephalus,1.97,quadrupedal
Stegosaurus,1.70,quadrupedal
Tyrannosaurus Rex,4.76,bipedal
Hadrosaurus,1.3,bipedal
Deinonychus,1.11,bipedal
Struthiomimus,1.24,bipedal
Velociraptorr,2.62,bipedal

[Output]
Struthiomimus,1.91845
Velociraptorr,1.91333
Stegosaurus,0.511208
Hadrosaurus,-0.264575
Euoplocephalus,-1.22311
Tyrannosaurus Rex,-2.13651
"""

import csv
import math


def  calculate_speed(stride_length, leg_length):
    g = 9.8
    return ((stride_length/leg_length) - 1) * math.sqrt(leg_length * g)


def main():
    
    with open("dataset1.csv", "r") as file_1, open("dataset2.csv", "r") as file_2:
        reader_1 = csv.reader(file_1)
        reader_2 = csv.reader(file_2)
        
        data = {}
        for row in reader_1:
            name, leg_length, diet = row
            data[name] = {"leg_length": float(leg_length), "diet": diet}
            
        for row in reader_2:
            name, stride_length, stance = row
            if name in data:
                data[name]["stride_length"]  = float(stride_length)
                data[name]["stance"] = stance
        
        
    bipedal_dinosaurs = []   
     
    for name, dino_data in data.items():
         if dino_data["stance"] == "bipedal":
            speed = calculate_speed(dino_data["stride_length"], dino_data["leg_length"])
            
            bipedal_dinosaurs.append((name, speed))
    
    bipedal_dinosaurs.sort(key=lambda x: x[1], reverse=True)
    
    
    for name, _ in bipedal_dinosaurs:
        print(name)