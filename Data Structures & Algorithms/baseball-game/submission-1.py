class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for operation in operations:
            if operation == '+' and len(record) != 0:
                score_add = record[-1] + record[-2]
                record.append(score_add)
            elif operation == 'D' and len(record)!= 0:
                xtwoscore = record[-1]*2
                record.append(xtwoscore)
            elif operation == 'C' and len(record) != 0:
                record.pop()
            else:
                record.append(int(operation))
        return sum(record)
        
