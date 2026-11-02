import time

print("THE MIND labyrthtign")
print("welcome the labyrinth, hello world")


wall = "#"
treasure = "T"
player = "P"
empty = "."
map = [[empty, empty, empty, wall, player],
       [empty, wall, empty, wall, empty],
       [empty, wall, empty, empty, empty],
       [treasure, wall, empty, wall, wall],
       [empty, empty, wall, wall, empty]]

player_coords = [0, 4]
treasure_coords = [3, 0]



def display(maze):
       for row in maze:
              print(row)

def checkUp(coords):
       if coords[0] >= 1 and coords[1] >= 0:
              if map[coords[0]-1][coords[1]] == empty:
                     return True
              elif map[coords[0]-1][coords[1]] == treasure:
                     return "wincon"
              else:
                     return False
       else:
              return False


def checkDown(coords):
       if coords[0] != 4 and coords[1] >= 0:
              if map[coords[0]+1][coords[1]] == empty:
                     return True
              elif map[coords[0]+1][coords[1]] == treasure:
                     return "wincon"
              else:
                     return False
       else:
              return False

def checkRight(coords):
       if coords[0] >= 0 and coords[1] != 4:
              if map[coords[0]][coords[1]+1] == empty:
                     return True
              elif map[coords[0]][coords[1]+1] == treasure:
                     return "wincon"
              else:
                     return False
       else:
              return False

def checkLeft(coords):
       if coords[0] >= 0 and coords[1] >= 1:
              if map[coords[0]][coords[1]-1] == empty:
                     return True
              elif map[coords[0]][coords[1]-1] == treasure:
                     return "wincon"
              else:
                     return False
       else:
              return False

used_coords = []
new_coords = None

while player_coords != treasure_coords:
       time.sleep(2)
       display(map)
       print()
       if checkUp(player_coords):
              falses = 0
              new_coords = [player_coords[0]-1, player_coords[1]]
              if not checkUp(new_coords):
                     falses += 1
              elif not checkDown(new_coords):
                     falses += 1
              elif not checkRight(new_coords):
                     falses += 1
              elif not checkLeft(new_coords):
                     falses += 1
              if falses == 3:
                     new_coords_value = False
              else:
                     new_coords_value = True
              if new_coords_value:
                     used_coords.append(player_coords)
                     print(used_coords)
                     val = 0
                     val2 = 0
                     for i in used_coords:
                            val += 1
                            if i != new_coords:
                                   val2 +=1
                     if val == val2:
                            map[player_coords[0]][player_coords[1]] = map[player_coords[0]-1][player_coords[1]]
                            player_coords = new_coords
                            map[player_coords[0]][player_coords[1]] = "P"
       elif checkUp(player_coords) == "wincon":
              print("-------------------------")
              print("YOU WINNN OMMGGGGG YESSS")
              print("-------------------------")

       if checkDown(player_coords):
              falses = 0
              new_coords = [player_coords[0]+1, player_coords[1]]
              if not checkUp(new_coords):
                     falses += 1
              elif not checkDown(new_coords):
                     falses += 1
              elif not checkRight(new_coords):
                     falses += 1
              elif not checkLeft(new_coords):
                     falses += 1
              if falses == 3:
                     new_coords_value = False
              else:
                     new_coords_value = True
              if new_coords_value:
                     used_coords.append(player_coords)
                     print(used_coords)
                     val = 0
                     val2 = 0
                     for i in used_coords:
                            val += 1
                            if i != new_coords:
                                   val2 +=1
                     if val == val2:
                            map[player_coords[0]][player_coords[1]] = map[player_coords[0]-1][player_coords[1]]
                            player_coords = new_coords
                            map[player_coords[0]][player_coords[1]] = "P"
       elif checkUp(player_coords) == "wincon":
              print("-------------------------")
              print("YOU WINNN OMMGGGGG YESSS")
              print("-------------------------")

       if checkRight(player_coords):
              falses = 0
              new_coords = [player_coords[0], player_coords[1]+1]
              if not checkUp(new_coords):
                     falses += 1
              elif not checkDown(new_coords):
                     falses += 1
              elif not checkRight(new_coords):
                     falses += 1
              elif not checkLeft(new_coords):
                     falses += 1
              if falses == 3:
                     new_coords_value = False
              else:
                     new_coords_value = True
              if new_coords_value:
                     used_coords.append(player_coords)
                     print(used_coords)
                     val = 0
                     val2 = 0
                     for i in used_coords:
                            val += 1
                            if i != new_coords:
                                   val2 +=1
                     if val == val2:
                            map[player_coords[0]][player_coords[1]] = map[player_coords[0]-1][player_coords[1]]
                            player_coords = new_coords
                            map[player_coords[0]][player_coords[1]] = "P"
       elif checkUp(player_coords) == "wincon":
              print("-------------------------")
              print("YOU WINNN OMMGGGGG YESSS")
              print("-------------------------")


       if checkLeft(player_coords):
              falses = 0
              new_coords = [player_coords[0], player_coords[1]-1]
              if not checkUp(new_coords):
                     falses += 1
              elif not checkDown(new_coords):
                     falses += 1
              elif not checkRight(new_coords):
                     falses += 1
              elif not checkLeft(new_coords):
                     falses += 1
              if falses == 3:
                     new_coords_value = False
              else:
                     new_coords_value = True
              if new_coords_value:
                     used_coords.append(player_coords)
                     print(used_coords)
                     val = 0
                     val2 = 0
                     for i in used_coords:
                            val += 1
                            if i != new_coords:
                                   val2 +=1
                     if val == val2:
                            map[player_coords[0]][player_coords[1]] = map[player_coords[0]-1][player_coords[1]]
                            player_coords = new_coords
                            map[player_coords[0]][player_coords[1]] = "P"

       elif checkUp(player_coords) == "wincon":
              print("-------------------------")
              print("YOU WINNN OMMGGGGG YESSS")
              print("-------------------------")
       
