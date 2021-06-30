
import operator

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        scores = dict()
        for i in range(len(items)):
            ID = items[i][0]
            if ID not in scores.keys():
                scores[ID] = [items[i][1]]
            else:
                scores[ID].append(items[i][1])
        res = dict()
        for i in scores:
            end = len(scores[i])
            scores[i].sort()
            res[i] = sum(scores[i][end-5:end])//5
        print(res)
        final =[]
        for i in res:
            x = [i, res[i]]
            final.append(x)
        final = sorted(final, key=operator.itemgetter(0))
        return final