class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:x[1],reverse=True)
        k=truckSize
        res=0
        print(boxTypes)
        for number,units in boxTypes:
            if not k:
                return res
            if k and number<=k:
                print(res,number,units)
                res+=number*units
                k-=number
                print(k)
            else:
                res+=k*units
                k-=k
        return res

        