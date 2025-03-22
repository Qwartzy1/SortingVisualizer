# Sorting Visualizer

import pygame
import time
import random
import sys



class visualizer():
    def __init__(self, size, delay, name):
        pygame.init()

        # Screen Info
        self.screen = pygame.display.Info()
        self.width, self.height = self.screen.current_w, self.screen.current_h
        self.delay = delay

        # List Creation
        self.size = size
        self.sort_list = [i + 1 for i in range(size)]

        # Block Appearance
        self.block_width = self.width / self.size
        self.block_height = (self.height - 155) / self.size
        self.set_height = {i + 1: self.block_height * (i + 1) for i in range(size)}

        # Statistics
        self.name = name
        self.accesses = 0
        self.comparisons = 0
        self.swaps = 0
        self.start = False
        self.font = pygame.font.SysFont("Calibri", 20)

        # Visual Initialization
        self.window = pygame.display.set_mode((self.width, self.height))
        self.display((0, 0, 0), [])
        time.sleep(3)

    def display(self, color, indexes):

        # Clear the screen
        self.window.fill((0, 0, 0))
        self.escape()

        self.draw_text(self.name,(255,255,255),20,20)
        self.draw_text("Size: " + str(self.size), (255, 255, 255), 20, 50)
        self.draw_text("Delay: " + str(self.delay*1000) + "ms", (255, 255, 255), 20, 70)
        self.draw_text("Accesses: " + str(self.accesses), (255, 255, 255), 20, 90)
        self.draw_text("Comparisons: " + str(self.comparisons), (255, 255, 255), 20, 110)
        self.draw_text("Swaps: " + str(self.swaps), (255, 255, 255), 20, 130)


        # Draw the rectangles
        for i in range(self.size):

            if i in indexes:

                pygame.draw.rect(self.window, color,
                                 (self.block_width * (i), self.height - self.set_height[self.sort_list[i]],
                                  self.block_width + 1, self.set_height[self.sort_list[i]] + 1))


            else:
                pygame.draw.rect(self.window, (255, 255, 255),
                                 (self.block_width * (i), self.height - self.set_height[self.sort_list[i]],
                                  self.block_width + 1, self.set_height[self.sort_list[i]] + 1))

        # Update the display
        pygame.display.update()
    def draw_text(self,text,col,x,y):
        txt = self.font.render(text, True, col)
        self.window.blit(txt,(x,y))

    def check(self, indexes):
        self.display((243, 59, 59), [i for i in indexes])
        self.comparisons += 1
        self.accesses += 2

    def access(self,indexes):
        self.display((243, 59, 59), [i for i in indexes])
        time.sleep(self.delay)
        self.accesses += len(indexes)

    def swap(self, index1, index2):
        if self.start:
            self.swaps += 1
            self.accesses += 2

        placeholder = self.sort_list[index1]

        self.sort_list[index1] = self.sort_list[index2]
        self.sort_list[index2] = placeholder

        self.display((59, 243, 59), [index1, index2])

    def replace(self, index, value):
        self.accesses += 1
        self.sort_list[index] = value
        self.display((59, 243, 59), [index])

    def scramble(self):

        for i in range(self.size):
            switch = random.randint(0, self.size - 1)
            self.swap(i, switch)
        pygame.draw.rect(self.window, (255, 255, 255),
                         (self.block_width * (switch), self.height - self.set_height[self.sort_list[switch]],
                          self.block_width + 1, self.set_height[self.sort_list[switch]] + 1))
        pygame.draw.rect(self.window, (255, 255, 255),
                         (self.block_width * (self.size - 1), self.height - self.set_height[self.sort_list[-1]],
                          self.block_width + 1, self.set_height[self.sort_list[-1]] + 1))
        self.start = True
        pygame.display.update()

        time.sleep(2)

    def finished(self):
        self.delay *= 2

        if self.sort_list != [i + 1 for i in range(self.size)]:
            print("NOT SORTED!!!")
            time.sleep(10)
            pygame.quit()
            sys.exit()

        self.display((255, 255, 255), ())
        for i in range(self.size):
            pygame.draw.rect(self.window, (59, 243, 59),
                             (self.block_width * (i), self.height - self.set_height[self.sort_list[i]],
                              self.block_width + 1, self.set_height[self.sort_list[i]] + 1))

            if i != self.size - 1:
                pygame.draw.rect(self.window, (243, 59, 59),
                                 (self.block_width * (i + 1), self.height - self.set_height[self.sort_list[i + 1]],
                                  self.block_width + 1, self.set_height[self.sort_list[i + 1]] + 1))
            pygame.display.update()
        time.sleep(3)
    def escape(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()


########################################################################################################################


# DIVIDER!!!!!!!!


########################################################################################################################

def bubblesort(size, delay):
    _ = visualizer(size, delay, "Bubble Sort")

    _.scramble()

    for i in range(size):
        for l in range(size - i - 1):
            _.check([l, l + 1])
            if _.sort_list[l] > _.sort_list[l + 1]:
                _.swap(l, l + 1)
    _.finished()

def cocktail(size, delay):
    _ = visualizer(size, delay, "Cocktail Shaker Sort")
    _.scramble()

    if_sort = False
    start = 0
    end = size - 1

    while (if_sort == False):

        if_sort = True

        for i in range(start, end):
            _.check([i, i + 1])
            if _.sort_list[i] > _.sort_list[i + 1]:
                _.swap(i, i + 1)
                if_sort = False
        if if_sort:
            break

        if_sort = True

        end -= 1

        for i in range(end - 1, start - 1, -1):
            _.check([i, i + 1])
            if _.sort_list[i] > _.sort_list[i + 1]:
                _.swap(i, i + 1)
                if_sort = False
        start += 1

    _.finished()

def selection_sort(size, delay):
    _ = visualizer(size, delay, "Selection Sort")
    _.scramble()

    for i in range(size - 1):
        min_idx = i

        for l in range(i + 1, size):
            _.check([min_idx, l])

            if _.sort_list[min_idx] > _.sort_list[l]:
                min_idx = l

        _.swap(i, min_idx)
    _.finished()

def insertion_sort(size, delay):
    _ = visualizer(size, delay, "Insertion Sort")
    _.scramble()

    for i in range(1, size):
        _.access([i])
        cur = _.sort_list[i]
        l = i - 1

        while l >= 0 and cur < _.sort_list[l]:
            _.check([l, l + 1])
            _.swap(l, l + 1)
            l -= 1
        if l >= 0:
            _.check([l, l + 1])

    _.finished()

def binary_insertion_sort(size,delay):
    def binary_search(low,high,cur):
        while low <= high:
            mid = (low + high)//2
            _.check([cur,mid])
            if _.sort_list[cur] == _.sort_list[mid]:
                return mid + 1

            _.check([cur, mid])
            if _.sort_list[cur] > _.sort_list[mid]:
                low = mid+1
            else:
                high = mid-1
        return low

    _ = visualizer(size,delay,"Binary Insertion Sort")
    _.scramble()

    for i in range(1,size):
        l = i - 1
        idx = binary_search(0,l,i)

        while l >= idx:
            _.swap(l,l+1)
            l -= 1

    _.finished()

def gnome_sort(size, delay):
    _ = visualizer(size,delay, "Gnome Sort")
    _.scramble()
    index = 0

    while index < size:
        if index == 0:
            index += 1

        _.check([index,index-1])
        if _.sort_list[index] >= _.sort_list[index-1]:
            index += 1
        else:
            _.swap(index,index-1)
            index -= 1

    _.finished()

def odd_even_sort(size,delay):
    _ = visualizer(size,delay, "Odd/Even Sort")
    _.scramble()

    issort = False

    while not issort:
        issort = True

        for i in range(1,size-1,2):
            _.check([i,i+1])
            if _.sort_list[i] > _.sort_list[i+1]:
                _.swap(i,i+1)
                issort = False

        for i in range(0,size-1,2):
            _.check([i,i+1])
            if _.sort_list[i] > _.sort_list[i+1]:
                _.swap(i,i+1)
                issort = False

    _.finished()

def comb_sort(size, delay):
    def getnext(gap):
        gap = (gap*10)//13
        if gap < 1:
            gap = 1
        return gap

    _ = visualizer(size,delay, "Comb Sort")
    _.scramble()
    gap = size
    swap = True

    while gap != 1 or swap == True:
        gap = getnext(gap)
        swap = False

        for i in range(size-gap):
            _.check([i,i+gap])

            if _.sort_list[i] > _.sort_list[i+gap]:
                _.swap(i,i+gap)
                swap = True
    _.finished()

def shell_sort(size,delay):
    _ = visualizer(size,delay,"Shell Sort")
    _.scramble()

    gap = size // 2

    while gap > 0:
        l = gap

        while l < size:
            i = l - gap
            while i >= 0:
                _.check([i+gap,i])
                if _.sort_list[i+gap] > _.sort_list[i]:
                    break
                else:
                    _.swap(i+gap,i)
                i -= gap
            l += 1
        gap //= 2

    _.finished()

def pancake_sort(size,delay):

    def flip(i):
        l = 0

        while l < i:
            _.swap(l,i)
            l += 1
            i -= 1

    def pancake(n):
        if n == 1:
            return

        largest = 0

        for i in range(n):
            _.check([largest,i])
            if _.sort_list[largest] < _.sort_list[i]:
                largest = i

        if largest != 0:
            flip(largest)

        flip(n-1)

        pancake(n-1)

    _ = visualizer(size,delay,"Pancake Sort")
    _.scramble()

    pancake(size)

    _.finished()

def count_sort(size,delay):
    _ = visualizer(size,delay, "Counting Sort")
    _.scramble()

    _.access([0])
    m = _.sort_list[0]

    for i in range(1,size):
        _.access([i])

        if m < _.sort_list[i]:
            m = _.sort_list[i]

    count_array = [0 for i in range(m+1)]

    for i in range(size):
        _.access([i])
        count_array[_.sort_list[i]] += 1

    cur = 0
    for i in range(m+1):
        while count_array[i] > 0:
            _.replace(cur,i)
            count_array[i] -= 1
            cur += 1

    _.finished()

def merge_sort(size, delay):
    def merge(start, array):
        if len(array) > 1:
            div = len(array) // 2

            merge(start, _.sort_list[start:start + div])
            merge(start + div, _.sort_list[start + div:start + len(array)])

            _.access([i for i in range(start,start+div)])
            left = _.sort_list[start:start + div]
            _.access([i for i in range(start+div, start+len(array))])
            right = _.sort_list[start + div:start + len(array)]

            l = r = 0
            section = []

            while l < len(left) and r < len(right):
                _.check([start + l, start + div + r])
                if left[l] > right[r]:
                    section.append(right[r])
                    r += 1
                else:
                    section.append(left[l])
                    l += 1

            while l < len(left):
                section.append(left[l])
                _.access([start + l])
                l += 1

            while r < len(right):
                section.append(right[r])
                _.access([start + div + r])
                r += 1

            for i in range(len(section)):
                _.replace(start + i, section[i])

    _ = visualizer(size, delay, "Merge Sort")
    _.scramble()

    merge(0, _.sort_list)

    _.finished()

def quick_sort(size, delay):

    def partition(array,low,high):
        _.access([high])
        pivot = array[high]
        i = low

        for l in range(low,high):
            _.check([l,high])
            if array[l] <= pivot:
                _.swap(i,l)
                i += 1

        _.swap(high,i)

        return i

    def quick(array,low,high):
        if low < high:
            par = partition(array,low,high)
            quick(array, low, par-1)
            quick(array,par+1,high)


    _ = visualizer(size,delay, "Quick Sort")
    _.scramble()

    quick(_.sort_list,0,size-1)
    _.finished()

def heap_sort(size, delay):

    def heapify(l,i):
        largest = i
        left = 2*i+1
        right = 2*i+2

        if left < l:
            _.check([largest,left])
            if _.sort_list[largest] < _.sort_list[left]:
                largest = left

        if right < l:
            _.check([largest,right])
            if _.sort_list[largest] < _.sort_list[right]:
                largest = right

        if largest != i:
            _.swap(largest,i)
            heapify(l,largest)

    _ = visualizer(size, delay, "Heap Sort")
    _.scramble()

    for i in range(size//2-1, -1, -1):
        heapify(size, i)

    for i in range(size-1, 0, -1):
        _.swap(0,i)
        heapify(i, 0)

    _.finished()

def lsd_radix_sort(size,delay):

    def count(exp):
        ans = [0 for i in range(size)]
        count = [0 for i in range(10)]

        for i in range(size):
            _.access([i])
            index = _.sort_list[i]//exp
            count[index%10] += 1

        for i in range(1,10):
            count[i] += count[i-1]

        l = size - 1

        while l >= 0:
            _.access([l])
            index = _.sort_list[l]//exp
            _.access([l])
            ans[count[index%10]-1] = _.sort_list[l]
            count[index % 10] -= 1
            l -= 1

        for i in range(size):
            _.replace(i,ans[i])

    _ = visualizer(size,delay, "LSD Radix Sort")
    _.scramble()

    _.access([0])
    m = _.sort_list[0]

    for i in range(1,size):
        _.access([i])
        m = max(m,_.sort_list[i])
    power = 1

    while m >= power:
        count(power)
        power *= 10

    _.finished()

def bitonic_sort(size,delay):

    def bitonic_compare(index1, index2, direction):
        _.check([index1,index2])
        if direction == 1:
            if _.sort_list[index1] > _.sort_list[index2]:
                _.swap(index1,index2)
        else:
            if _.sort_list[index1] < _.sort_list[index2]:
                _.swap(index1,index2)


    def bitonic_merge(low, count, direction):
        if count > 1:
            k = count//2
            for i in range(low,low + k):
                bitonic_compare(i,i+k,direction)

            bitonic_merge(low,k,direction)
            bitonic_merge(low+k,k,direction)

    def bitonic(low, count, direction):
        if count > 1:
            k = count // 2
            bitonic(low,k,1)
            bitonic(low+k,k,0)
            bitonic_merge(low,count,direction)

    _ = visualizer(size,delay,"Bitonic Sort")
    _.scramble()

    bitonic(0,size,1)

    _.finished()

def bogo_sort(size,delay):
    def shuffle():
        for i in range(size):
            switch = random.randint(0, size - 1)
            _.swap(i, switch)
    def if_sorted():
        for i in range(size-1):
            _.check([i,i+1])
            if _.sort_list[i] > _.sort_list[i+1]:
                return False
        return True

    _ = visualizer(size,delay,"Bogo Sort")
    _.scramble()

    while if_sorted() == False:
        shuffle()

    _.finished()

# I Don't Know What This Means But It Looks Cool
if __name__ == "__main__":
    bubblesort(100,0.001)
    cocktail(100,0.001)
    selection_sort(125,0.001)
    insertion_sort(125,0.001)
    binary_insertion_sort(150,0.001)
    gnome_sort(125, 0.001)
    odd_even_sort(100, 0.001)
    comb_sort(125, 0.001)
    shell_sort(200, 0.002)
    pancake_sort(100, 0.001)
    count_sort(500, 0.003)
    merge_sort(250, 0.001)
    quick_sort(300, 0.001)
    heap_sort(350,0.001)
    lsd_radix_sort(350,0.001)
    bitonic_sort(256,0.002)
    bogo_sort(5,0.05)