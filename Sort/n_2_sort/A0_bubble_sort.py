"""冒泡排序"""


class BubbleSort:
    alist = [9, 7, 4, 6, 2, 1, 8, 3, 5]

    def bubble_sort(self):
        size = len(self.alist)
        for j in range(size-1):
            for i in range(size-1-j):  # 这里 -j,不用每轮都比较n次
                if self.alist[i] > self.alist[i+1]:
                    self.alist[i], self.alist[i+1] = self.alist[i+1], self.alist[i]
            print("**:", self.alist)

        return self.alist

    def bubble_sort_2(self):
        self.alist = [9, 4, 6, 2, 7, 1, 8, 3, 5]
        size = len(self.alist)
        swap = True  # 🌟
        for j in range(size-1):
            if not swap:  # 🌟加个判断，如果又一轮没有发生数据交换，就说明已经排好序了，不用继续比较了。
                break
            swap = False
            print("compare_nums:", size-1-j)
            for i in range(size-1-j):  # 这里 -j,不用每轮都比较n次
                if self.alist[i] > self.alist[i+1]:
                    self.alist[i], self.alist[i+1] = self.alist[i+1], self.alist[i]
                    swap = True
            print("++:", self.alist)

        return self.alist

    def bubble_sort_3(self):
        self.alist = [9, 4, 6, 2, 7, 1, 8, 3, 5]
        size = len(self.alist)
        swap = True
        last_swap_index = size-1  # 🌟记录上一轮循环最后的交换位置
        swap_index = -1
        while swap:  # 这里的条件也可以变了
            if not swap:  # 加个判断，如果又一轮没有发生数据交换，就说明已经排好序了，不用继续比较了。
                break
            swap = False
            print("compare_nums:", last_swap_index)
            for i in range(last_swap_index):  # 🌟本次循环比较到记录的上一轮循环的位置处就可以了
                if self.alist[i] > self.alist[i+1]:
                    self.alist[i], self.alist[i+1] = self.alist[i+1], self.alist[i]
                    swap = True
                    swap_index = i
            last_swap_index = swap_index
            print("++:", self.alist)

        return self.alist

    """
    延伸：如何在不引入第三个中间变量的情况下，完成两个数字的交换。
        位运算
    """

    nums = [0, 0, 1, 0, 0, 1, 0, 3, 12]
    """
    例题:
    给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
    请注意 ，必须在不复制数组的情况下原地对数组进行操作。
    """
    # 练习，移动零；耗时解法：冒泡,  正确解法：双指针
    def moveZeroes_2(self, nums: list):
        n = len(nums)
        left = right = 0
        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1
        return nums

    def moveZeroes(self, nums: list):
        swap = True
        size = len(nums)
        last_swap_index = size - 1
        swap_index = -1
        for i in range(size - 1):
            if not swap:
                break
            swap = False
            for j in range(last_swap_index):  # 先判断等于0再交换会更快
                if nums[j] == 0:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    swap = True
                    swap_index = j

            last_swap_index = swap_index
        return nums

    def insert_sort(self):
        size = len(self.alist)
        for i in range(1, size):
            print(i)
            for j in range(i):
                print("j:", j)
                if self.alist[i] < self.alist[j]:
                    temp = self.alist[i]
                    for k in range(i, j, -1):
                        print("k:", k)
                        self.alist[k] = self.alist[k-1]
                    self.alist[j] = temp
            print("**:", self.alist)

        return self.alist

    def select_sort(self):
        size = len(self.alist)
        for i in range(size):
            min_index = i
            for j in range(i, size):
                if self.alist[j] < self.alist[min_index]:
                    min_index = j
            self.alist[i], self.alist[min_index] = self.alist[min_index], self.alist[i]
            print("**:", self.alist)
        return self.alist


if __name__ == '__main__':
    # print(BubbleSort().bubble_sort())
    # print(BubbleSort().bubble_sort_2())
    # print(BubbleSort().bubble_sort_3())
    print(BubbleSort().moveZeroes(BubbleSort.nums))
