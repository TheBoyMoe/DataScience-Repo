phone_dict = { }

# Main function. Prompts for next command and executes.
def main():
    while True:
        prompt = 'Choose: 1. data entry, '
        prompt += '2. query, 3. exit, 4. prefix, 5. load file, '
        prompt += '6. save >> '
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
        elif cmd == 5:
            load_file()
        elif cmd == 6:
            save_file()

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
                       
# Load files function.
# Use try/except to re-prompt if file not found.
def load_file():
    phone_dict.clear()       # This dict created earlier.
    while True:
        try:
            fname = input('Enter file to load: ')
            in_file = open(fname, 'r')
            a_list = in_file.readlines()
            for i in range(0, len(a_list), 2):
                key_str = (a_list[i]).strip('\n')
                val_str = (a_list[i + 1]).strip('\n')
                phone_dict[key_str] = val_str
            print(fname, 'successfully loaded.')
            in_file.close()
            break
        except FileNotFoundError:
            print('File not found. Re-enter.')

# Save file function.
# Prompt for name of oa file and then write out key/val pairs.
def save_file():
    fname = input('Enter name of a file to save to: ')
    out_file = open(fname, 'w')
    for k in phone_dict:
        out_file.write(k + '\n')
        out_file.write(phone_dict[k] + '\n')
    out_file.close()

main()
