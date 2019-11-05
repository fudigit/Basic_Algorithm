class Solution:
    """
    @param houses: positions of houses
    @param heaters: positions of heaters
    @return: the minimum radius standard of heaters
    """
    def findRadius(self, houses, heaters):
        
        hourses = sorted(houses)
        heaters = sorted(heaters)
        
        start = min(houses[0], heaters[0])
        end = max(houses[-1], heaters[-1])
        
        while start + 1 < end:
            mid = start + (end - start)//2
            print(start, end, mid)
            if self.cover_houses(mid, houses, heaters):
                end = mid
            else:
                start = mid
        
        print(start, end)
        if self.cover_houses(start, houses, heaters):
            return start
        return end
        
    def cover_houses(self, radius, houses, heaters):
        heater_cur = 0
        for h in range(len(houses)):
            while heater_cur < len(heaters) - 1 and abs(houses[h] - heaters[heater_cur]) > radius:
                heater_cur += 1
            if abs(houses[h] - heaters[heater_cur]) > radius:
                return False
        return True
