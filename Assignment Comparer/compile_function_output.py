from Connect import Connect;
import functions;

def main():
    conn = Connect("dcris.txt");
    cursor = conn.cursor;
    if(input("A - Nausher\nB - Chandler\nWho's testing the file?: ").lower() == "A"):
        fileName = "nausher_data.txt";
    else: fileName = "chandler_data.txt";

    f = open(fileName, 'w');
    for x in dir(functions).reverse():
        func = getattr(functions, x);
        if(callable(func)):
            thisFunction = True;
            i = 1;
            while(thisFunction):
                print("="*100);
                print(f"Function call #{i}, Parameters for {func} ");    
                params = get_params();

                print("="*100, file=f);
                print(f"Testing {func}() with parameters={params}", file=f);
                for row in func(cursor, *params):
                    print(row, file=f);
            
                print("\n", file = f);
                print("="*100, file = f);

                thisFunction = input("Done with this function? (Y/N): ") == "N";
                i += 1;
            
    print("Done");

def get_params():
    params = [];
    gettingData = True;
    i = 1;
    while(gettingData):
        param_in = input(f"Input Parameter {i}: ");
        if(param_in == "stop"):
            gettingData = False;

        else: params.append(param_in);
        i += 1;

    return params;

if(__name__ == "__main__"):
    main();

