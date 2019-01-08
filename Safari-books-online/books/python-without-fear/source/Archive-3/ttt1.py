sz = 3
mat = [['.' for j in range(sz)] for i in range(sz)]

def main():
     num_moves = 0
     print_mat()
     print('Moves are r,c or "0" to exit.')
     exit_flag = False
     while not exit_flag:
          num_moves += 1
          if num_moves > 9:
               print('No more space. It is a tie.')
               exit_flag = True
          player_ch = 'X' if num_moves % 2 > 0 else 'O'
          exit_flag, r, c = get_move(player_ch)

def get_move(player_ch):
     while True:
          prompt = 'Enter move for ' + player_ch + ': '
          s = input(prompt)
          a_list = s.split(',')
          if len(a_list) >= 1 and int(a_list[0]) == 0:
               print('Bye now.')
               return True, 0, 0
          elif len(a_list) < 2:
               print('Use row, col. Re-enter.')
          else:
               r = int(a_list[0]) - 1
               c = int(a_list[1]) - 1
               if r < 0 or r >= sz or c < 0 or c >= sz:
                     print('Out of range. Re-enter.')
               elif mat[r][c] != '.':
                     print('Occupied square. Re-enter.')
               else:
                     mat[r][c] = player_ch
                     print_mat()
                     break
     return False, r, c
                                    
def print_mat():
     s = ''
     s += '  1 2 3\n'
     for i in range(sz):
          s += str(i + 1) + ' '
          for j in range(sz):
               s += mat[i][j] + ' '
          s += '\n'
     print(s)

def print_mat2():
     lines = []
     lines.append('   1 2 3')
     for i in range(sz):
          cur_line = [str(i + 1) + ' ']
          for j in range(sz):
               cur_line.append(str(mat[i][j]))
          lines.append((' ').join(cur_line))
     print(('\n').join(lines))
                                 
main()


    


