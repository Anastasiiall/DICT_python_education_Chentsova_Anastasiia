import ast
import itertools
import copy
from math import floor, ceil

def m_input(row):
    line = row
    a = []
    for i in range(line):
        t = []
        for k in input().split():
            if k != " ":
                t.append(ast.literal_eval(k))
        a.append(t)
    return a


def m_print(result, row, column):
    line, columns = row, column
    for x in range(line):
        for k in range(columns):
            if result[x][k] == -0.0:
                print(0, end=" ")
            elif type(result[x][k]) == int or result[x][k] == 0:
                print(result[x][k], end=" ")
            elif type(result[x][k]) == float and result[x][k] != 0:
                if result[x][k] > 0:
                    print(floor(result[x][k] * 100) / 100.0, end=" ")
                else:
                    print(ceil(result[x][k] * 100) / 100.0, end=" ")
        print()


def m_sum(a1, a2, row, col):
    line, columns = row, col
    append = []
    for i in range(line):
        u = []
        for j in range(columns):
            u.append(a1[i][j] + a2[i][j])
        append.append(u)
    return append


def m_number(a1, number_m):
    multiply = []
    for x in range(len(a)):
        u = []
        for k in range(len(a[0])):
            u.append(a1[x][k] * number_m)
        multiply.append(u)
    return multiply


def m_element(c1, c2):
    result = 0
    for x in range(len(c1)):
        result += c1[x] * c2[x]
    return result


def m_two(a1, a2):
    value = [[0 for row in range(len(a2[0]))] for column in range(len(a1))]
    for x in range(len(a1)):
        l1 = a1[x]
        for k in range(len(a2[0])):
            l2 = [a2[y][k] for y in range(len(a2))]
            value_range = m_element(l1, l2)
            value[x][k] = value_range
    return value

def tr(g):
    return list(itertools.zip_longest(*g))


def sd(g):
    new_m = [[g[k][x] for k in range(len(g))] for x in range(len(g[0]) - 1, -1, -1)]
    result = []
    for x in range(len(new_m[0])):
        new_m[x] = new_m[x][::-1]
        result.append(new_m[x])
    return result


def vr(g):
    new_m = [[g[k][x] for k in range(len(g))] for x in range(len(g[0]) - 1, -1, -1)]
    result = list(itertools.zip_longest(*new_m))
    return result


def bc(g):
    result = list(itertools.zip_longest(*g[::-1]))
    result = list(itertools.zip_longest(*result))
    return result


def l(m_min, x, k):
        return [row[:k] + row[k + 1:] for row in (m_min[:x] + m_min[x + 1:])]


def min_t(g):
    d = det(g)
    if len(g) == 2:
        return [[g[1][1] / d, -1 * g[0][1] / d],
                [-1 * g[1][0] / d, g[0][0] / d]]
    cof = []
    for w in range(len(g)):
        s = []
        for k in range(len(g)):
            mino = min(g, w, k)
            s.append(((-1) ** (w + k)) * det(mino))
        cof.append(s)
    cof = tr(cof)
    for x in range(len(cof)):
        cof[x] = list(cof[x])
    for w in range(len(cof)):
        for k in range(len(cof)):
            cof[w][k] = int(cof[w][k]) / d
    return cof

def det(m_det):
    if len(m_det) == 2:
        return m_det[0][0] * m_det[1][1] - m_det[0][1] * m_det[1][0]
    d = 0
    for x in range(len(m_det)):
        d += ((-1) ** x) * m_det[0][x] * det(min(m_det, 0, x))
    return d


while True:
    print("""1. Add matrices
    2. Multiply matrix by a constant
    3. Multiply matrices
    4. Transpose matrix
    5. Calculate a determinant
    6. Inverse matrix
0. Exit""")

    ch = int(input('Your choice:'))
    if ch == 1:
        f, n = map(int, input("Enter size of first matrix:").split())
        print("Enter first matrix:")
        a = m_input(f)
        p, q = map(int, input("Enter size of second matrix:").split())
        print("Enter second matrix:")
        b = m_input(p)
        if f != p and n != q:
            print("The operation cannot be performed.")
        else:
            c = m_sum(a, b, f, n)
            m_print(c, f, n)
    elif ch == 2:
        f, n = map(int, input("Enter size of matrix:").split())
        print("Enter matrix:")
        a = m_input(f)
        number = float(input("Enter constant:"))
        c = m_number(a, number)
        print("The result is:")
        m_print(c, f, n)
    elif ch == 3:
        f, n = map(int, input("Enter size of first matrix:").split())
        print("Enter first matrix:")
        a = m_input(f)
        p, q = map(int, input("Enter size of second matrix:").split())
        print("Enter second matrix:")
        b = m_input(p)
        c = m_two(a, b)
        print("The result is:")
        m_print(c, f, q)
    elif ch == 4:
        print("""1. Main diagonal
        2. Side diagonal
        3. Vertical line
        4. Horizontal line.""")
        choice = int(input("Your choice:"))
        if choice == 1:
            f, n = map(int, input("Enter size of matrix:").split())
            print('Enter matrix:')
            a = m_input(f)
            c = tr(a)
            print('The result is:')
            m_print(c, n, f)
        elif choice == 2:
            f, n = map(int, input("Enter size of matrix:").split())
            print('Enter matrix:')
            a = m_input(f)
            c = tr(a)
            print('The result is:')
            m_print(c, n, f)
        elif ch == 3:
            f, n = map(int, input("Enter size of matrix:").split())
            print('Enter matrix:')
            a = m_input(f)
            c = vr(a)
            print('The result is:')
            m_print(c, f, n)
        elif ch == 4:
            f, n = map(int, input("Enter size of matrix:").split())
            print('Enter matrix:')
            a = m_input(f)
            c = bc(a)
            print('The result is:')
            m_print(c, f, n)
        elif choice == 5:
            f, n = map(int, input("Enter size of matrix:").split())
            print('Enter matrix:')
            a = m_input(f)
            c = det(a)
            print('The result is:')
            print(c)
        elif choice == 6:
            f, n = map(int, input("Enter size of matrix:").split())
            print('Enter matrix:')
            a = m_input(f)
            c = det(a)
            print(c)
            if c != 0:
                d = min_t(a)
                print('The result is:')
                m_print(d, f, n)
            else:
                print("This matrix doesn't have an inverse.")
        elif ch == 0:
            break