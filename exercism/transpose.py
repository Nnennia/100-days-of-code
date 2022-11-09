def transpose(lines):
    lines = [line.replace(' ', '$') for line in lines.splitlines()]
    lines = [line.ljust(len(max(lines, key=len))) for line in lines]
    lines = [''.join(line) for line in zip(*lines)]
    return '\n'.join(line.rstrip().replace('$', ' ') for line in lines)
