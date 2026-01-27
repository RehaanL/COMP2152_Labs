# Lab03 Coding Questions

## Question 1 {
print("QUESTION 1")
grades = [85, 92, 78, 95, 88]
grades.append(90)

grades.sort()
print("Sorted grades:", grades)
print("Highest grade:", grades[-1])
print("Lowest grade:", grades[0])
print("Total number of grades:", len(grades))
print()
# }

#------------------------------------------------#

## Question 2 {
print("QUESTION 2")
cart = ["apple", "banana", "milk", "bread", "apple", "eggs"]
print("Number of apples: ", cart.count("apple"))
print("Position of milk: ", cart.index("milk"))
cart.remove("apple")
print("removed item using pop:", cart.pop(-1))
if "banana" in cart:
    print("Is banana in cart? True")
else:
    print("Is banana in cart? False")
print("Final cart:", cart)
print()
# }

#------------------------------------------------#

## Question 3 {
print("QUESTION 3")
point1 = (3,5)
print("Point:",point1)
point2 = (7,2)
print("Point2:",point2)
x1 = point1[0]
y1 = point1[1]
print("x1 =", x1, ",","y1 =",y1)
x2 = point2[0]
y2 = point2[1]
print("x2 =", x2, ",","y2 =",y2)
print("Distance between points:", ((x2-x1)**2 + (y2-y1)**2)**0.5)

char_tuple = tuple("PYTHON")
print("Characters tuple:", char_tuple)
for char in char_tuple:
    print(char)
print()
# }

#------------------------------------------------#

## Question 4
print("QUESTION 4")
monday_class = {"Alice", "Bob", "Charlie", "Diana"}
print("Monday class:", monday_class)
wednesday_class = {"Bob", "Diana", "Eve", "Frank"}
print("Wednesday class:", wednesday_class)
monday_class.add("Grace")

print("Attended both classes:", monday_class & wednesday_class)
print("Attended either class:", monday_class | wednesday_class)

print("Only Monday:", monday_class - wednesday_class)
print("Only one class (not both):", monday_class ^ wednesday_class)

if monday_class <= (monday_class | wednesday_class):
    print("Is Monday subset of all students? True")
else:
    print("Is Monday subset of all students? False")
print()
# }

#------------------------------------------------#

## Question 5
print("QUESTION 5")
contacts = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9999",
}
print("Alice's number:", contacts["Alice"])
contacts["Diana"] = "555-0000"
print("Contacts after adding Diana:", contacts)

contacts["Bob"] = "555-0000"
print("Contacts after updating Bob:", contacts)

del contacts["Charlie"]
print("Contacts after deleting Charlie:", contacts)

print("All names:", contacts.keys())
print("All numbers:", contacts.values())
print("Total contacts:", len(contacts))
print()
# }

#------------------------------------------------#
print("QUESTION 6")
print("=== Current Inventory ===")
inventory = {
    "Laptop": (999.99,5),
    "Mouse": (29.99, 15),
    "Keyboard": (79.99, 10),
    "Monitor": (299.99, 8)
}
for item in inventory:
    print(item, "- Price:", f"${inventory[item][0]},", "Quantity:", inventory[item][1])

electronics = {"Laptop", "Monitor"}
accessories = {"Mouse", "Keyboard"}
print("\nAll product categories:", electronics | accessories)

price_list = []
for item in inventory:
    price_list.append(inventory[item][0])

print("\nPrice list:",price_list)
price_list.sort()
print("Sorted prices:", price_list)
print("Lowest price:", f"${price_list[0]}" )
print("Highest price:", f"${price_list[-1]}" )

inventory["Headphones"] = (49.99, 20)
inventory["Mouse"] = (29.99, 12)
del inventory["Monitor"]

print("\n=== Final Inventory ===")
for item in inventory:
    print(item, "- Price:", f"${inventory[item][0]},", "Quantity:", inventory[item][1])




