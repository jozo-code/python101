# s = "()(()()"

# s.count("(")
# s.count(")")
# print(s.find("("))
# k = s.count("(")-s.count(")")




# # if k <0:


# # if k >0:

# # if k=0:


# nums = [1,2,3,5,7,8,9]
# an_lst =[]
# cnt_lst=[]
# def solution(nums):
#     a0 = nums[0]
#     for i in nums:
#         d = nums[i+1]-a0
#         an = list(range(a0,max(nums),d))
#         an_lst.append(list(set(an)&set(nums)))
#     for j in an_lst:
#         cnt_lst.append(len(an_lst[j]))
#     answer = max(cnt_lst)

    

#     m = 2
#     for n in range(1,(len(nums) + 1 )):
#         an = (nums[2]-nums[1])*(n-1) + nums[0] 

#         if an != nums[n - 1 ]:
#             break
        
#         m += 1
    
#     return m



nums = [1,2,3,5,7,8,9]
an_lst =[]
cnt_lst=[]

a0 = nums[0]
d = nums[1]-a0
an = list(range(a0,max(nums)+1,d))
print(an)
an_lst.append(list(set(an)&set(nums)))
print(an_lst)
# for j in an_lst:
#     cnt_lst.append(len(an_lst[j]))
# answer = max(cnt_lst)
# print(answer)