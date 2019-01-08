phone_dict = { }

# Main function. Prompts for next command and executes.
def main():
    while True:
        prompt = 'Enter command: 1. data entry. '
        prompt += '2. query, 3. exit, 4. prefix >> '
        s = input(prompt)
        if not s:              # If string empty, break
            break
        cmd = int(s)
        if cmd == 3:
            break
        if cmd == 1:
            add_entries()
        elif cmd == 2:
            display_entries()
        elif cmd == 4:
            display_by_prefix()

# Add Entries function. Prompts for key-value pairs
# until user wants to exit. Adds key-value to dict.
def add_entries():
    while True:
        key_str = input('Input name (ENTER to exit): ')
        key_str = key_str.strip()
        if not key_str:        # If key_str empty, return
            return
        val_str = input('Enter phone no: ')
        val_str = val_str.strip()
        if not val_str:
            return
        phone_dict[key_str] = val_str

# Display Entries function. Prompts for name & prints
# corresponding value. Re-prompts if key not found.
def display_entries():
    while True:
        key_str = input('Enter name (ENTER to exit): ')
        key_str = key_str.strip()
        if not key_str:        # If key_str empty, return
            return
        val_str = phone_dict.get(key_str)
        if val_str:
            print(val_str)
        else:
            print('Name not found. Re-enter.')

# Get by Prefix function. Prompt and search dict.
def display_by_prefix():
    while True:
        s = input('Enter prefix (ENTER to exit): ')
        s = s.strip()
        if not s:
            return
        for k, v in phone_dict.items():
            if k.startswith(s):
                print(k, '\t', v)
                       
main()
