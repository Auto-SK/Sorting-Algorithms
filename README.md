# 十大经典排序算法

| 排序算法 | 平均            | 最好     | 最坏     | 空间   | 排序方式 | 稳定性 |
| :------: | :-------------: | :------: | :------: | :----: | :------: | :----: |
| 冒泡排序 | $\Theta(n^2)$        | $\Omega(n)$​ | $O(n^2)$ | $O(1)$ | 内部     | 稳定   |
| 选择排序 | $\Theta(n^2)$        | $\Omega(n^2)$ | $O(n^2)$ | $O(1)$ | 内部     | 不稳定 |
| 插入排序 | $\Theta(n^2)$        | $\Omega(n)$ | $O(n^2)$ | $O(1)$ | 内部     | 稳定   |
| 希尔排序 | $\Theta(nlog^2n)$    | $\Omega(nlogn)$​ | $O(nlog^2n)$ | $O(1)$ | 内部 | 不稳定 |
| 归并排序 | $\Theta(nlogn)$ | $\Omega(nlogn)$ | $O(nlogn)$ | $O(n)$ | 外部 | 稳定 |
| 快速排序 | $\Theta(nlogn)$ | $\Omega(nlogn)$ | $O(n^2)$​ | $O(logn)$ | 内部 | 不稳定 |
| 堆排序 | $\Theta(nlogn)$ | $\Omega(nlogn)$ | $O(nlogn)$ | $O(1)$ | 内部 | 不稳定 |
| 计数排序 | $\Theta(n+k)$ | $\Omega(n+k)$ | $O(n+k)$ | $O(k)$ | 外部 | 稳定 |
| 桶排序 | $\Theta(n+k)$ | $\Omega(n+k)$ | $O(n^2)$ | $O(n+k)$ | 外部 | 稳定 |
| 基数排序 | $\Theta(n\times k)$ | $\Omega(n\times k)$​ | $O(n\times k)$ | $O(n+k)$ | 外部 | 稳定 |

## 排序算法分类

* 稳定性：**稳定排序算法**会让原本有相等键值的纪录维持相对次序。也就是如果一个排序算法是**稳定**的，当有两个相等键值的纪录`R`和`S`，且在原本的列表中`R`出现在`S`之前，在排序过的列表中`R`也将会是在`S`之前。
* 排序方式：内部排序算法（In-place）在排序期间不需要额外内存；外部排序算法（Out-place）在排序期间需要额外内存。

## 1 冒泡排序（Bubble Sort）

### 1.1 原理

冒泡排序是一种简单直观的排序算法。它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。这个算法的名字由来是因为越小的元素会经由交换慢慢“浮”到数列的顶端。

### 1.2 步骤

1. 比较相邻的元素，如果第一个比第二个大，就交换他们；
2. 对每一对相邻元素做同样的工作，从开始的第一对到结尾的最后一对。这步完成后，最后的元素会是最大的数；
3. 针对所有的元素重复以上两步，除了最后一个元素，直到排序完成。

### 1.3 演示

![img](https://gblobscdn.gitbook.com/assets%2F-Lm9JtwbhXVOfXyecToy%2F-Lm9KQIJAMvCgJQzErQS%2F-Lm9KRSInFt3BHoLgdXb%2FbubbleSort.gif?alt=media)

### 1.4 实现

原始版本：

```python
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
```

改进版本：

```python
def bubble_sort_pro(arr):
    for i in range(len(arr)):
        flag = False
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = True
        if not flag:
            break
    return arr
```

## 2 选择排序（Selection Sort）

### 2.1 原理

选择排序是一种简单直观的排序算法，无论什么数据进去都是 $O(n^2)$ ​的时间复杂度。所以用到它的时候，数据规模越小越好。唯一的好处可能就是不占用额外的内存空间了吧。

### 2.2 步骤

1. 首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置；
2. 再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾；
3. 重复第二步，直到所有元素均排序完成。

### 2.3 演示

![img](https://gblobscdn.gitbook.com/assets%2F-Lm9JtwbhXVOfXyecToy%2F-Lm9KQIJAMvCgJQzErQS%2F-Lm9KSObDh5VGWhPE8Wh%2FselectionSort.gif?alt=media)

### 2.4 实现

```python
def selection_sort(arr):
    for i in range(len(arr) - 1):           # 循环第 i 趟
        min_index = i                       # 记录最小数的下标
        for j in range(i + 1, len(arr)):    # j 为下标
            if arr[j] < arr[min_index]:     # 如果这个数小于记录的最小数则更新最小数的下标
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]  # 将已排序序列末尾的数和最小数交换
    return arr
```

## 3 插入排序（Insertion Sort）

### 3.1 原理

插入排序一般也被称为直接插入排序。对于少量元素的排序，它是一个有效的算法。它的基本思想是将一个记录插入到已经排好序的有序表中，从而形成一个新的有序表。在其实现过程使用双层循环，外层循环对除了第一个元素之外的所有元素进行遍历，内层循环对当前元素前面有序表进行待插入位置查找，并进行移动。

插入排序的工作方式像许多人排序一手扑克牌。开始时，我们的左手为空并且桌子上的牌面向下。然后，我们每次从桌子上拿走一张牌并将它插入左手中正确的位置。为了找到一张牌的正确位置，我们从右到左将它与已在手中的每张牌进行比较。拿在左手上的牌总是排序好的，原来这些牌是桌子上牌堆中顶部的牌。

### 3.2 步骤

1. 从第一个元素开始，该元素可以认为已经被排序；
2. 取出下一个元素，在已经排序的序列中从后向前扫描；
3. 如果该元素（已排序的）大于新元素，将该元素往右移到下一位置，重复该步骤，直到找到已排序的元素小于或者等于新元素的位置；
4. 将新元素插入到步骤 3 找到的位置的后面；
5. 重复步骤 2 到 4。

### 3.3 演示

![img](https://gblobscdn.gitbook.com/assets%2F-Lm9JtwbhXVOfXyecToy%2F-Lm9KQIJAMvCgJQzErQS%2F-Lm9KSRUSDsU1-_gwBLT%2FinsertionSort.gif?alt=media)

### 3.4 实现

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):            # 将 i 看作摸到的牌的下标
        value = arr[i]                      # 将摸到的牌储存到 value
        j = i - 1                           # 将 j 看做手里的牌的下标
        while j >= 0 and arr[j] > value:    # 如果手里的牌大于摸到的牌
            arr[j + 1] = arr[j]             # 将手里的牌往右移一个位置
            j -= 1                          # 下标 j 前移
        arr[j + 1] = value                  # 将摸到的牌插入到 j + 1 位置
    return arr
```

## 4 希尔排序

### 4.1 原理

### 4.2 步骤

### 4.3 演示

### 4.4 实现

## 5 归并排序

### 5.1 原理



### 5.2 步骤

### 5.3 演示

### 5.4 实现

## 6 快速排序

### 6.1 原理



### 6.2 步骤

### 6.3 演示

### 6.4 实现

## 7 堆排序

### 7.1 原理



### 7.2 步骤

### 7.3 演示

### 7.4 实现

## 8 桶排序

### 8.1 原理



### 8.2 步骤

### 8.3 演示

### 8.4 实现

## 9 计数排序

### 9.1 原理



### 9.2 步骤

### 9.3 演示

### 9.4 实现

## 10 基数排序

### 10.1 原理



### 10.2 步骤

### 10.3 演示

### 10.4 实现