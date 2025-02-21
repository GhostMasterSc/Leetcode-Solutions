class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
       
        intervals.sort(key = lambda x: x[0])

        results = [intervals[0]]

        for i in range(1,len(intervals)):
            if results[-1][1]>=intervals[i][0]:
                if results[-1][1]<=intervals[i][1]:
                    results[-1][1]=intervals[i][1]
                else:
                    pass
            else:
                results.append(intervals[i])





        
        return results
