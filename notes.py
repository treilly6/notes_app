import tkinter as tk
from datetime import datetime

class NotesApp:
    # initialize the instance
    def __init__(self):
        # create the window
        self.gui = tk.Tk()

        # set the title
        self.gui.title("Add Notes")

        # set dimensions of the window
        self.gui.geometry("700x350")

        # make the text box inside the window
        self.text_box = tk.Text(self.gui, height=350, width=700)

        # make the submit button
        self.button = tk.Button(self.gui, text="Submit", command=self.format_note_entry)

        # pack the button and the text box
        self.button.pack()
        self.text_box.pack()

        # start the program
        self.gui.mainloop()

    # get the content from the text_box
    def get_text_value(self):
        return self.text_box.get("1.0", "end-1c")

    # format the note
    def format_note_entry(self):
        # get the typed text
        text_content = self.get_text_value()
        # get the timestamp
        timestamp = self.get_date()
        # format the note
        note = timestamp + '\n' + text_content + '\n'
        # append to notes file
        self.append_to_file(note)
        # close the tkinter window
        self.gui.destroy()

    # get the timestamp for the note
    def get_date(self):
        now = datetime.now()
        return now.strftime("%m/%d/%Y %I:%M %p")

    # append the content to the file
    def append_to_file(self, note):
        notes_file = open("notes.txt", "a");

        print("HER IS THE CONTENT IN THE APPEND TO FILE TING")
        print(note)

        # append to the file
        notes_file.write("\n" + note)

        # close the file
        notes_file.close()

NotesApp()
