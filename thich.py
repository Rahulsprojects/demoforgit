thickness = int(input())    #This must be an odd number
c = 'H'

# Top cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

# Top pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

# Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))











