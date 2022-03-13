import pycosat
from QueenCNFBuilder import build_cnf, get_cells_from_cnf


if __name__ == '__main__':
    n = int(input("Insert size of board: "))
    cnf = build_cnf(n)
    cnf_res = pycosat.solve(cnf)

    if type(cnf_res) == str and cnf_res == "UNSAT":
        print(f"It is impossible to put {n} queens on the board of size {n}")
        exit(0)

    queens_cells = get_cells_from_cnf(cnf_res, n)
    print("Solution: ")
    for it, cell in enumerate(queens_cells):
        if it == len(queens_cells) - 1:
            print(cell)
        else:
            print(cell, ", ", end='', sep='')
