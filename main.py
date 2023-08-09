import sys
from graph_challenge import graph_challenge
from string_challenge import string_challenge

def main():
    if len(sys.argv) < 3:
        print("Usage: python main.py graph|string 1|2")
        return

    function_selected = sys.argv[1]
    test_case_choice = sys.argv[2]

    if function_selected == 'graph':
        if test_case_choice == '1':
            result = graph_challenge(["(A,B,C)", "(B-A,C-B)", "(C,B,A)"])
            print("GraphChallenge Result:", result)
        elif test_case_choice == '2':
            result = graph_challenge(["(X,Y,Z,Q)", "(X-Y,Y-Q,Y-Z)", "(Z,Y,Q,X)"])
            print("GraphChallenge Result:", result)
        else:
            print("Invalid test case choice for GraphChallenge.")
    elif function_selected == 'string':
        if test_case_choice == '1':
            result = string_challenge("after badly")
            print("StringChallenge Result:", result)
        elif test_case_choice == '2':
            result = string_challenge("Laura sobs")
            print("StringChallenge Result:", result)
        else:
            print("Invalid test case choice for StringChallenge.")
    else:
        print("Invalid function choice. Please enter 'graph' or 'string'.")

if __name__ == "__main__":
    main()
