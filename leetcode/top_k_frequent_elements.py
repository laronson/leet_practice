'''
Question:
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Link: 
https://leetcode.com/problems/top-k-frequent-elements/description/


'''

from typing import List


def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    countDict = {}
    #Because we are instantiating a list of lists, this does not work because using this instantiation strategy makes 
    # a shallow copy of the array so if you add to the array at any index, all indexs will also change
    #freqArray = [[]] * (len(nums) + 1)

    #We must create an array like this so we create a new instance of an array at every index
    freqArray = [[] for i in range(len(nums) + 1)]

    for n in nums:
        countDict[n] = countDict.get(n,0) + 1

    # unpack every item in the dictionary in this for loop 
    for number,count in countDict.items():
        freqArray[count].append(number)

    print(freqArray)

    kthFrequentItems = []
    for i in range(len(freqArray) - 1, 0, -1):
        for n in freqArray[i]:
            kthFrequentItems.append(n)
            if len(kthFrequentItems) == k:
                return kthFrequentItems

    return

