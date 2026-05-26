import numpy as np
import matplotlib.pyplot as plt

firstDigit = [] # empty list to put all first digits in

for _ in range (5000): # so benford's law will actually work, create correct conditions
 smth = np.random.uniform(1, 10)
 for i in range(50):
    factor = np.random.uniform(1.01,1.05) # so exponential growth won't occur
    smth = smth * factor
    firstDigit.append(int(str(int(smth))[0])) # adding the first digit of the new value to the list

firstDigit = np.array(firstDigit) # turning list into array so it can be plotted

plt.hist(firstDigit,
         bins = np.arange(1,11),
         edgecolor = "black") # plotting histogram

plt.title("Benford's Law Monte Carlo Simulation") # title
plt.xticks(range(1,11)) # shows all x axis interval
plt.show()