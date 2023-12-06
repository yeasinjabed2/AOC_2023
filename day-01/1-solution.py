def get_cal_val(line: str) -> int:
    digits = []
    for char in line:
        if char.isdigit():
            digits.append(char)
    return int(digits[0] + digits[-1])


def run(path: str):
    with open(path, 'r') as f:
        lines = f.read().strip().split('\n')
    return sum([get_cal_val(line) for line in lines])


print(run('day-01/1-input.txt'))
