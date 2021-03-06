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

算法的实现见[Sorting Algorithms](https://github.com/Auto-SK/Sorting-Algorithms)。

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

![bubbleSort](https://cdn.jsdelivr.net/gh/Auto-SK/CDN/Articles/Sorting-Algorithms/bubbleSort.gif)

### 1.4 实现

原始版本：

```python
def bubble_sort(arr):
    for i in range(len(arr)):               # 循环第 i 趟
        for j in range(len(arr) - i - 1):   # j 为下标
            if arr[j] > arr[j + 1]:         # 如果这个数大于后面的数就交换两者的位置
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
```

改进版本：

```python
def bubble_sort_pro(arr):
    for i in range(len(arr)):               # 循环第 i 趟
        flag = False                        # 每次都初始化标记
        for j in range(len(arr) - i - 1):   # 如果这个数大于后面的数就交换两者的位置
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = True                 # 有逆序就设置标记
        if not flag:                        # 标记没有变化就退出循环
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

![selectionSort](https://cdn.jsdelivr.net/gh/Auto-SK/CDN/Articles/Sorting-Algorithms/selectionSort.gif)

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

![insertionSort](https://cdn.jsdelivr.net/gh/Auto-SK/CDN/Articles/Sorting-Algorithms/insertionSort.gif)

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

## 4 希尔排序（Shell Sort）

### 4.1 原理

希尔排序，也称递减增量排序，是插入排序的一种更高效的改进版本。但希尔排序是非稳定排序算法。

希尔排序是基于插入排序的以下两点性质二提出改进方法的：

* 插入排序在对几乎已经排好序的数据操作时，效率高，即可以达到线性排序的效率；
* 但插入排序一般来说是低效的，因为插入排序每次只能将数据移动一位。

希尔排序的基本思想是：先将整个待排序的序列分割成若干子序列分别进行直接插入排序，待整个序列中的记录“基本有序”时，再对全体记录依次进行直接插入排序。

### 4.2 步骤

1. n 为数组长度，首先取一个整数 d1=n/2，将元素分为 d1 个组，每组相邻两元素之间的距离为 d1-1，在各组内进行直接插入排序；
2. 取第二个整数 d2=d1/2，重复步骤 1 分组排序过程，直到 di=1，即所有元素在同一组内进行直接插入排序。

PS：希尔排序每趟并不使某些元素有序，而是使整体数据越来越接近有序；最后一趟排序使得所有数据有序。

### 4.3 演示

![希尔排序](https://cdn.jsdelivr.net/gh/Auto-SK/CDN/Articles/Sorting-Algorithms/%E5%B8%8C%E5%B0%94%E6%8E%92%E5%BA%8F.gif)

### 4.4 实现

分开写：

```python
def insertion_sort_gap(arr, gap):           # 将 gap 看作隔 gap 个距离摸一张牌，而不是依次按顺序摸牌
    for i in range(gap, len(arr)):          # 将 i 看作摸到的牌的下标
        value = arr[i]                      # 将摸到的牌存储到 value
        j = i - gap                         # 将 j 看作手里的牌的下标
        while j >= 0 and arr[j] > value:    # 如果手里的牌大于摸到的牌
            arr[j + gap] = arr[j]           # 将手里的牌右移 gap 个距离
            j -= gap                        # 下标 j 左移 gap 个距离
        arr[j + gap] = value                # 将摸到的牌插入到 j + gap 位置


def shell_sort_part(arr):                   # 分开写 shell 排序
    d = len(arr) // 2                       # 第一次分组
    while d >= 1:
        insertion_sort_gap(arr, d)          # 调用插入排序
        d //= 2                             # 整除 2 后再次分组
    return arr
```

合到一起：

```python
def shell_sort(arr):                        # 合到一起
    gap = len(arr) // 2                     # 第一次分组
    while gap >= 1:                         # 将 gap 看作隔 gap 个距离摸一张牌，而不是依次顺序摸牌
        for i in range(gap, len(arr)):      # 将 i 看作摸到的牌的下标
            value = arr[i]                  # 将摸到的牌存储到 value
            j = i - gap                     # 将 j 看作手里的牌的下标
            while j >= 0 and arr[j] > value:
                arr[j + gap] = arr[j]       # 将手里的牌右移 gap 个距离
                j -= gap                    # 下标 j 左移 gap 个距离
            arr[j + gap] = value            # 将摸到的怕插入到 j + gap 位置
        gap //= 2                           # 整除 2 后再分组
    return arr
```

## 5 归并排序（Merge Sort）

### 5.1 原理

归并排序是记者能力在归并操作上的一种有效的排序算法。该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。

作为一种典型的分而治之思想的算法应用，归并排序的实现由两种方法：

* 自上而下的递归；
* 自下而上的迭代。

### 5.2 步骤

1. 申请空间，使其大小为两个已经排序序列之和，该空间用来存放合并后的序列；
2. 设定两个指针，最初位置分别为两个已经排序序列的起始位置；
3. 比较两个指针所指向的元素，选择相对小的元素放入到合并空间，并移动指针到下一位置；
4. 重复步骤 3 直到某一指针到达序列尾部；
5. 将另一序列剩下的所有元素直接复制到合并序列尾部。

![Picture1.png](https://cdn.jsdelivr.net/gh/Auto-SK/CDN/Articles/Sorting-Algorithms/1614274007-nBQbZZ-Picture1.png)

### 5.3 演示

![mergeSort](https://cdn.jsdelivr.net/gh/Auto-SK/CDN/Articles/Sorting-Algorithms/mergeSort.gif)

### 5.4 实现

```python
def merge_sort(arr):
    def mergesort(l, r):
        # 终止条件
        if l >= r:
            return
        # 递归划分
        m = ((r - l) >> 1) + l
        mergesort(l, m)
        mergesort(m + 1, r)
        # 合并阶段
        i, j = l, m + 1
        tmp[l: r + 1] = arr[l: r + 1]
        for k in range(l, r + 1):
            if i > m or (j <= r and tmp[i] > tmp[j]):
                arr[k] = tmp[j]
                j += 1
            else:
                arr[k] = tmp[i]
                i += 1
    tmp = [0] * len(arr)
    mergesort(0, len(arr) - 1)
    return arr
```

## 6 快速排序（Quick Sort）

### 6.1 原理

快速排序是对冒泡排序的一种改进。顾名思义快速排序就是快，而且效率高！它是处理大数据最快的排序算法之一了。它的基本思想是：通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列。

>快速排序的最坏运行情况是 $O(n^2)$，比如顺序数列的快排。但它的均摊期望时间是 $O(nlogn)$，且 $O(nlogn)$​ 记号中隐含的常数因子很小，比复杂度稳定等于 $O(nlogn)$ 的归并排序要小很多。所以，对绝大多数顺序性较弱的随机数列而言，快速排序总是优于归并排序。

### 6.2 步骤

1. 从数列中挑出一个元素，称为“基准值”;
2. 重新排序数列，所有元素比基准值小的放在基准值的左边，比基准值大的放在基准值的右边（相同的数可以到任一边）。在这个分区退出之后，该基准值就处于数列的中间位置。这个称为分区（partition）操作，也可以称为一次归位操作；
3.  递归地把小于基准值元素的子数列和大于基准值元素的子数列按照步骤 1、2 排序。

![Picture1.png](https://cdn.jsdelivr.net/gh/Auto-SK/CDN/Articles/Sorting-Algorithms/1612615552-rifQwI-Picture1.png)

### 6.3 演示

![quickSort](https://cdn.jsdelivr.net/gh/Auto-SK/CDN/Articles/Sorting-Algorithms/quickSort.gif)

### 6.4 实现

```python
def quick_sort(arr):
    def quicksort(l, r):
        # 子数组长度为 1 时终止递归
        if l >= r:
            return
        # 哨兵划分操作（以 arr[l] 作为基准数）
        i, j = l, r
        while i < j:
            while i < j and arr[j] >= arr[l]:
                j -= 1
            while i < j and arr[i] <= arr[l]:
                i += 1
            arr[i], arr[j] = arr[j], arr[i]
        arr[l], arr[i] = arr[i], arr[l]
        # 递归左（右）子数组执行哨兵划分
        quicksort(l, i - 1)
        quicksort(i + 1, r)

    quicksort(0, len(arr) - 1)
    return arr
```

## 7 堆排序（Heap Sort）

### 7.1 原理

堆排序是指利用堆这种数据结构所设计的一种排序算法。堆是一个完全二叉树，并且堆中每一个节点的值都必须大于等于或者（小于等于）其子树中每个节点的值。

* 大顶堆：每个节点的值都大于等于其子树中每个节点的值，在堆排序算法中用于升序排列；
* 小顶堆：每个节点的值都小于等于其子树中每个节点的值，在堆排序算法中用于降序排列。

![11堆排序](https://cdn.jsdelivr.net/gh/Auto-SK/CDN/Articles/Sorting-Algorithms/Heap.png)

>对于从 1 开始存储，长度为 n 的堆：数组下标为 i 的节点，其左子节点为 2 * i，右子节点为 2 * i + 1，父节点为 i / 2，最后一个非叶子节点为 n / 2；
>
>对于从 0 开始存储，长度为 n 的堆：数组下标为 i 的节点，其左子节点为 2 * i + 1，右子节点为 2 * i + 2，父节点为 (i - 1) / 2，最后一个非叶子节点为 n / 2 - 1。

### 7.2 步骤

1. 构建堆：将待排序序列构建成一个堆 Hp[0, ..., n-1]，从最后一个非叶子节点开始，从右至左、从下至上进行调整。根据升序或者降序建立大顶堆或者小顶堆；
2. 此时的堆顶元素，为最大或者最小元素；
3. 把堆顶元素和堆尾元素互换，调整堆，重新使堆有序；
4. 此时堆顶元素为第二大元素；
5. 重复步骤 2 到 4，直到堆只剩一个元素。

### 7.3 演示

![heapSort](https://cdn.jsdelivr.net/gh/Auto-SK/CDN/Articles/Sorting-Algorithms/heapSort.gif)

### 7.4 实现

```python
def build_heap(arr):
    for i in range(len(arr) // 2 - 1,  -1, -1):     # 从 n / 2 - 1 到 0 开始建堆
        heapify(arr, len(arr), i)


def heapify(arr, n, i):
    """
    :param arr: 要建堆的数组
    :param n: 堆的长度
    :param i: 要入堆的元素的索引
    :return: None
    """
    left = 2 * i + 1    # 左子节点
    right = 2 * i + 2   # 右子节点
    largest = i
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    build_heap(arr)
    for l in range(len(arr) - 1, 0, -1):    # 从 n - 1 到 1 重复堆化
        arr[0], arr[l] = arr[l], arr[0]
        heapify(arr, l, 0)
    return arr
```

## 8 桶排序（Bucket Sort）

### 8.1 原理

桶排序的核心思想是将要排序的数据分到几个有序的桶里，每个桶里的数据再单独进行排序。桶内排序完成之后，再把每个桶里的数据按照顺序依次取出，组成的序列就是有序的了。

![img](https://cdn.jsdelivr.net/gh/Auto-SK/CDN/Articles/Sorting-Algorithms/987564607b864255f81686829503abae.jpg)

假设要排序的数据有 n 个，把它们均匀地划分到 m 个桶内，每个桶里有 k=n/m 个元素。每个桶内部使用快速排序，时间复杂度为 O(k * logk)。m 个桶排序的时间复杂度就是 O(m * k * logk)，因为 k=n/m，所以整个桶排序的时间复杂度就是 O(n*log(n/m))。当桶的个数 m 接近数据个数 n 时，log(n/m) 就是一个非常小的常量，这个时候桶排序的时间复杂度接近 O(n)。

* 最好情况：当输入的数据能够均匀地分配到每个桶中，此时的时间复杂度为 O(n)；
* 最坏情况：当输入的数据都被分配到同一个桶中，此时的时间复杂度退化到 O(nlogn)。

为了使桶排序更加高效，我们需要做到这两点：

* 在额外空间充足的情况下，尽量增大桶的数量，桶排序比较适合用在外部排序中；
* 使用的映射函数能够将输入的 n 个数据均匀地分配到 m 个桶中，并且桶与桶之间有着天然的大小顺序。

### 8.2 步骤

1. 创建一个定量的数组当作空桶；
2. 遍历序列，把元素依次放到对应的桶中；
3. 对每个非空桶进行排序；
4. 依次从非空桶中将元素取出放入原来的序列中。

### 8.3 演示

![15桶排序](https://cdn.jsdelivr.net/gh/Auto-SK/CDN/Articles/Sorting-Algorithms/BucketSort.gif)

### 8.4 实现

```python
def bucket_sort(arr):
    min_val = min(arr)
    max_val = max(arr)
    res = []

    # 桶的初始化
    bucket_size = 5  # 桶的大小
    bucket_count = (max_val - min_val) // bucket_size + 1  # 桶的数量
    buckets = [[] for _ in range(bucket_count)]

    # 利用映射函数将数据分配到每个桶中
    for a in arr:
        i = (a - min_val) // bucket_size
        buckets[i].append(a)
    for bucket in buckets:
        bucket.sort()
    for bucket in buckets:
        res.extend(bucket)  # 从 list 中提取
    return res
```

## 9 计数排序（Counting Sort）

### 9.1 原理

**计数排序其实是桶排序的一种特殊情况**。当要排序的 n 个数据，所处的范围并不大的时候，比如最大值是 k，我们就可以把数据划分成 k 个桶。每个桶内的数据值都是相同的，省掉了桶内排序的时间。

计数排序的核心在于将输入的数据值转化为键存储在额外开辟的数组空间中。作为一种线性时间复杂度的排序，计数排序要求**输入的数据**必须是**有确定范围的整数**。

### 9.2 步骤

1. 找到待排序列表中的最大值 k，开辟一个长度为 k + 1 的计数列表，计数列表中的值都为 0；
2. 遍历待排序列表，如果遍历到的元素值为 i，则计数列表中索引 i 的值加1；
3. 遍历完整个待排序列表，计数列表中索引 i 的值 j 表示 i 的个数为 j，统计出待排序列表中每个值的数量；
4. 创建一个新列表（也可以清空原列表，在原列表中添加），遍历计数列表，依次在新列表中添加 j 个 i，新列表就是排好序后的列表，整个过程没有比较待排序列表中的数据大小。

### 9.3 演示

![countingSort](https://cdn.jsdelivr.net/gh/Auto-SK/CDN/Articles/Sorting-Algorithms/countingSort.gif)

### 9.4 实现

```python
def counting_sort(arr):
    if len(arr) < 2:
        return arr
    max_num = max(arr)
    count = [0 for _ in range(max_num + 1)]  # 开辟一个计数列表
    for a in arr:
        count[a] += 1
    arr.clear()
    for ind, val in enumerate(count):  # 提出计数序列的索引和值
        arr.extend([ind] * val)
    return arr
```

## 10 基数排序（Radix Sort）

### 10.1 原理

基数排序属于分配式排序，是一种**非比较型整数排序算法**，其原理是将整数按位数切割成不同的数字，然后按每个位数分别比较（**必须用稳定排序算法**）。由于整数也可以表达字符串（比如名字或日期）和特定格式的浮点数，所以基数排序也不是只能使用于整数。

基数排序、计数排序、桶排序三种排序算法都利用了桶的概念，但对桶的使用方法上是有明显差异的：

- 桶排序：每个桶存储一定范围的数值；
- 计数排序：每个桶只存储单一键值；
- 基数排序：根据键值的每位数字来分配桶。

### 10.2 步骤

1. 取数组中的最大数，并取得位数；
2. 从最低位开始，依次进行一次排序；
3. 从最低位排序一直到最高位排序完成以后, 数列就变成一个有序序列。

### 10.3 演示

![radixSort](https://cdn.jsdelivr.net/gh/Auto-SK/CDN/Articles/Sorting-Algorithms/radixSort.gif)

### 10.4 实现

```python
def radix_sort(arr):
    digit = 0       # 当前位数
    max_digit = 1   # 最大位数
    max_value = max(arr)

    # 找出序列中最大的位数
    while 10 ** max_digit < max_value:
        max_digit += 1

    while digit < max_digit:
        count = [[] for _ in range(10)]  # 开辟一个计数列表
        for a in arr:
            d = (a // 10 ** digit) % 10  # 求出 digit 位对应的值
            count[d].append(a)
        # 计数排序
        arr.clear()
        for c in count:
            arr.extend(c)
        digit += 1
    return arr
```

## 相关参考

1. [十大经典排序算法](https://sort.hust.cc/)

2. [Python 实现十大经典排序算法](https://www.itrhx.com/2020/10/23/A91-sorting-algorithm/)

3. [数据结构与算法之美](https://time.geekbang.org/column/intro/126)

4. [数据结构和算法必知必会的50个代码实现](https://github.com/wangzheng0822/algo)

5. [十大排序python实现【精讲】合集 八大排序算法必学](https://zhuanlan.zhihu.com/p/144935860)

