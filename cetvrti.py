
def ispis_zvj(br):
    for i in range(br):
        print('*', end="")
    print("")

def print_space(br):
    for i in range(br):
        print(' ', end="")



br=int(input("Unesi broj:"))
razmak=br-1


for i in range(1,br,2):
    print_space(int(razmak/2)-int(i/2))
    ispis_zvj(i)

if br % 2 == 0:
    br = br - 1

for i in range(br, 0, -2):
    print_space(int(razmak/2)-int(i/2))
    ispis_zvj(i)