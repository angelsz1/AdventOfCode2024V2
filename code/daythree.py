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
        sum = 0
        dos = re.finditer(r'do\(\)', self.input)
        donts = re.finditer(r'don\'t\(\)', self.input)
        muls = re.finditer(r'mul\(\d+,\d+\)', self.input)
        dosStart, dontsStart = self.get_do_donts(dos, donts)
        starts, isValid = self.get_starts(dosStart, dontsStart)
        for mul in muls:
            if self.is_valid_mul(mul.start(), starts, isValid):
                value = mul.group()
                nums = [int(val) for val in re.split(',', re.findall(r'\d+,\d+', value)[0])]
                sum += nums[0] * nums[1]
        return sum

    def is_valid_mul(self, mul, starts, valid):
        i = 0
        while i < len(starts) and mul > starts[i]:
            i += 1
        return valid[i-1]
        
    def get_starts(self, do, dont):
        starts = [0]
        valid = [True]
        while len(do) > 0 and len(dont) > 0:
            if do[0] < dont[0]:
                starts.append(do.pop(0))
                valid.append(True)
            else:
                starts.append(dont.pop(0))
                valid.append(False)
        for d in do:
            starts.append(d)
            valid.append(True)
        for d in dont:
            starts.append(d)
            valid.append(False)
        return starts, valid


    def get_do_donts(self, dos, donts):
        dosStart = []
        dontsStart = []
        for do in dos:
            dosStart.append(do.start())
        for dont in donts:
            dontsStart.append(dont.start())
        return dosStart, dontsStart


DayThree().run(sys.argv[1])
