import sys
input = sys.stdin.readline
MAX = 65537

def update(start,end,node,idx,val):
    if start == end :
        seg_tree[node] += val
        return seg_tree[node]
    
    mid = (start+end)//2
    if idx <= mid:
        update(start,mid,node*2,idx,val)
    else :
        update(mid+1,end,node*2+1,idx,val)
    seg_tree[node] = seg_tree[node*2] + seg_tree[node*2+1]
    return seg_tree[node]

def query(start,end,node,val):
    if start==end : return start
    mid = (start+end)//2
    left = seg_tree[node*2]
    if left >= val :
        return query(start,mid,node*2,val)
    else :
        return query(mid+1,end,node*2+1,val-left)

n,k = map(int,input().split())
seg_tree = [0] * MAX*4
nums = [int(input()) for i in range(n)]
ans = 0

for i in range(len(nums)):
    update(0,MAX,1,nums[i],1)
    if i > k-1:
        update(0,MAX,1,nums[i-k],-1)
    if i>= k-1:
        ans += query(0,MAX,1,(k+1)//2)
print(ans)