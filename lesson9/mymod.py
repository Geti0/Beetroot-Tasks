
def count_lines(name):
    with open(name, 'r') as file:
        lines = file.readlines()
        return len(lines)

def count_chars(name):
    with open(name, 'r') as file:
        content = file.read()
        return len(content)

def test(name):
    lines = count_lines(name)
    chars = count_chars(name)
    print(f"Number of lines: {lines}")
    print(f"Number of characters: {chars}")

if __name__ == "__main__":
    # When the script is run directly, you can provide a filename as an argument.
    import sys
    if len(sys.argv) != 2:
        print("Usage: python mymod.py <filename>")
    else:
        filename = sys.argv[1]
        test(filename)


# Testing mymod interactively
import mymod

filename = "example.txt"  # Replace with your filename
mymod.test(filename)


# Testing mymod on itself
mymod.test("mymod.py")