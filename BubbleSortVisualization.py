import matplotlib.pyplot as plt
import numpy as np
import random
from matplotlib.animation import FuncAnimation

List = [random.randrange(0, 10) for _ in range(20)]

def BubbleSort(list):
    length = len(list)
    for j in range(length - 1):
        flag = False
        for i in range(length - j - 1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                flag = True
                yield list
        if not flag:
            break

def update_graph(frame, list, bar_rects):
    for rect, val in zip(bar_rects, frame):
        rect.set_height(val)
    return bar_rects

def PrintGraph(list):
    categories = [str(i) for i in range(len(list))]
    values = np.array(list)

    fig, ax = plt.subplots()
    bar_rects = ax.bar(categories, values, color='Green', edgecolor='black')

    ax.set_title('Bubble Sort Visualization')
    ax.set_xlabel('Categories')
    ax.set_ylabel('Values')

    ani = FuncAnimation(fig, update_graph, frames=BubbleSort(list), fargs=(list, bar_rects), repeat=False, save_count=len(list)*len(list))
    plt.show()

PrintGraph(List)
