def solve_linear_system(a1, b1, c1, a2, b2, c2):
    # Write your code hdef solve_linear_system(a1, b1, c1, a2, b2, c2):
    det = a1 * b2 - a2 * b1
    if det == 0:
        raise ValueError("The system does not have a unique solution.")
    x = (c1 * b2 - c2 * b1) / det
    y = (a1 * c2 - a2 * c1) / det
    return (x, y)
solution = solve_linear_system(2, 3, 8, 5, -1, 4)
print("x =", solution[0], ", y =", solution[1])