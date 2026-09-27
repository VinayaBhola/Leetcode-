'''#program
def binary_num(list1,item):
    low = 0
    high = len(list1)-1
    while low<=high:
        mid = (low + high)//2
        guess=list1[mid]
        if (guess==item):
            return mid
        if (guess>item):
            high = mid -1
        else :
            low = mid + 1
    return None
    
#list = [1,2,3,4,5,6,7,8,9,10]
#item = 7
print(binary_num([1,2,3,4,5,6,7,9,10],7)) '''
'''class solution(object):
    def firstbadversion(self,n):
        low=1
        high=n
        while(low==high):
            mid=(high+low)//2
            version=mid
            if isbadversion(version):
                high=mid
                return true
            else:
                low=mid+1
        return False'''
                     


