import tkinter as tk
from datetime import datetime

class NotesApp:
    # initialize the instance
    def __init__(self):
        print("In the __init__")
        # create the window
        self.gui = tk.Tk()

        # set the title
        self.gui.title("Add Notes")

        # set dimensions of the window
        self.gui.geometry("700x350")

        # make the text box inside the window
        self.text_box = tk.Text(self.gui, height=350, width=700)

        # make the submit button
        self.button = tk.Button(self.gui, text="Add Note", command=self.format_note_entry)

        # pack the button and the text box
        self.button.pack()
        self.text_box.pack()

        # start the program
        self.gui.mainloop()

    # get the content from the text_box
    def get_text_value(self):
        print("In the get text value")
        return self.text_box.get("1.0", "end-1c")

    # format the note
    def format_note_entry(self):
        print("In format note entry")
        # get the typed text
        text_content = self.get_text_value()

        # get the timestamp
        timestamp = self.get_date()

        # format the note
        note = timestamp + '\n' + text_content + '\n'

        # append to notes file
        self.append_to_file(note)

        # clear the text box
        self.clear_text_box()

    # method for clearing the text box
    def clear_text_box(self):
        print("clearing the text box")
        self.text_box.delete("1.0", "end-1c")

    # get the timestamp for the note
    def get_date(self):
        print("getting the date")
        now = datetime.now()
        return now.strftime("%m/%d/%Y %I:%M %p")

    # append the content to the file
    def append_to_file(self, note):
        print("In append to file function")

        # open the note file
        notes_file = open("notes.txt", "a");

        # append to the file
        notes_file.write("\n" + note)

        # close the file
        notes_file.close()

print("About to initiate the NotesApp")
NotesApp()
