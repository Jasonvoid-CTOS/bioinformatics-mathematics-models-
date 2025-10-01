import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
 

#--- formula volume of egg from oval volume equation
# where a = semi-major axis (x-axis) n
# where b = semi-minor axis (y-axis)
# where c = Polar axis (z-axis)

def Volume_of_egg(a,b,c):
    V = 4/3 * np.pi * a * b * c
    return V


#--- dictionary of egg status and volume
# values are approximated from experiment

egg_status_and_volume = {"1. raw egg" : Volume_of_egg(2.32,1.86,1.63) , 
                         "2. white vinegar" : Volume_of_egg(2.76,2.20,1.93) ,
                         "3. golden syrup" : Volume_of_egg( 2.5,2.0,1.75) ,
                            "4. water" : Volume_of_egg( 3.25,2.25,1.75) , 
                            }

# white vinegar egg +46.2% in golden syrup

#--- plot the bar chart of egg volume
plt.style.use('ggplot')
plt.figure(figsize=(10,6))

bars = plt.bar(egg_status_and_volume.keys(), egg_status_and_volume.values(), color='skyblue')

# Add labels
plt.title("Effect of Different Solutions on Egg Volume")
plt.xlabel("Egg Condition")
plt.ylabel("Volume of Egg (cm³)")

# Add value labels on top of bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5, f"{yval:.2f}", 
             ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()




