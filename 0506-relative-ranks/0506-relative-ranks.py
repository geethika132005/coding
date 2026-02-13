class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_scores = sorted(score, reverse=True)
        rank_dict = {}
        for i in range(len(sorted_scores)):
            rank_dict[sorted_scores[i]] = i + 1
        result = []
        for s in score:
             r = rank_dict[s]
             if r == 1:
                result.append("Gold Medal")
             elif r == 2:
                result.append("Silver Medal")
             elif r == 3:
                result.append("Bronze Medal")
             else:
                result.append(str(r))
        return result
               
               
        