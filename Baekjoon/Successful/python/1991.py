# 1991
import sys
input = sys.stdin.readline
N = int(input().strip())
tree = {}
for _ in range(N) :
    node, leftchild, rightchild = map(str, input().strip().split())
    tree[node] = (leftchild, rightchild)

def preorder(c) :
    if c == '.' : return ''
    l, r = tree[c]
    return c + preorder(l) +  preorder(r)
print(preorder('A'))

def inorder(c) :
    if c == '.' : return ''
    l, r = tree[c]
    return inorder(l) + c + inorder(r)
print(inorder('A'))

def postorder(c) :
    if c == '.' : return ''
    l, r = tree[c]
    return postorder(l) + postorder(r) + c
print(postorder('A'))