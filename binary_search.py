def binarysearch(A, left_ptr, right_ptr, search_ele):
    
    mid_index = (left_ptr + right_ptr)//2

    if(left_ptr == right_ptr):
        if A[mid_index] == search_ele:
            return "Element {} found at index: {}".format(search_ele, mid_index)
        else:
            return False

    if A[mid_index] == search_ele:
        return "Element {} found at index: {}".format(search_ele, mid_index) #element found
    elif(A[mid_index] > search_ele):
        right_ptr = mid_index - 1
    elif(A[mid_index] < search_ele):
        left_ptr = mid_index + 1
    
    return binarysearch(A, left_ptr, right_ptr, search_ele)


A = [1,2,3,4,5]
search_elem = 5
ans = binarysearch(A, 0, len(A) - 1, search_elem)
print(ans)
