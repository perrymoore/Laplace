import sympy as sym
import matplotlib.pyplot as plt
from sympy.abc import s, t
import numpy as np

# Testing Laplace Output
y1 = sym.sin(t)
Y1 = sym.laplace_transform(y1, t, s)

print('Your equation in the frequency domain is: ' + str(Y1[0]))

# Inversing and plotting
y2 = sym.inverse_laplace_transform(Y1[0], s, t)

# Gives a 'Heaviside(t)' at the end; print(y2)
char_holder = str(y2)

# Removing Heaviside(t)
no_heaviside = ''
for i in range(len(char_holder)):
    if char_holder[i + 1] != 'H':
        no_heaviside += char_holder[i]
    else:
        break
print('Your equation in the time domain is: ' + no_heaviside)

# Plotting
time = np.linspace(0, 8, 100)
filler_array = np.zeros(len(time))

for y in [y2]:
    for i in range(len(time)):
        filler_array[i] += y.subs(t, time[i])

plt.figure()
plt.plot(time, filler_array, label='y(t)')
plt.legend()
plt.xlabel('Time')
plt.ylabel('f(t)')
plt.show()
