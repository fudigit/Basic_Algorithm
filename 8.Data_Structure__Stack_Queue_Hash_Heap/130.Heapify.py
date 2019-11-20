'''
sift up:
1. for every element A[i], compare A[i] and its father node, if A[i] < A[father]:
    Swap with father node(sift up)
2. After swap, compare the siftedup node with the nest father node,
    Until A[father'] > A[father]
'''

class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """
    def heapify(self, A):
        for i in range(len(A)):
            self.siftup(A, i)
        
        
    def siftup(self, A, k):
        while k != 0:
            father = (k - 1)//2 # (k-1)//2 and (k-1)//2 give the same result
            if A[k] > A[father]:
                break
            # when A[i] <= A[father]
            tmp = A[k]
            A[k] = A[father]
            A[father] = tmp
            
            k = father # track the index of A[k] after swap

# 2刷
# Heap既有结构特性(complete binary tree)，又有值特性(min heap: parent.val < child.val), 有min heap和max heap
# Heap的操作：heappush：O(logn), heappop: O(logn), heap[0]:O(1)
# heappush：插入在最下层，最左边，然后做sift up。移到合适的位置，最多需要O(树高)次操作
# heappop: 取出root，把最后一个node移到root的位置，做sift down，也最多是O(树高)次操作
#   - 如果比两个child都大，father需要和2个child里较小的那个互换，否非new father > child
# delete/remove heap 中的某个元素： 需要O(n)查找到位置，把位置用最后的node覆盖，然后把node sift up或sift down
#   - 如果用hashmap的话，查找可以O(1)
# Heap可以用array来实现，因为array的第n个点就对应二叉树中的某个位置

class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """
    def sift_up(self, A, node):
        # 对node进行sift_up，如果比爸爸小，就上移，否则停止
        while node != 0:
            father = (node - 1)//2
            if A[father] > A[node]:
                A[father], A[node] = A[node], A[father]
                node = father
            else:
                break
  
    def heapify(self, A):
        # 使用"sift_up"，是在已有heap的末端加入一个新元素，然后对新元素sift_up。所以要从左到右依次
        # 如果为当前node为最终node的A不是min heap，当前node到root的路径上的一串node是没有被排序的
        for node in range(len(A)):
            self.sift_up(A, node)
        
        return A

# sift down 解法
class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """
    def sift_down(self, A, node):
        # 从最底层的爸爸节点开始
        while node*2 + 1 < len(A):
            print(node)
            # find the son with smaller value
            smaller_son = node*2 + 1
            if node*2 + 2 < len(A):
                son2 = node*2 + 2
                if A[son2] < A[smaller_son]:
                    smaller_son = son2
            
            if A[smaller_son] < A[node]:
                A[smaller_son], A[node] = A[node], A[smaller_son]
                node = smaller_son
            else:
                break


    def heapify(self, A):
        for node in range(len(A)-1, -1, -1):
            self.sift_down(A, node)
        
        return A
