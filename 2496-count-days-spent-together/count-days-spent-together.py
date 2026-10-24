class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str,
                          arriveBob: str, leaveBob: str) -> int:

        days = [31, 28, 31, 30, 31, 30,
                31, 31, 30, 31, 30, 31]

        def convert(date):
            month, day = map(int, date.split("-"))

            total = 0

            for i in range(month - 1):
                total += days[i]

            return total + day

        alice_start = convert(arriveAlice)
        alice_end = convert(leaveAlice)

        bob_start = convert(arriveBob)
        bob_end = convert(leaveBob)

        start = max(alice_start, bob_start)
        end = min(alice_end, bob_end)

        if start > end:
            return 0

        return end - start + 1