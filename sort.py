"""
This module creates a visualizer for sorting algorithms
"""
import matplotlib.pyplot as plt
import numpy as np
import threading
from matplotlib.animation import FuncAnimation

AMOUNT = 30 # how many nums are generated
PAUSE = 0.0005 # how long matplotlib waits before moving again
plt.figure(figsize=(12, 10)) # size of window

nums_bubble = np.arange(1, AMOUNT + 1)
nums_selection = np.arange(1, AMOUNT + 1)
nums_quick = np.arange(1, AMOUNT + 1)
nums_insertion = np.arange(1, AMOUNT + 1)
nums_merge = np.arange(1, AMOUNT + 1)

np.random.shuffle(nums_bubble)
np.random.shuffle(nums_selection)
np.random.shuffle(nums_quick)
np.random.shuffle(nums_insertion)
np.random.shuffle(nums_merge)

x = np.arange(0, AMOUNT, 1)
bars_bubble = plt.bar(x, nums_bubble, color='blue', width = 0.6)
bars_selection = plt.bar(x, nums_selection, color='blue', width = 0.6)
bars_quick = plt.bar(x, nums_quick, color='blue', width = 0.6)
bars_insertion = plt.bar(x, nums_insertion, color='blue', width = 0.6)
bars_merge = plt.bar(x, nums_merge, color='blue', width = 0.6)

# Bubble sort
# Bubbles items up to where they need to be in list, stable, in-place
# Time complexity : best O(n), avg O(n^2), worst O(n^2)
# Space complexity : O(1)
def bubble(bars, nums):
    for i in range(AMOUNT):
        for j in range(0, AMOUNT-i-1):
            # for bar, height in zip(bars, nums):
            #     bar.set_height(height)
            #     bar.set_color('blue')
            # bars[j].set_color('red')
            # plt.pause(PAUSE)
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
            yield nums
    # bars[j].set_color('blue')

# Selection sort
# Selects minimum item from unsorted part and puts the smallest element in first unsorted spot, which is then part of sorted, not stable, in-place
# Time complexity : best O(n^2), avg O(n^2), worst O(n^2)
# Space complexity : O(1)
def selection(bars, nums):
    for i in range(AMOUNT):
        min_val = i
        # for bar, height in zip(bars, nums):
        #     bar.set_height(height)
        #     bar.set_color('blue')
        # bars[i].set_color('red')
        for j in range(i+1, AMOUNT):
            bars[j].set_color('black')
            # plt.pause(PAUSE) 
            if nums[j] < nums[min_val]:
                min_val = j
            bars[j].set_color('blue')
        nums[i], nums[min_val] = nums[min_val], nums[i]
        yield nums
    #     plt.pause(PAUSE)
    # bars[j].set_color('blue')

def update_bubble(frame):
    for bar, height in zip(bars_bubble, frame):
        bar.set_height(height)
    return bars_bubble

def update_selection(frame):
    for bar, height in zip(bars_selection, frame):
        bar.set_height(height)
    return bars_selection

def count_frames(generator):
    count = 0
    for _ in generator:
        count += 1
    return count

frames_bubble = count_frames(bubble(bars_bubble, nums_bubble))
frames_selection = count_frames(selection(bars_selection, nums_selection))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(24, 10))

ax1.set_title('Bubble Sort')
ax1.set_xlabel('Index')
ax1.set_ylabel('Value')
bubble_gen = bubble(bars_bubble, nums_bubble)

ax2.set_title('Selection Sort')
ax2.set_xlabel('Index')
ax2.set_ylabel('Value')
selection_gen = selection(bars_selection, nums_selection)

ani_bubble = FuncAnimation(fig, update_bubble, frames=bubble_gen, repeat=False, interval=PAUSE, blit=True, save_count=frames_bubble)
ani_selection = FuncAnimation(fig, update_selection, frames=selection_gen, repeat=False, interval=PAUSE, blit=True, save_count=frames_selection)

plt.tight_layout()
plt.show()

# Bubble sort
# Bubbles items up to where they need to be in list, stable, in-place
# Time complexity : best O(n), avg O(n^2), worst O(n^2)
# Space complexity : O(1)

# Bubble sort
# Bubbles items up to where they need to be in list, stable, in-place
# Time complexity : best O(n), avg O(n^2), worst O(n^2)
# Space complexity : O(1)

# Bubble sort
# Bubbles items up to where they need to be in list, stable, in-place
# Time complexity : best O(n), avg O(n^2), worst O(n^2)
# Space complexity : O(1)
