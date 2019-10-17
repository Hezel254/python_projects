command=""

while True:
    started=False
    command = input(">>> ").lower()
    if command == "start":
        if started:
         print("Car is already started...what's up?")
        else:
            print("Car started...ready to go!")
    if command == "stop":
        if not started:
            print("Car stopped...")
        else:
                print("Heey! Car is already stopped")
    if command == "help":
        print("""
        start-> To start the Car
        stop-> To stop the Car
        quit-> To quit the process
        """
        )
        break
else:
    print(" Sorry the operation is unidentified!")