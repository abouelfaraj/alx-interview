#!/usrin/python3
'''N Queens Backtrack'''

import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
        
        try:
            n = int(sys.argv[1])
        except ValueError:
            print('N must be at least 4')
            exit(1)

    if n < 4:
        print('N must be at least 4')
        exit(1)

    solutions = []
    p_queens = []
    stop = False
    r = 0

    while r < n:
