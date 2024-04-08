import matplotlib.pyplot as plt
import numpy as np



def onclick(event):
    print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          ('double' if event.dblclick else 'single', event.button,
           event.x, event.y, event.xdata, event.ydata))

    labels = classify(funcs, np.array([[event.xdata, event.xdata]]))
    plt.scatter(event.xdata, event.xdata, c=marker_colors[labels[0]], edgecolor='black')
    plt.draw()

fig, ax = plt.subplots()
ax.plot(np.random.rand(10))

cid = fig.canvas.mpl_connect('button_press_event', onclick)

plt.show(block=True)
