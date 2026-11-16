class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        record = []
        for i in operations:
            if i == "+":
                a = record.pop()
                b = record.pop()
                record.append(b)
                record.append(a)
                record.append(a+b)
            elif i == "C":
                record.pop()
            elif i == "D":
                record.append(2*record[-1])
            else:
                record.append(int(i))
        return sum(record)
