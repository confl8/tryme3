def three_lines():
    print ("\n")
    print ("\n")
    print ("\n")

def nine_lines():
    three_lines()
    three_lines()
    three_lines()

print ("First line look at me")
nine_lines()
print ("That was 9 blank lines")

def clear_screen():
    nine_lines()
    nine_lines()
    three_lines()
    three_lines()

print ("Now, I give you twenty-five blank lines")
clear_screen()
