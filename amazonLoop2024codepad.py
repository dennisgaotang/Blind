Hello Tang! output: String, Node value integers 

class TreeNode 

        5
        /\
        3 8
        /\ /\
        2 46 9
        
        5
        /\
        3  8
        /\  /\      left root right
         4

       
     inorder = [None,3,4,5,8, None, None] 
     
    result = []
    stack = [5, 3]
    def serialize(root):
        result = []
        cur = root
        stack = []
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            node = stack.pop()
            result.append(node)
            cur = cur.right
        return result
    
    def deserialze(inorder):
        # edge

        # base
        if not inorder or len(inorder) == 0:
            return None

        n = len(inorder)
        mid = n//2
        rootval = inorder[mid]
        newroot = TreeNode(rootval)
        newroot.left = deserialze(inorder[:mid])
        newroot.right = deserialze(inorder[mid+1:])
        return newroot
     
    
        
    deserialze: 
                         |
    in order:  [2, 3(2), 4, 5(1), 6, 8(2), 9] 
                |
    pre order: [5, 3, 2, 4, 8, 6, 9]
    
    # receiving 
    def deserialize(inorder, preorder[]):
        # edge
        if len(inorder) != len(preorder):
            raise error
            return
        # base
        if len(inorder) == 0:
            return None
        
        rootVal = preorder[0]
        mid = inorder.getIndex(rootVal)
        
        leftinorder = inorder[:mid]
        leftpreorder = preorder[1:1+mid]
        
        rightinorder = inorder[mid+1:]
        rightpreorder = preorder[mid+1:]
        
        
        root = TreeNode(rootVal)
        
        leftchild = deserialize(leftinorder, leftpreorder)
        rightchild = deserialize(rightinorder, rightpreorder)
        root.left = leftchild
        root.right = rightchild
        
        return root
        
        
        
        
        
can you see me?

// Given N sorted linked lists, and you need to merged them into a single linked list

range N, heappq

1 2 3
3 4 5
6 7 9

heap = [2,3,6]
        |cur
result = 1 
def mergeNLinedList(listOfListNodes):
    heap = []
    result = Node() # this is the dummy head
    cur = result
    
    for i for len(listOfListNodes):
        node = listOfListNodes[i]
        heap.append((node.val, node))
        
    heapq.heapify(heap)
    
    while heap:
        smallestVal, smallestNode = heapq.heappopleft(heap)
        nextNode = smallestNode.next
        cur.next = smallestNode
        cur = cur.next
        if nextNode:
            heapq.heapadd(heap, (nextNode.val, nextNode))
        
    return result.next
    
    # time complexity: N * avererage#element * logN
    
    
 // Linked List with a random pointer - 
 Node {
     next*
     data
     random*
     }
     
     
 1(points to 3) -> 2 -> 3 -> 4 -> 5
 |
 1'                2'   3'   4'   5'
 
 
 make a copy/clone of this linked list
 
 def clone(Node head):
     dic = {}
     
     
     cur = head:
     # 1. clone the list
     while cur:
         newNode = Node(cur.val)
         dic[cur] = newNode
         cur = cur.next
         
     # 2. connect the new copies
     
     cur = head
     while cur:
         newnext = dic[cur.next]
         newrandom = dic[cur.random]
         cloned = dic[cur]
         cloned.next = newnext
         cloned.random = newrandom
         cur = cur.next
         
     return dic[head]
     
space complexity: O(n)
time complexity: O(2n) = O(n)
 
 