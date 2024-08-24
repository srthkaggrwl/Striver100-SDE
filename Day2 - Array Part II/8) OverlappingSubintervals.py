class Solution(object):
    def merge(self, intervals):
       if len(intervals) == 1:
           print(intervals)
       else:   
            intervals = sorted(intervals, key=lambda x: x[0])
 
            last_merged = 0
            mergerd_intervals = []
            for i in range(len(intervals)-1):
                if intervals[i][1] >= intervals[i+1][0]:
                    mergerd_intervals.append([intervals[i][0], max(intervals[i+1][1], intervals[i][1])])
                    last_merged = i+1
            if last_merged == 0:
                print(intervals)
            else:    
                for i in range(last_merged+1, len(intervals)):
                    mergerd_intervals.append(intervals[i])

                print(mergerd_intervals)

solution = Solution()
solution.merge([[1,4],[2,3]])               
        