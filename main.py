from src import sorting
from src import sortstring

choice = input("")

if choice == "1":
	sorting.main()
elif choice == "2":
	sortstring.main()
else:
	print("Wrong choise, 1 or 2. Restart program")
input("Enter to exit")