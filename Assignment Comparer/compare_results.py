def main():
    nausher = open("nausher_data.txt", 'r').readlines();
    chandler = open("chandler_data.txt", 'r').readlines();
    results = open("results.txt", 'w');
    if(len(nausher) != len(chandler)):
        print("OUTPUT FILES ARE DIFFERENT SIZES!");
        print("OUTPUT FILES ARE DIFFERENT SIZES!", file = results);

    else:
        print("OUTPUT FILES ARE THE SAME SIZES :D");
        print("OUTPUT FILES ARE THE SAME SIZES :D", file = results);

    i = 0;
    length = max(len(nausher), len(chandler));
    differences = 0;
    while(i < length):
        n = nausher[i] if i < len(nausher) else None;
        c = chandler[i] if i < len(chandler) else None;
        if(c == None):
            print(f"Line #{i+1}:", file = results);
            print(f"   Nausher: {n}", file = results);
            print(f"   Chandler: Missing?!?!?!", file = results);
            print("="*100, file = results);
            print("\n\n", file = results);
            differences += 1;

        elif(n == None):
            print(f"Line #{i+1}:", file = results);
            print(f"   Nausher:  Missing?!?!?!", file = results);
            print(f"   Chandler:{c}", file = results);
            print("="*100, file = results);
            print("\n\n", file = results);
            differences += 1;

        elif(n != c):
            print(f"Line #{i+1}:", file = results);
            print(f"   Nausher: {n}", file = results);
            print(f"   Chandler: {c}", file = results);
            print("="*100, file = results);
            print("\n\n", file = results);
            differences += 1;

        i += 1;

    print(f"Found {differences} differences!");
    print(f"Found {differences} differences!", file = results);
    print("Done");

if(__name__ == "__main__"):
    main();