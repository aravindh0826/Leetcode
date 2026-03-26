class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        for i in range(len(boxTypes)):
            for j in range(i+1, len(boxTypes)):
                if boxTypes[i][1] < boxTypes[j][1]:
                    boxTypes[i], boxTypes[j] = boxTypes[j], boxTypes[i]
        i = 0
        totalunits = 0
        while truckSize > 0 and i < len(boxTypes):
            boxes=boxTypes[i][0]
            units=boxTypes[i][1]
            take=min(boxes, truckSize)
            totalunits+=take*units
            truckSize-=take
            i+=1
        return totalunits