# writing my own functions
# Jeffrey Smith

def header(text, surround):
    length = len(text) + 4
     # surround = "*"
     # text = "Hello, World!"
    print(surround * length)
    print(surround, text, surround)
    print(surround * length)

def main():
    header("Hello, World!", "*")
    header("Python Rocks!", "!")
    header("TEE PEE FOR MY BUNGHOLE!", "@")
    header("Happy Birthday, Mauna", "#")

main()


