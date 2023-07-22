# multiline.py
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        argument = " ".join(sys.argv[1:])
        print("Received argument:", argument)
    else:
        print("No argument provided.")
