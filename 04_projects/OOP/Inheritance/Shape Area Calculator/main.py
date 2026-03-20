from shapes import Circle, Rectangle, Triangle
def main():
    cir=Circle(5)
    rect=Rectangle(4,6)
    tri=Triangle(3,7)
    shapes=[cir,rect,tri]
    for s in shapes:
        print(f"{s.__class__.__name__} area = {s.area()}")

if __name__=="__main__":
    main()