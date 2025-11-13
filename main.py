

from shapes_module import Cylinder, Cone, Cube, Cuboid, Sphere

def main():
    print("===== 3D SHAPE CALCULATOR =====")
    print("Select the shape:")
    print("1. Cylinder")
    print("2. Cone")
    print("3. Cube")
    print("4. Cuboid")
    print("5. Sphere")

    choice = int(input("Enter your choice (1-5): "))

    # Create object based on user selection
    shape = None

    # Cylinder
    if choice == 1:
        r = float(input("Enter radius: "))
        h = float(input("Enter height: "))
        shape = Cylinder(r, h)

    # Cone
    elif choice == 2:
        r = float(input("Enter radius: "))
        h = float(input("Enter height: "))
        shape = Cone(r, h)

    # Cube
    elif choice == 3:
        s = float(input("Enter side length: "))
        shape = Cube(s)

    # Cuboid
    elif choice == 4:
        l = float(input("Enter length: "))
        b = float(input("Enter breadth: "))
        h = float(input("Enter height: "))
        shape = Cuboid(l, b, h)

    # Sphere
    elif choice == 5:
        r = float(input("Enter radius: "))
        shape = Sphere(r)

    else:
        print("Invalid shape choice!")
        return

    # Menu for operations
    print("\nSelect Operation:")
    print("1. Curved Surface Area (CSA)")
    print("2. Total Surface Area (TSA)")
    print("3. Volume")

    op = int(input("Enter your choice (1-3): "))

    # Perform selected operation (Polymorphism)
    if op == 1:
        print("\nCurved Surface Area (CSA) =", shape.csa())
    elif op == 2:
        print("\nTotal Surface Area (TSA) =", shape.tsa())
    elif op == 3:
        print("\nVolume =", shape.volume())
    else:
        print("Invalid operation selected!")

if __name__ == "__main__":
    main()
