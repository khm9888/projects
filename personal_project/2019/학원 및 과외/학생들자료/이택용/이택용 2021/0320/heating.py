

class Heater():
    def __init__(self,name,temperature=10.0,minimum=0.0,maximum=100.0):
        self.name=name
        self.temp=temperature   
        self.minimum=minimum
        self.maximum=maximum
    def __str__(self):
        return f"{self.name}: current temperature: {self.temp:.1f}; allowed min: {self.minimum:.1f}; allowed max: {self.maximum:.1f}"
    def __repr__(self):
        return f"Heater('{self.name}', {self.temp:.1f}, {self.minimum:.1f}, {self.maximum:.1f})"
    def change_temperature(self,temperature):
        self.temp+=temperature
        if self.temp<self.minimum:
            self.temp=self.minimum
        if self.temp>self.maximum:
            self.temp=self.maximum
            
    def temperature(self):
        return float(self.temp)
          
machine1 = Heater('radiator kitchen', temperature=20)
machine2 = Heater('radiator living', minimum=15, temperature=18)    
machine3 = Heater('radiator bathroom', temperature=22, minimum=18, maximum=28)
# v= print(machine1)
# Heater('radiator living', 18.0, 15.0, 100.0)
# machine2.change_temperature(8)
print(machine1.temperature())
# 26.0
v= machine3.change_temperature(-5)
v= machine3
# Heater('radiator bathroom', 18.0, 18.0, 28.0) 
print(v)