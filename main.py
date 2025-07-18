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