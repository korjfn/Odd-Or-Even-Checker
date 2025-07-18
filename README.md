---

# Odd or Even Checker ✅

A simple Python program that lets users check if a number is **odd** or **even** in a continuous loop until they choose to exit.

## Features

* ✅ Continuously checks numbers until user types `0` to exit
* ✅ Handles invalid input gracefully with error messages
* ✅ Provides clear and friendly user prompts

## How It Works

* The user is welcomed with a message.
* The program asks the user to enter a number or type `0` to exit.
* If the input is a valid integer:

  * If `0`, the program says goodbye and exits.
  * If even, it prints "`<number> Is Even`".
  * If odd, it prints "`<number> Is Odd`".
* If the input is invalid (not a number), it shows an error and asks again.

## Example Output


We To The Odd Or Even Checker✅
Enter A Number Or Type 0 To Exit 
5
5 Is Odd
Enter A Number Or Type 0 To Exit 
8
8 Is Even
Enter A Number Or Type 0 To Exit 
0
Goodbye!👋


## Code Example

python
def oddoreven():
    print("We To The Odd Or Even Checker✅")
    while True:
        try:
            num = int(input("Enter A Number Or Type 0 To Exit \n"))
            if num == 0:
                print("Goodbye!👋")
                break
            if num % 2 == 0:
                print(f"{num} Is Even")
            else:
                print(f"{num} Is Odd")
        except ValueError:
            print("Please enter A Valid Number👎")

oddoreven()


## How to Run

1. Save the code in a file called `odd_even_checker.py`.
2. Open a terminal or command prompt.
3. Run the program with:

   
   python odd_even_checker.py
   

## License

Free to use for educational and personal projects.

---
