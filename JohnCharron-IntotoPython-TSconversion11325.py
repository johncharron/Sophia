# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 23:52:18 2025

@author: John Charron
"""

#Volume conversion program to convert between Cups, Pints, Liters, and Quarts

#Name the program and display the title and what this program will do 
def uomconversionprogram():
    print("Volume Conversion Program\nThis program will convert volumes between: Cups, Pints, Quarts, and Liters.\n")
    


    
#Verifies that the user entered input is a number 
    while True:
        try:
    
            volumeamount = float(input("Enter the amount (i.e. 1, .25, 2, etc) you want to convert from: "))
  
#If input is not a number, then displays error mesage and loops back to re-enter a number
            
            break
        except ValueError:
            print("Please enter a valid number.")
    
#Prompts user to input a unit of measure to convert from and to, and also to choose from Cups, Quarts, Liters, or Pints
    
    convertfrom = input("Enter the unit of measurement you are converting from.\nChoose from Cups, Quarts, Liters, or Pints: ")
    convertto = input("Enter the unit you are converting to (i.e., Cups, Quarts, Liters, or Pints: ")

#Creates and assigns names to handle the input

    conversion = VolumeConversion(volumeamount, convertfrom, convertto)

#Performs the conversion
    result = conversion.convert()
    
#Display the result using the input from user
    print(f"{volumeamount} {convertfrom} is equal to {result} {convertto}")

#Assigns the user input value to send for conversion 

class VolumeConversion:
    def __init__(self, volumeamount, convertfrom, convertto):
       
        self.volumeamount = volumeamount
        self.convertfrom = convertfrom.lower()
        self.convertto = convertto.lower() 
#Defines acceptable input options
    def convert(self):
        valid_units = ["cups", "quarts", "liters", "pints"]
#If valid option not input, then return error message and advise of available options        
        if self.convertfrom not in valid_units or self.convertto not in valid_units:
            print(f"Invalid option! '{self.convertfrom}' or '{self.convertto}' is not a valid option.\nPlease input a valid measurement: i.e. Cups, Liters, Quarts, or Pints.")
            return "Invalid option."
       
  
     
       
        
#Sets all the available conversions between units of measure
        if self.convertfrom == "cups" and self.convertto == "quarts":
            return CupsToQuarts(self.volumeamount).convert()
        elif self.convertfrom == "cups" and self.convertto == "liters":
            return CupsToLiters(self.volumeamount).convert()
        elif self.convertfrom == "quarts" and self.convertto == "cups":
            return QuartsToCups(self.volumeamount).convert()
        elif self.convertfrom == "liters" and self.convertto == "cups":
            return LitersToCups(self.volumeamount).convert()
        elif self.convertfrom == "cups" and self.convertto == "pints":
            return CupsToPints(self.volumeamount).convert()
        elif self.convertfrom == "pints" and self.convertto == "quarts":
            return PintsToQuarts(self.volumeamount).convert()
        elif self.convertfrom == "pints" and self.convertto == "cups":
            return PintsToCups(self.volumeamount).convert() 
        elif self.convertfrom == "pints" and self.convertto == "liters":
            return PintsToLiters(self.volumeamount).convert()
        elif self.convertfrom == "liters" and self.convertto == "pints":
            return LitersToPints(self.volumeamount).convert()
        elif self.convertfrom == "liters" and self.convertto == "quarts":
            return LitersToQuarts(self.volumeamount).convert()
        elif self.convertfrom == "quarts" and self.convertto == "pints":
            return QuartsToPints(self.volumeamount).convert()
        elif self.convertfrom == "quarts" and self.convertto == "liters":
            return QuartsToLiters(self.volumeamount).convert()
        elif self.convertfrom == "quarts" and self.convertto == "cups":
            return QuartsToCups(self.volumeamount).convert()
        elif self.convertfrom == "quarts" and self.convertto == "quarts":
            return QuartsToQuarts(self.volumeamount).convert()
        elif self.convertfrom == "cups" and self.convertto == "cups":
            return CupsToCups(self.volumeamount).convert()
#If invalid input, returns error message      
        else:
            return "This conversion option is not currently available"


#Codes the conversion for Cups to Quarts
class CupsToQuarts:
    def __init__(self, cups):
        self.cups = cups
    def convert(self):
        return self.cups * 0.25

#Codes the conversion for Cups to Liters
class CupsToLiters:
    def __init__(self, cups):
        self.cups = cups
    def convert(self):
        return self.cups * 0.236588

#Codes the conversion for Quarts to Cups
class QuartsToCups:
    def __init__(self, quarts):
        self.quarts = quarts
    def convert(self):
        return self.quarts * 4

#Codes the conversion for Liters to Cups
class LitersToCups:
    def __init__(self, liters):
        self.liters = liters
    def convert(self):
        return self.liters * 4.22675

#Codes the conversion for Cups to Pints
class CupsToPints:
    def __init__(self, cups):
        self.cups = cups
    def convert(self):
        return self.cups * 0.5

#Codes the conversion for Pints to Quarts
class PintsToQuarts:
    def __init__(self, pints):
        self.pints = pints
    def convert(self):
        return self.pints * 0.5

#Codes the conversion for Liters to Pints
class LitersToPints:
    def __init__(self, liters):
        self.liters = liters
    def convert(self):
        return self.liters * 2.11338

#Codes the conversion for Pints to Cups
class PintsToCups:
    def __init__(self, pints):
        self.pints = pints
    def convert(self):
        return self.pints * 2
#Codes the conversion for Pints to Liters 
    
class PintsToLiters:
    def __init__(self, pints):
        self.pints = pints
    def convert(self):
         # 1 Liter = 4.22675 Cups
         return self.pints * 0.473176
#Codes the conversion for Liters to Quarts     
class LitersToQuarts:
    def __init__(self, liters):
        self.liters = liters
    def convert(self):
        # 1 Liter = 4.22675 Cups
        return self.liters * 1.05669
#Codes the conversion for Quarts to Pints   
class QuartsToPints:
    def __init__(self, quarts):
        self.quarts = quarts
    def convert(self):
        # 1 Liter = 4.22675 Cups
        return self.quarts * 2
#Codes the conversion for Quarts to Liters    
class QuartsToLiters:
    def __init__(self, quarts):
        self.quarts = quarts
    def convert(self):
        # 1 Liter = 4.22675 Cups
        return self.quarts * 0.946353
#Codes the conversion for Quarts to Quarts    
class QuartsToQuarts:
    def __init__(self, quarts):
        self.quarts = quarts
    def convert(self):
        # 1 Quart = 1 Quart
        return self.quarts * 1
#Codes the conversion for Cups to Cups    
class CupsToCups:
    def __init__(self, cups):
        self.cups = cups
    def convert(self):
            # 1 cup = 1 Cups
        return self.cups * 1
#Codes the conversion for Liters to Liters       
class LitersToLiters:
    def __init__(self, liters):
        self.liters = liters
    def convert(self):
        # 1 Liter = 1 Liter
        return self.liters * 1
#Codes the conversion for Pints to Pints
class PintsToPints:
    def __init__(self, liters):
        self.liters = liters
    def convert(self):
        # 1 Liter = 4.22675 Cups
        return self.liters * 1        
        
 
    


#Runs the program

    uomconversionprogram()
