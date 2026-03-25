FILE = "data.txt"

def write_file():
    try:
        data = input("Enter text to write: ")

        with open(FILE, "a") as file:
            file.write(data + "\n")

        print("Data written successfully")

    except PermissionError:
        print("Permission denied!")

    except Exception as e:
        print("Error:", e)


def read_file():
    try:
        with open(FILE, "r") as file:
            content = file.read()
            print("\nFile Content:\n", content)

    except FileNotFoundError:
        print("File not found! Please write data first.")

    except Exception as e:
        print("Error:", e)


def menu():
    while True:
        print("\n1. Write to file")
        print("2. Read file")
        print("3. Exit")

        try:
            choice = int(input("Enter choice: "))

            if choice == 1:
                write_file()
            elif choice == 2:
                read_file()
            elif choice == 3:
                print("Exiting...")
                break
            else:
                print("Invalid choice")

        except ValueError:
            print("Please enter a valid number!")


menu()