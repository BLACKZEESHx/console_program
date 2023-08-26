import pyfiglet
import write_like_gpt

# Ask the user to enter some text
text = input("Enter some text: ")

# Use pyfiglet to convert the text to ASCII art
ascii_art = pyfiglet.figlet_format(text)
# typing the ASCII art to the console
write_like_gpt.write(ascii_art)
