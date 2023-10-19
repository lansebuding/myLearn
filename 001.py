from typing import Optional

# ############1.
# def test(arr:list[int])->int:
#     x=0
#     l,r = 0, len(arr)-1
#     while l!=r:
#         x+=int(str(arr[l])+str(arr[r]))
#         l+=1
#         r-=1
#     if l==r:
#         x+=int(arr[1])
#     return x
# print(test([1,2,3]))

# ##############2.
# def checkTime(event1:list[str],event2:list[str])->bool:
#     return not(event1[1]<event2[0] or event1[0]>event2[1])
# print(checkTime(["01:00","02:00"],["01:20","03:00"]))

# ##############3.
# def twoSum(nums:list[int], target: int) -> list[int]:
#     l1,l2=0,len(nums)-1
#     newList=[]
#     while l1<len(nums)-1:
#         while l2>l1:
#             if nums[l1]+nums[l2]==target:
#                 newList= newList+[l1,l2]
#             l2-=1
#         l1+=1
#         l2=len(nums)-1
#     return newList
# print(twoSum([3,2,4],6))

# ##############3.---解法2
# def twoSum(nums:list[int], target: int) -> list[int]:
#     d = {}
#     for index,value in enumerate(nums):
#         if target-value not in d:
#             d[value]=index
#         else:
#             return [d[target-value],index]
# print(twoSum([3,2,4],6))

# #########4.
def getLength(s:str)->int:
    if len(s)==1:
        return 1
    strList=[s[0]]
    numberList=[]
    x=0,
    y=1
    while y<=len(s)-1:
        if x<y:
            if s[y] not in strList:
                strList.append(s[y])
                y+=1
            else:
                numberList.append(len(strList))
                strList=[]
                x+=1
        else:
            numberList.append(len(strList))
            strList=[]
            break
    return max(numberList)