class Node:
    def __init__(self,number):
        self.value = number
        self.lc = None
        self.rc = None
        
class Tree:
    lis = []
    
    def __init__(self):
        self.root = None
    
    def add(self,number):
        
        node = Node(number)
        
        if self.root == None:
            self.root = node
            self.lis.append(self.root)
        else:
            target_node = self.lis[0]
            if target_node.lc==None:
                target_node.lc = node
                self.lis.append(target_node.lc)
            else:
                target_node.rc = node
                self.lis.append(target_node.rc)
                del(self.lis[0])

tree = Tree()
for x in range(10):
    tree.add(x)

def preorder(node):
    if node==None:
        return None
    print(node.value)
    preorder(node.lc)
    preorder(node.rc)
def inorder(node):
    if node==None:
        return None
    inorder(node.lc)
    print(node.value)
    inorder(node.rc)
def postorder(node):
    if node==None:
        return None
    postorder(node.lc)
    postorder(node.rc)
    print(node.value)
# Preorder is simple, Inorder is hard, Postorder you need another mark number or an last_pop sentry variable.
def preorder_no_recursion(node):
    stack = []
    stack.append(node)
    while stack:
        target = stack.pop(-1)
        print(target.value)
        if target.rc!=None:
            stack.append(target.rc)
        if target.lc!=None:
            stack.append(target.lc)
def inorder_no_recursion(node):
    stack = []
    stack.append(node)
    while stack:
        target = stack[-1]
        while target.lc!=None:
            target = target.lc
            stack.append(target)
        target = stack.pop(-1)
        print(target.value)
        while target.rc==None and stack:
            target = stack.pop(-1)
            print(target.value)
        if target.rc:
            stack.append(target.rc)
def postorder_no_recursion(node):
    return None