print("welcome the labyrinth")
found_row, found_col = -1, -1


wall = "#"
treasure = "T"
player = "P"
empty = "."
map = [[empty, empty, empty, wall, player],
       [empty, wall, empty, wall, empty],
       [empty, wall, empty, empty, empty],
       [treasure, wall, empty, wall, wall],
       [empty, empty, wall, wall, empty]]

def wasd(moves):
    for rowindex,row in enumerate(map):
        if player in row:
            found_row = rowindex
            found_col = row.index(player)
            break

    old_row, old_col = found_row, found_col

    if moves.upper() == "W":
        found_row -= 1
    elif moves.upper() == "S":
        found_row += 1
    elif moves.upper() == "A":
        found_col -= 1
    elif moves.upper() == "D":
        found_col += 1
    else:
        print("invalid input bruv")
        return

    if 0 <= found_row < len(map) and 0 <= found_col < len(map[0]):
        rn = map[found_row][found_col]

        if rn == wall:
            print("cant go there bud its walled")
        elif rn == treasure:
            print("you win")
            map[old_row][old_col] = empty
            map[found_row][found_col] = player
            exit()
        else:
            map[old_row][old_col] = empty
            map[found_row][found_col] = player


while True:
    for rows in map:
        print(rows)
    movement = input("enter your move to reach the treasure (WASD): ")
    wasd(movement)





