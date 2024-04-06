import webbrowser
import os

def read_text_file(text_file):
    with open(text_file) as file:
        lines = [line.strip() for line in file]
    return lines

def main():
    # change directory to the path where the script is run
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # read the clickables file content into a list
    links = read_text_file('clickables')
    # open each link into my default browser - this will be a lot of tabs!!!!
    for link in links:
        webbrowser.open(link)


if __name__ == "__main__":
    main()