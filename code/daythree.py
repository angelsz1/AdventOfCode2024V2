import sys
import re
from solution import Solution


class DayThree(Solution):

    def __init__(self):
        self._setup('daythree')

    def part_one(self):
        muls = re.findall(r'mul\(\d+,\d+\)', self.input)
        sum = 0
        for mul in muls:
            nums = [int(val) for val in re.split(',', re.findall(r'\d+,\d+', mul)[0])]
            sum += nums[0] * nums[1]
        return sum

    def part_two(self):
        pass

DayThree().run(sys.argv[1])
