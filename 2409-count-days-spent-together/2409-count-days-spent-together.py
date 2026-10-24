class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        start = max(arriveAlice, arriveBob)
        end = min(leaveAlice, leaveBob)

        if start > end:
            return 0

        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def days(date):
            m, d = map(int, date.split('-'))
            return sum(months[:m-1]) + d

        return days(end) - days(start) + 1