import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 9.81  # Acceleration due to gravity (m/s^2)

# Initial conditions
v0 = 20  # Initial velocity (m/s)
theta = 45  # Launch angle (degrees)

# Convert angle to radians
theta_rad = np.radians(theta)

# Time of flight
t_flight = 2 * v0 * np.sin(theta_rad) / g

# Time points
t = np.linspace(0, t_flight, num=500)

# Horizontal and vertical positions as a function of time
x = v0 * np.cos(theta_rad) * t
y = v0 * np.sin(theta_rad) * t - 0.5 * g * t**2

# Plotting the trajectory
plt.figure(figsize=(10, 5))
plt.plot(x, y)
plt.title('Projectile Trajectory')
plt.xlabel('Horizontal Distance (m)')
plt.ylabel('Vertical Distance (m)')
plt.ylim(bottom=0)
plt.grid(True)
plt.show()
