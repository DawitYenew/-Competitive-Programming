def theater_square(n, m, a):
    if n%a == 0:
        sqaure1 = n//a
    else:
        square1 = n//a + 1
    
    if m%a == 0:
        square2 = m//a
    else:
        square2 = m//a + 1
    return square1 + square2

x, y, z = map(int,(input("Enter the diamensions: ").split()))
print(theater_square(x,y,z))

    