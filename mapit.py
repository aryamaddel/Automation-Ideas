import pyperclip
import sys
import webbrowser

# Automation to search a address in google maps using command-line
if len(sys.argv) > 1:
    address = " ".join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open(f"https://www.google.co.in/maps/place/{address}")
# Run the file through command line and enter a address as parameter
# If address is copied to the clipboard then simply run the file
