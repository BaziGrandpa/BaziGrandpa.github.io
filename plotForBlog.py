import numpy as np
import matplotlib.pyplot as plt

# Function definition
def f(x):
    return x**2

# Gradient of the function
def grad_f(x):
    return 2 * x

# Parameters
x_start = 2.3  # Initial value of x
learning_rate = 0.8  # Learning rate
iterations = 3  # Number of gradient descent updates

# Lists to store the x values and corresponding f(x) values
x_values = [x_start]
y_values = [f(x_start)]

# Gradient descent loop
x = x_start
for _ in range(iterations):
    x = x - learning_rate * grad_f(x)
    x_values.append(x)
    y_values.append(f(x))

# Plot the function
x_plot = np.linspace(-3, 3, 500)
y_plot = f(x_plot)
plt.plot(x_plot, y_plot, label='f(x) = x^2', color='blue')

# Plot the points from the optimization process
plt.scatter(x_values, y_values, color='red', label='Gradient Descent Points')
for i, (x, y) in enumerate(zip(x_values, y_values)):
    plt.text(x, y, f'x {i}', fontsize=8, color='black')

# Add labels and legend
plt.title('Gradient Descent on f(x) = x^2')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.legend()
plt.grid()

# Show the plot
plt.show()
