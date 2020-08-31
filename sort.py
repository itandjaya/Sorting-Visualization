## sort.py

def quick_sort(arr):
    
    def recurs(i, j):

        if i >= j:       
            return;
        
        left, right =   i+1, j;
        pivot       =   arr[i];

        while left < right:

            if arr[left] <= pivot:

                yield left, arr[left];
                yield right, arr[right];

                left += 1;
            
            else:
                arr[left], arr[right]   =   arr[right], arr[left];

                yield left, arr[left];
                yield right, arr[right];
                
                right -= 1;   

        if arr[left] < pivot:
            arr[left], arr[i] = arr[i], arr[left];
            i_pivot =   left;
        
        else:
            arr[left-1], arr[i] = arr[i], arr[left-1];
            i_pivot =   left-1;
        
        yield i, arr[i];
        yield i_pivot, arr[i_pivot];

        yield from recurs(i, i_pivot-1);
        yield from recurs(i_pivot+1, j);

        return;
    
    yield from recurs(  0, len(arr)-1);

    return;


def merge_sort( arr):


    def recurs( i, j):

        if i >= j:      return;
        elif i+1 == j:

            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i];
                yield i, arr[i];
                yield j, arr[j];
            return;

        mid =   (i+j)//2;
        
        yield from recurs(i, mid-1);
        yield from recurs(mid, j);

        #print(arr[i:mid], arr[mid:j+1])
        buff    =   [];

        l, r    =   i, mid;
        for _ in range( j-i+1):
            
            if l < mid and r <=j:
                if arr[l] < arr[r]: buff.append(    (l,arr[l]));    l+=1;
                else:               buff.append(    (r,arr[r]));    r+=1;

            elif l<mid:             buff.append(    (l,arr[l]));    l+=1;
            elif r<=j:              buff.append(    (r,arr[r]));    r+=1;


        for ind in range(i, j+1):

            i_buff, v_buff  =   buff[ind-i];
            #yield   i_buff, v_buff;

            arr[ind]    =   v_buff;
            yield ind, arr[ind];

        del buff;
        return;
    
    yield from recurs(0, len(arr)-1);

    return;

def bubble_sort(    arr):

    ln_arr  =   len(arr);

    for end in range(ln_arr, 0, -1):

        for i in range(end-1):
            j = i+1;
            if arr[i] > arr[j]:     
                arr[i], arr[j] = arr[j], arr[i];
                yield i, arr[i];
                yield j, arr[j];

    
    return;


    


def insertion_sort( arr):
    pass;

def heap_sort(  arr):
    pass;


