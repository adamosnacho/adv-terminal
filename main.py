import os
running = True
mode = 1
print('[APPLICATION] better terminal by Adam Ryan | use help for help')
while running:
    if mode == 1:
        inp = input('[USER] command --> ')
    else:
        inp = input('[COMMANDER] command --> ')
    if inp == 'md' and mode == 1:
        mode = 0
    else:
        if inp == 'md':
            mode = 1
    if inp == 'q' and 1 == mode:
        running = False
    if inp == 'help' and mode == 1:
        print('[HELP] us md to swich modes|use q as a user to quit|use help as a user for help(this menu)|use $ as a commander to enter system commands')
    if inp == '$' and 0 == mode:
        inp = input('[SYSTEM] enter system command --> ')
        os.system(inp)

