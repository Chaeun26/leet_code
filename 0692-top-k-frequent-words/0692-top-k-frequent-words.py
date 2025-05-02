class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        '''
        words = ["i","love","leetcode","i","love","coding"]

        "i" "i" "love" "love" "coding" "leetcode"

        

        "i":-2 "love":-2 "leetcode":-1 "coding":-1

        words = ["the","day","is","sunny","the","the","the","sunny","is","is"]

        the 4 day 1 is 3 sunny 2

        heap = [(-4, "the"), (-1, "day"), (-3, "is"), (-2, "sunny")]

        dict freq : {list of words}
        10 : [] 9: [] ... 1:[]
        4 : ["the"] 3 : ["is"] 2 : ["sunny"] 1: ["day"]
        '''

        cnt = Counter(words)
        heap = [(-freq, word) for word, freq in cnt.items()]
        heapify(heap)

        return [heapq.heappop(heap)[1] for i in range(k)]