"""
This module creates a visualizer for sorting algorithms
"""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

AMOUNT = 30 # how many nums are generated
PAUSE = 100 # how long matplotlib waits before moving again

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

# Bubble sort
# Bubbles items up to where they need to be in list, stable, in-place
# Time complexity : best O(n), avg O(n^2), worst O(n^2)
# Space complexity : O(1)
def bubble(bars, nums):
    for i in range(AMOUNT):
        for j in range(0, AMOUNT-i-1):
            for bar, height in zip(bars, nums):
                bar.set_height(height)
                bar.set_color('blue')
            bars[j].set_color('red')
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
            yield nums

# Selection sort
# Selects minimum item from unsorted part and puts the smallest element in first unsorted spot, which is then part of sorted, not stable, in-place
# Time complexity : best O(n^2), avg O(n^2), worst O(n^2)
# Space complexity : O(1)
def selection(bars, nums):
    for i in range(AMOUNT):
        min_val = i
        for bar, height in zip(bars, nums):
            bar.set_height(height)
            bar.set_color('blue')
        bars[i].set_color('red')
        for j in range(i+1, AMOUNT):
            if nums[j] < nums[min_val]:
                min_val = j
        nums[i], nums[min_val] = nums[min_val], nums[i]
        yield nums

# Insertion sort
# Moves down the list and moves all larger items down one, then puts item in first item mvoed spot, stable, in-place
# Time complexity : best O(n), avg O(n^2), worst O(n^2)
# Space complexity : O(1)
def insertion(bars, nums):
    for i in range(1, AMOUNT):
        for bar, height in zip(bars, nums):
            bar.set_height(height)
            bar.set_color('blue')
        bars[i].set_color('red')
        val = i
        j = i -1
        while j >= 0 and val < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = val
        yield nums

def update_bubble(frame):
    for bar, height in zip(bars_bubble, frame):
        bar.set_height(height)
    return bars_bubble

def update_selection(frame):
    for bar, height in zip(bars_selection, frame):
        bar.set_height(height)
    return bars_selection

def update_insertion(frame):
    for bar, height in zip(bars_insertion, frame):
        bar.set_height(height)
    return bars_insertion

fig, ax = plt.subplots(2, 3, figsize=(12, 8))

# bars_quick = plt.bar(np.arange(AMOUNT), nums_quick, color='blue', width = 0.6)
# bars_merge = plt.bar(np.arange(AMOUNT), nums_merge, color='blue', width = 0.6)

ax[0,0].set_title('Bubble Sort')
ax[0,0].set_xlabel('Index')
ax[0,0].set_ylabel('Value')
bars_bubble = ax[0,0].bar(np.arange(AMOUNT), nums_bubble, color='blue', width = 0.6)

ax[0,1].set_title('Selection Sort')
ax[0,1].set_xlabel('Index')
ax[0,1].set_ylabel('Value')
bars_selection = ax[0,1].bar(np.arange(AMOUNT), nums_selection, color='blue', width = 0.6)

ax[0,2].set_title('Insertion Sort')
ax[0,2].set_xlabel('Index')
ax[0,2].set_ylabel('Value')
bars_insertion = ax[0,2].bar(np.arange(AMOUNT), nums_insertion, color='blue', width = 0.6)

bubble_gen = bubble(bars_bubble, nums_bubble)
selection_gen = selection(bars_selection, nums_selection)
insertion_gen = insertion(bars_insertion, nums_insertion)

ani_bubble = FuncAnimation(fig, update_bubble, frames=bubble(bars_bubble, nums_bubble), repeat=False, interval=PAUSE, blit=True, cache_frame_data=False)
ani_selection = FuncAnimation(fig, update_selection, frames=selection(bars_selection, nums_selection), repeat=False, interval=PAUSE, blit=True, cache_frame_data=False)
ani_insertion = FuncAnimation(fig, update_insertion, frames=insertion(bars_insertion, nums_insertion), repeat=False, interval=PAUSE, blit=True, cache_frame_data=False)

fig.suptitle('Sorting Algorithms Visualizer', fontsize=16)

plt.show()



# Merge sort
# Bubbles items up to where they need to be in list, stable, in-place
# Time complexity : best O(n), avg O(n^2), worst O(n^2)
# Space complexity : O(1)

# Quick sort
# Bubbles items up to where they need to be in list, stable, in-place
# Time complexity : best O(n), avg O(n^2), worst O(n^2)
# Space complexity : O(1)

# Heap sort
# Bubbles items up to where they need to be in list, stable, in-place
# Time complexity : best O(n), avg O(n^2), worst O(n^2)
# Space complexity : O(1)
