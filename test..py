import matplotlib.pyplot as plt, patches

figure, axes = plt.subplots()
Drawing_colored_circle = plt.Circle((0.6, 0.6), 0.2, color='green')

axes.set_aspect(1)
axes.add_artist(Drawing_colored_circle)
plt.show()
