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

    def is_safe_with_tolerance(self, report):
        if report[0] > report[1] and report[1] + 3 >= report[0]:
            isAsc = False
        elif report[1] > report[0] and report[0] + 3 >= report[1]:
            isAsc = True
        else:
            copy = report.copy()
            report.pop(0)
            copy.pop(1)
            if self.is_safe(report) or self.is_safe(copy):
                return True
            return False
        for i in range(1, len(report) - 1):
            if isAsc:
                low = report[i]
                high = report[i+1]
            else:
                low = report[i+1]
                high = report[i]
            if high < low or not self.is_pair_safe(high, low):
                minus = report.copy()
                plus = report.copy()
                report.pop(i)
                minus.pop(i - 1)
                plus.pop(i + 1)
                if self.is_safe(report) or self.is_safe(minus) or self.is_safe(plus):
                    return True
                return False
        return True

    def is_pair_safe(self, num1, num2):
        return num1 != num2 and abs(num1 - num2) <= 3

    def part_two(self):
        reports = self.parse_input()
        safe = 0
        for report in reports:
            safe += 1 if self.is_safe_with_tolerance(report) else 0
        return safe

DayTwo().run(sys.argv[1])
