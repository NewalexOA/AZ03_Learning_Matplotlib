import numpy as np
import matplotlib.pyplot as plt


x_array = np.random.rand(150)
y_array = np.random.rand(150)

plt.scatter(x_array, y_array)
plt.title('Диаграммя рассеяния')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
