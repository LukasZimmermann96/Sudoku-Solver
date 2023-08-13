import datetime


ALL_OPTIONS = [str(x + 1) for x in range(9)]

def init_board(input: str, empty_board: list):
  input_board = input.strip().split('= ')[1]       # remove unnecessary notation
  input_rows = trim_first_and_last_n_elemets(input_board, 2).split('],[')
  for row in input_rows:
    empty_board.append(trim_first_and_last_n_elemets(row, 1).split('","'))
  return empty_board

def init_possible_options_board(length : int , height: int, empty_option_board: list):
  for i in range(length):
    empty_option_board.append([])
    for j in range(height):
      empty_option_board[i].append([str(x + 1) for x in range(9)])
  return empty_option_board
  

def board_is_full(board: list):
  for row in board:
    for cell in row:
      if cell == '.':
        return False
  return True

def get_options_for_cell(board: list, option_board: list, lenght_x: int, height_y: int):
  def contain_in_row(row: list, value: int):
    return str(value) in row
  def contain_in_column(value: int):
    for row in board:
      if row[height_y] == str(value):
        return True
    return False
  def contain_in_box(value: int):
    box_lenght_x_start_index =  int(lenght_x / 3) * 3
    box_height_y_start_index = int(height_y / 3) * 3
    for box_row in board[box_lenght_x_start_index:box_lenght_x_start_index + 3]:
      if str(value) in box_row[box_height_y_start_index:box_height_y_start_index + 3]:
        return True
    return False
  
  removable_options = []
  for option in option_board[lenght_x][height_y]:
    if contain_in_row(board[lenght_x], int(option)) or contain_in_column(int(option)) or contain_in_box(int(option)):
      removable_options.append(option)
  left_over_options = option_board[lenght_x][height_y]
  for option in removable_options:
      left_over_options.remove(option)

  option_board[lenght_x][height_y] = left_over_options
  return option_board[lenght_x][height_y]
    


def solve(board: list):
  option_board = init_possible_options_board(9, 9, [])
  iterations = 0
  while not board_is_full(board):
    iterations = iterations + 1
    for lenght_x, row in enumerate(board):
      for height_y, cell in enumerate(row):
        options = get_options_for_cell(board=board, option_board=option_board, lenght_x=lenght_x, height_y=height_y)
        if len(options) == 1 and board[lenght_x][height_y] == '.':
          board[lenght_x][height_y] = options[0]
  return board, iterations

def print_board(board):
  print(board)
  return None

def trim_first_and_last_n_elemets(_list: list, n: int):
  return _list[n:len(_list)-n]

iterations = 0
starttime = datetime.datetime.now()
input = 'board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]'
unsolved_board = init_board(input=input, empty_board=[])
print_board(unsolved_board)
(solved_board, iterations) = solve(unsolved_board)
endtime = datetime.datetime.now()
print(f'board solved in {endtime - starttime} with {iterations} iterations')
print_board(solved_board)
