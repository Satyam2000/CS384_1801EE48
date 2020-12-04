#A Python project to Make Notepad using Tkinter .......
# Group members:-
                 #Satyam Kumar (1801EE48)
                 #Kishan Kumar singh (1801EE22).
import pathlib
import datetime
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from tkinter import Event, font as tkfont
from tkinter import filedialog, messagebox


class Notepad(tk.Tk):
    """A notepad application"""

    def __init__(self):
        super().__init__()
        self.withdraw()

        #this is how to check platform & set zoom status
        platform = self.tk.call('tk', 'windowingsystem')
        self.wm_state('zoomed') if platform == 'win32' else self.attributes(
            '-zoomed', 1)

        # code for naming file and about file variables.
        self.file = pathlib.Path.cwd() / 'Untitled_notepad.txt'
        self.file_defaults = {
            'defaultextension': '*',
            'filetypes': [('All Files', '.*')]}

        # code to find,search and replace variables
        self.query = None
        self.matches = None
        self.findnext = None
        self.findreplace = None

        # code to do main menu setup
        self.menu = tk.Menu(self)
        self.configure(menu=self.menu)
        self.menu_file = tk.Menu(self.menu, tearoff=False)
        self.menu_edit = tk.Menu(self.menu, tearoff=False)
        

    # file menu looks like
        #To open a new file
        self.menu_file.add_command(label='New', accelerator='Ctrl+N', command=self.new_file)
        #To open already existing file.
        self.menu_file.add_command(label='Open...', accelerator='Ctrl+O', command=self.open_file)
        #To save the current file
        self.menu_file.add_command(label='Save', accelerator='Ctrl+S', command=self.save_file)
        #To save an existing file under new name 
        self.menu_file.add_command(label='Save As...', accelerator='Ctrl+Shift+S', command=self.save_file_as)
		#To Exit current file or loation.
        self.menu_file.add_command(label='Exit', accelerator='Alt+F4', command=self.quit_App)


        # edit menu looks like
        
        #To give a Feature of undo and Redo.
        self.menu_edit.add_command(label='Redo', accelerator='Ctrl+Y', command=self.undo_edit)
        self.menu_edit.add_command(label='Undo', accelerator='Ctrl+Z', command=self.redo_edit)
        #To give a feature of cut,copy and Paste.
        self.menu_edit.add_command(label='Cut', accelerator='Ctrl+X', command=self.text_cut)
        self.menu_edit.add_command(label='Copy', accelerator='Ctrl+C', command=self.text_copy)
        self.menu_edit.add_command(label='Paste', accelerator='Ctrl+V', command=self.text_paste)
        #To give the feature of finding something and/or replacing it.
        self.menu_edit.add_command(label='Find', accelerator='Ctrl+F', command=self.ask_find_next)
        self.menu_edit.add_command(label='Find and Replace', accelerator='Ctrl+H', command=self.ask_find_replace)
        #To get the current time and date at the begining of cursor.
        self.menu_edit.add_command(label='Time/Date', accelerator='F5', command=self.get_datetime)

    
        # code to add cascading menus to main menu
        self.menu.add_cascade(label='File', menu=self.menu_file)
        self.menu.add_cascade(label='Edit', menu=self.menu_edit)
       

        # how to setup  text widget
        self.text_frame = tk.Frame(self)
        self.text = ScrolledText(self.text_frame, wrap=tk.WORD, font='-size 20', undo=True, maxundo=10,
                                 autoseparator=True, blockcursor=False, padx=5, pady=10)

        # set default tab size to 4 characters
        self.font = tkfont.Font(family='Courier New', size=12, weight=tkfont.NORMAL,
                                slant=tkfont.ROMAN, underline=False, overstrike=False)
        self.text.configure(font=self.font)
        tab_width = self.font.measure(' ' * 4)
        self.text.configure(tabs=(tab_width,))
        self.text.insert(tk.END, self.file.read_text()
                         if self.file.is_file() else '')

        # packing up all widget to screen
        self.text.pack(fill=tk.BOTH, expand=tk.YES)
        self.text_frame.pack(fill=tk.BOTH, expand=tk.YES)

        # adding up status bar
        self.status_bar = StatusBar(self, self.text)

        # this is the final setup
        self.update_title()

        #self.eval('tk::PlaceWindow . center')
        self.deiconify()

    # -------------defining FILE MENU starts--------------------------------------

    def new_file(self, event=None):
        """Create a new file"""
        # check for content change before opening new file
        self.confirm_changes()

        # reset text widget
        self.text.delete(1.0, tk.END)
        self.file = pathlib.Path.cwd() / 'Untitled_notepad.txt'
        self.update_title()

    def open_file(self, event=None):
        """Open an existing file"""
        # check for content change before opening new file
        self.confirm_changes()

        # open new file
        file = filedialog.askopenfilename(
            initialdir=self.file.parent, **self.file_defaults)
        if file:
            self.text.delete(1.0, tk.END)  # delete existing content
            self.file = pathlib.Path(file)
            self.text.insert(tk.END, self.file.read_text())
            self.update_title()
            self.status_bar.update_status()

    def save_file(self, event=None):
        """Save the currently open file"""
        if self.file.name == 'Untitled_notepad.txt':
            file = filedialog.asksaveasfilename(
                initialfile=self.file, **self.file_defaults)
            self.file = pathlib.Path(file) if file else self.file
        self.file.write_text(self.text.get(1.0, tk.END))
        self.update_title()

    def save_file_as(self, event=None):
        """Save the currently open file with a different name or location"""
        file = filedialog.asksaveasfilename(
            initialdir=self.file.parent, **self.file_defaults)
        if file:
            self.file = pathlib.Path(file)
            self.file.write_text(self.text.get(1.0, tk.END))
            self.update_title()


    def confirm_changes(self):
        """Check to see if content has changed from original file; if so, confirm save"""
        if self.file.is_file():
            original = self.file.read_text()
            current = self.text.get(1.0, tk.END)
            if original != current:
                confirm = messagebox.askyesno(
                    message="Save current file changes?")
                if confirm:
                    self.save_file()
        # new unsaved document with content is prompted to save
        elif self.text.count(1.0, tk.END)[0] > 1:
            confirm = messagebox.askyesno(message="Save current document?")
            if confirm:
                self.save_file()

    def update_title(self):
        """Update the title with the file name"""
        self.title(self.file.name + " - Notepad")

    def quit_App(self):
        """Quit application after checking for user changes"""
        self.confirm_changes()
        self.destroy()

#-----------------FILE Menu definition Ends--------------------------------

#-----------------EDIT MENU definition starts------------------------------

    def undo_edit(self):
        """Undo the last edit in the stack"""
        try:
            self.text.edit_undo()
        except tk.TclError:
            pass

    def redo_edit(self):
        """Redo the last edit in the stack"""
        try:
            self.text.edit_redo()
        except tk.TclError:
            pass

    def text_copy(self):
        """Append selected text to the clipboard"""
        selected = self.text.get(tk.SEL_FIRST, tk.SEL_LAST)
        self.text.clipboard_clear()
        self.text.clipboard_append(selected)

    def text_paste(self):
        """Paste clipboard text into text widget at cursor"""
        self.text.insert(tk.INSERT, self.text.clipboard_get())

    def text_cut(self):
        """Cut selected text and append to clipboard"""
        selected = self.text.get(tk.SEL_FIRST, tk.SEL_LAST)
        self.text.delete(tk.SEL_FIRST, tk.SEL_LAST)
        self.text.clipboard_clear()
        self.text.clipboard_append(selected)

    def quit_application(self, event=None):
        """Quit application after checking for user changes"""
        self.confirm_changes()
        self.destroy()

    def ask_find_next(self, event=None):
        """Create find next popup widget"""
        self.findnext = Find(self, self.text)

    def ask_find_replace(self, event=None):
        """Create replace popup widget"""
        self.findreplace = Replace(self, self.text)

    def get_datetime(self, event=None):
        """insert date and time at cursor position"""
        self.text.insert(tk.INSERT, datetime.datetime.now().strftime("%c"))

#-----------------EDIT Menu definition ends---------------------------------
