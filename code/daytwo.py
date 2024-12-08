import sys
from solution import Solution


class DayTwo(Solution):

    def __init__(self):
        self._setup('daytwo')

    def parse_input(self):
        reports = []
        for line in self.input.split('\n'):
            reports.append([int(val) for val in line.split(' ')])
        return reports

    def part_one(self):
        reports = self.parse_input()
        safe = 0
        for report in reports:
            safe += 1 if self.is_safe(report) else 0
        return safe
    
    def is_safe(self, report):
        if report[0] > report[1] and report[1] + 3 >= report[0]:
            isAsc = False
        elif report[1] > report[0] and report[0] + 3 >= report[1]:
            isAsc = True
        else:
            return False
        for i in range(1, len(report) - 1):
            if isAsc:
                low = report[i]
                high = report[i+1]
            else:
                low = report[i+1]
                high = report[i]
            if low == high or high < low or low + 3 < high:
                return False
        return True

    def part_two(self):
        pass

DayTwo().run(sys.argv[1])
