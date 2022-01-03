class Solution:
    def mincostTickets(self, days, costs):
        def get_days_ago(day, ago):
            for i in range(len(days)):
                if days[i] > days[day-1] - ago:
                    return i
        out = [0] * (len(days) + 1)
        for i in range(1, len(days) + 1):
            out[i] = min(out[i-1] + costs[0], out[get_days_ago(i,7)] + costs[1], out[get_days_ago(i,30)] + costs[2])
        return print('minimum number of dollars you need to travel every day in the given list of days :',out[-1])


a=Solution()

a.mincostTickets([1,4,6,7,8,20],[2,7,15])