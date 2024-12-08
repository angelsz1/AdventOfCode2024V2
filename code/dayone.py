import sys
from solution import Solution


class DayOne(Solution):

    def __init__(self):
        self._setup('dayone')

    def parse_input(self):
        left = []
        right = []
        for line in self.input.split('\n'):
            nums = line.split('   ')
            left.append(int(nums[0]))
            right.append(int(nums[1]))
        return left, right

    def part_one(self):
        left, right = self.parse_input()
        left.sort()
        right.sort()
        return self.calculate_diff(left, right)

    def calculate_diff(self, l, r):
        diff = 0
        for i in range(len(l)):
            diff += abs(l[i] - r[i])
        return diff

    def part_two(self):
        left, right = self.parse_input()
        left.sort()
        right.sort()
        return self.calculate_similarity(left, right)

    def calculate_similarity(self, l, r):
        similarity = 0
        for num in l:
            similarity += num * r.count(num)
        return similarity
            

DayOne().run(sys.argv[1])
