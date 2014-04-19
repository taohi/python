#!/usr/bin/python
#encoding=utf-8

def selection_sort(seq):
    for i in range(len(seq)-1,0,-1):
        max_j=i
        for j in range(max_j):
            if seq[j]>seq[max_j]:
                max_j=j
                seq[i],seq[max_j]=seq[max_j],seq[i]
            #print seq
    return seq

def test_selection_sort():
    seq=[3,5,2,4,8,1]#,0,3,5,6,2]
    assert(selection_sort(seq)==sorted(seq))
    print("Test passed!")

if __name__=="__main__":
    test_selection_sort()
