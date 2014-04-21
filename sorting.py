#!/usr/bin/python
#encoding=utf-8

#插入排序
def insertion_sort(seq):
    for i in range(1,len(seq)):
        j=i
        while j>0 and seq[j-1]>seq[j]:
            seq[j-1],seq[j]=seq[j],seq[j-1]
            j-=1
    return seq

#递归插入排序
def insertion_sort_rec(seq,i=None):
    if i==None:i=len(seq)-1
    if i==0:return i
    insertion_sort_rec(seq,i-1)
    j=i
    while j>0 and seq[j-1]>seq[j]:
        seq[j-1],seq[j]=seq[j],seq[j-1]
        j-=1
    return seq

#选择排序
def selection_sort(seq):
    for i in range(len(seq)-1,0,-1):
        max_j=i
        for j in range(max_j):
            if seq[j]>seq[max_j]:
                max_j=j
                seq[i],seq[max_j]=seq[max_j],seq[i]
            #print seq
    return seq

#归并排序
def merge_sort(seq):
    if len(seq)<2:
        return seq
    mid = len(seq)//2
    left,right=None,None
    if seq[:mid]:
        left = merge_sort(seq[:mid])
    if seq[mid:]:
        right = merge_sort(seq[mid:])
    return merge_n(left,right)

#快速排序
def quick_sort(seq):
    if len(seq)<2:
        return seq
    mid = len(seq)//2
    pi=seq[mid]
    seq = seq[:mid]+seq[mid+1:]
    lo = [x for x in seq if x<=pi]
    hi = [x for x in seq if x>pi]
    return quick_sort(lo) + [pi] + quick_sort(hi)

#冒泡排序
def bubble_sort(seq):
    size = len(seq)-1
    #for num in range(size,0,-1):
    for i in range(len(seq)):
        for j in range(i+1,len(seq)):
            if seq[i]>seq[j]:
                seq[i],seq[j]=seq[j],seq[i]
    return seq
    
def test_sort():
    seq1=[3,5,2,6,8,1,0,3,5,6,2,5,4,1,5,3]
    seq2=[3,5,2,6,8,1,0,3,5,6,2,5,4,1,5,3]
    seq3=[3,5,2,6,8,1,0,3,5,6,2,5,4,1,5,3]
    seq4=[3,5,2,6,8,1,0,3,5,6,2,5,4,1,5,3]
    seq5=[3,5,2,6,8,1,0,3,5,6,2,5,4,1,5,3]
    seq6=[3,5,2,6,8,1,0,3,5,6,2,5,4,1,5,3]
    assert(selection_sort(seq1)==sorted(seq1))
    assert(insertion_sort(seq2)==sorted(seq2))
    assert(insertion_sort_rec(seq3)==sorted(seq3))
    assert(quick_sort(seq4)==sorted(seq4))
    assert(bubble_sort(seq5)==sorted(seq5))
    print "All sorting tests passed!"

if __name__ == "__main__":
    test_sort()
