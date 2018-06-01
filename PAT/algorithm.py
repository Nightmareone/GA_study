class Solution(object):
    # def removeElement(self, nums, val):
    #     if(nums == None or nums == []):
    #         return(0)
    #     amountLength = len(nums)
    #     have_to_move = 0
    #     for index, item in enumerate(nums):
    #         if(item == val):
    #             have_to_move += 1
    #         else:
    #             nums[index-have_to_move] = item
    #     remainLength = amountLength - have_to_move
    #     print(nums)
    #     return(remainLength)
    def removeElement(self, nums ,val):
        num_of_removed = 0
        original_length = len(nums)
        if nums == [] or nums == None: return 0
        for i,num in enumerate(nums):
            if num == val:
                num_of_removed += 1
            else:
                print(i-num_of_removed)
                nums[i-num_of_removed] = num

        print(nums)
        remain_length = original_length - num_of_removed
        return remain_length

list = [0,1,2,2,3,0,4,2]
val = 2

so = Solution()
remainNum = so.removeElement(list, val)
# print(remainNum)
