class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        if hour==12:
            hour=0
        return min(abs((minutes*6)-((hour*30)+(minutes*0.5))),abs(abs((minutes*6)-((hour*30)+(minutes*0.5)))-360))