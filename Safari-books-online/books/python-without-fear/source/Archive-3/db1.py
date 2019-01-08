emp_dict = {}
prompt = 'Select: 1. data entry, 2. query, 3. exit >> '

class Employee:
     def __init__(self, name, jname, jrank, salary):
          self.name = name
          self.jname = jname
          self.jrank = jrank
          self.salary = salary

# Main function. Prompts for command and executes.

def main():
     while True:
          s = input(prompt)
          if len(s) == 0:
               break
          cmd = int(s)
          if cmd == 3:
               break
          if cmd == 1:
               add_entries()
          elif cmd == 2:
               display_entries()

# Add Entries function. Prompts for key-balue pairs
# until user wants to exit. Adds key-value to dict.

def add_entries():
     while True:
          key_str = input('Input name (ENTER to exit): ')
          key_str = key_str.strip()
          if not key_str:
               return
          jname = input('Enter job name: ')
          jrank = int(input('Enter job rank: '))
          salary = float(input('Enter salary: '))
          emp_dict[key_str] = Employee(key_str, jname, jrank,
                                       salary)

# Display entires function. Prompts for a name and
# prints values. Re-prompts if key not found.

def display_entries():
     while True:
          key_str = input('Input name (ENTER to exist): ')
          key_str = key_str.strip()
          if not key_str:
               return
          emp_obj = emp_dict.get(key_str)
          if emp_obj is None:
               print('Name not found. Re-enter. ')
          else:
               print('Name:', emp_obj.name)
               print('Job title:', emp_obj.jname)
               print('Job rank:', emp_obj.jrank)
               print('Salary:', emp_obj.salary)

main()
