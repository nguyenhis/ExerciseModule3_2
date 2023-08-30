description_cabin_classes={"LUX":"upper-deck cabin with a balcony",
                   "A":"above the car deck, equipped with a window",
                   "B":"windowless cabin above the car deck",
                   "C":"windowless cabin below the car deck"}
cabin_class = input("Enter cabin class: ")
if cabin_class == "LUX":
    print(f"Your cabin is {description_cabin_classes[cabin_class]}.")
elif cabin_class == "A":
    print(f"Your cabin is {description_cabin_classes[cabin_class]}.")
elif cabin_class == "B":
    print(f"Your cabin is {description_cabin_classes[cabin_class]}.")
elif cabin_class == "C":
    print(f"Your cabin is {description_cabin_classes[cabin_class]}.")
else:
    print("Invalid cabin class.")
