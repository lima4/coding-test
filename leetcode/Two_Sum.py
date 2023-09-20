class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, value in enumerate(nums):
            rest = target - value # idx에 해당하는 값을 뺀 나머지가 In을 통해서 List에 존재하는지 확인하는 방법

            if rest in nums[idx+1:]:
                return [idx, nums[idx+1:].index(rest) + (idx + 1)] # 똑같은 숫자는 가장 빠른 숫자의 Index가 Return

            else:
                continue  

"""
else: 
    continue
    
위의 else구문은 잘못된 코드이다. 만약 해당 하는 닶이 없을 경우에는 [], None값을 Return했어야 했다. 

다른 풀이 방법으로는

def twoSum(nums: list[int], target: int) -> list[int]: 
    numMap = {} # Dictionary를 먼저 설정하고
    n = len(nums) # nums list의 길이를 설정한다.

    # Build the hash table
    for i in range(n):  
        numMap[nums[i]] = i # Dictionary에 key, value값으로 저장하고 

    # Find the complement
    for i in range(n): 
        complement = target - nums[i] # nums list의 길이를 기준으로 For문을 돌며 Target에서 값을 뺀다.
        if complement in numMap and numMap[complement] != i: # 만약 뺀 값이 Dictionary안에 있고 만약 그 값이 Idx와 같지 않다면 출력하는 방식인데 이는 만약 num_list가 [3,3], Target이 6이라면 똑같은 0,0을 Return하기 때문이다.
            return [i, numMap[complement]]

    return []  # No solution found


"""