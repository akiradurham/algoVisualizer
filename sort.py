"""
This module creates a visualizer for sorting algorithms
"""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

AMOUNT = 30 # how many nums are generated
PAUSE = 100 # how long matplotlib waits before moving again

nums_bubble = np.arange(1, AMOUNT + 1)
nums_insertion = np.arange(1, AMOUNT + 1)
nums_selection = np.arange(1, AMOUNT + 1)
nums_heap = np.arange(1, AMOUNT + 1)
nums_quick = np.arange(1, AMOUNT + 1)
nums_merge = np.arange(1, AMOUNT + 1)

np.random.shuffle(nums_bubble)
np.random.shuffle(nums_insertion)
np.random.shuffle(nums_selection)
np.random.shuffle(nums_quick)
np.random.shuffle(nums_heap)
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
        
# Heap sort
# Builds a max heap, remove largest element (root), and build new list, repeat until done - in-place, not stable
# Time complexity : best O(nlogn), avg O(nlogn), worst O(nlogn)
# Space complexity : O(1)
def heapify(bars, nums, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and nums[left] > nums[largest]:
        largest = left

    if right < n and nums[right] > nums[largest]:
        largest = right
        
    for bar, height in zip(bars, nums):
        bar.set_height(height)
        bar.set_color('blue')
    bars[i].set_color('red')
    if left < n:
        bars[left].set_color('orange')
    if right < n:
        bars[right].set_color('yellow')

    if largest != i:
        nums[i], nums[largest] = nums[largest], nums[i]
        heapify(bars, nums, n, largest)

def heap(bars, nums):
    nums = np.copy(nums)
    n = len(nums)

    for i in range(n // 2 - 1, -1, -1):
        heapify(bars, nums, n, i)

    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(bars, nums, i, 0)
        yield np.copy(nums)
        
# (Hoare's) Quick sort
# Uses two pointers and if the left is bigger than right, swaps the two and continues
# Time complexity : best O(nlogn), avg O(nlogn), worst O(n^2)
# Space complexity : O(logn), potentially O(n) worst case
def hoare_partition(nums, low, high):
    pivot = nums[low]
    i = low - 1
    j = high + 1
    while True:
        while True:
            i += 1
            if nums[i] >= pivot:
                break
        while True:
            j -= 1
            if nums[j] <= pivot:
                break
        if i >= j:
            return j
        nums[i], nums[j] = nums[j], nums[i]
        
        for bar, height in zip(bars_quick, nums):
            bar.set_height(height)
            bar.set_color('blue')
        bars_quick[low].set_color('black')
        bars_quick[i].set_color('red')
        bars_quick[j].set_color('red')

def quick(bars, nums, low, high):
    if low < high:
        p = hoare_partition(nums, low, high)
        yield nums
        yield from quick(bars, nums, low, p)
        yield from quick(bars, nums, p + 1, high)

# Update functions to help with the animation
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

def update_heap(frame):
    for bar, height in zip(bars_heap, frame):
        bar.set_height(height)
    return bars_heap

def update_quick(frame):
    for bar, height in zip(bars_quick, frame):
        bar.set_height(height)
    return bars_quick

# setting up the graphs and titles
fig, ax = plt.subplots(2, 3, figsize=(12, 8))

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

ax[1, 0].set_title('Heap Sort')
ax[1, 0].set_xlabel('Index')
ax[1, 0].set_ylabel('Value')
bars_heap = ax[1, 0].bar(np.arange(AMOUNT), nums_heap, color='blue', width=0.6)

ax[1, 1].set_title('Hoare\'s Quick Sort')
ax[1, 1].set_xlabel('Index')
ax[1, 1].set_ylabel('Value')
bars_quick = ax[1, 1].bar(np.arange(AMOUNT), nums_quick, color='blue', width=0.6)

# calculating the amount of frames each animation needs
bubble_gen = bubble(bars_bubble, nums_bubble)
selection_gen = selection(bars_selection, nums_selection)
insertion_gen = insertion(bars_insertion, nums_insertion)
heap_gen = heap(bars_heap, nums_heap)
quick_gen = quick(bars_quick, nums_quick, 0, len(nums_quick) - 1)

# running the animations with given frames and information
ani_bubble = FuncAnimation(fig, update_bubble, frames=bubble(bars_bubble, nums_bubble), repeat=False, interval=PAUSE, blit=True, cache_frame_data=False)
ani_selection = FuncAnimation(fig, update_selection, frames=selection(bars_selection, nums_selection), repeat=False, interval=PAUSE, blit=True, cache_frame_data=False)
ani_insertion = FuncAnimation(fig, update_insertion, frames=insertion(bars_insertion, nums_insertion), repeat=False, interval=PAUSE, blit=True, cache_frame_data=False)
ani_heap = FuncAnimation(fig, update_heap, frames=heap(bars_heap, nums_heap), repeat=False, interval=PAUSE, blit=True, cache_frame_data=False)
ani_quick = FuncAnimation(fig, update_quick, frames=quick(bars_quick, nums_quick, 0, len(nums_quick) - 1), repeat=False, interval=PAUSE, blit=True, cache_frame_data=False)
ani_merge = FuncAnimation(fig, update_insertion, frames=insertion(bars_insertion, nums_insertion), repeat=False, interval=PAUSE, blit=True, cache_frame_data=False)


fig.suptitle('Sorting Algorithms Visualizer', fontsize=16)

plt.show()



# Merge sort
# Bubbles items up to where they need to be in list, stable, in-place
# Time complexity : best O(n), avg O(n^2), worst O(n^2)
# Space complexity : O(1)

# Heap sort
# Bubbles items up to where they need to be in list, stable, in-place
# Time complexity : best O(n), avg O(n^2), worst O(n^2)
# Space complexity : O(1)
