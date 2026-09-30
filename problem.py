# arr=[1,2,3,4]
# result=[]

# for i in range(len(arr)):
#     product=1
    
#     for j in range(len(arr)):
        
#         if i != j:
#             product*=arr[j]
            
#     result.append(product)
        
# print(result)

##------------------------------------------------------------------------------

# arr=[100,4,200,1,3,2]

# longest=0

# for num in arr:
#     current=num
#     count=1
    
#     while current+1 in arr:
#         current += 1
#         count += 1
        
#     longest=max(longest,count)
    
# print(longest)

##------------------------------------------------------------------------------

# arr = [100, 4, 200, 1, 3, 2]

# arr.sort()

# longest=1
# current=1

# for i in range(1,len(arr)):
    
#     if arr[i] == arr[i-1]:
#         continue
    
#     if arr[i] == arr[i-1]+1:
#         current+=1
        
#     else:
#         current = 1
        
#     longest=max(longest,current)
    
# print(longest)
    
    
##--------------------------------------------------------------------------------------------

# def longest_consecutive(arr):
#     nums=set(arr)
#     longest=0
    
#     for num in nums:
#         if num-1 not in nums:
#             current=num
#             count=1
            
#             while current+1 in nums:
#                 current+=1
#                 count+=1
                
#             longest=max(longest,count)
            
#     return longest

# arr = [100, 4, 200, 1, 3, 2]

# print(longest_consecutive(arr))

##----------------------------------------------------------------------------------------------


print("hello world")
print("temporary changes")