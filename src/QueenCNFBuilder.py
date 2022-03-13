from Cell import *
import copy


def forbid_beaten_cells(cell, n):
    def forbid2cells(cell_1, cell_2):
        return [[-cell_1.to_num(n), -cell_2.to_num(n)]]

    cnf = []

    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if abs(dx) + abs(dy) == 0:
                continue

            cell_copy = copy.deepcopy(cell)
            while True:
                cell_copy.x += dx
                cell_copy.y += dy
                if not (0 <= cell_copy.x < n and 0 <= cell_copy.y < n):
                    break
                cnf += forbid2cells(cell, cell_copy)

    return cnf


def n_queen(n):
    return [[Cell(row, col).to_num(n) for col in range(n)] for row in range(n)]


def build_cnf(n):
    cnf = []
    for x in range(n):
        for y in range(n):
            cnf += forbid_beaten_cells(Cell(x, y), n)
    cnf += n_queen(n)
    return cnf


def get_cells_from_cnf(cnf_res, n):
    return list(map(lambda num: Cell.from_num(num, n),
                    filter(lambda res: res > 0, cnf_res)))
