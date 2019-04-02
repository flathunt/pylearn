#!/usr/local/bin/python

import os
import sqlite3
from tkinter import *
from tkinter import font
from tkinter import ttk
from tkinter.filedialog import askopenfilename, asksaveasfile
from tkinter.scrolledtext import ScrolledText

# v0.4 - 10/08/2016 - no predefined db or query (explorer04)
# v0.3 - 11/07/2016 - Added script open/save (explorer03)
# v0.2 - 11/07/2016 - Use PRAGMA table_info() to get column information (explorer02)
# v0.1 (Ahem) - 06/2016  - Removed zooming menu options (explorer01)
# v0.1 - Initial version (explorer)


class Application(Frame):
    def __init__(self, master=None):
        """
        Create the top level frame and standard fonts...
        """
        super().__init__(master)

        master.columnconfigure(0, weight=1)
        master.rowconfigure(0, weight=1)
        self.grid(sticky=(N, E, S, W))

        self.database = None

        # Define standard sizes and fonts...

        self.RHS_WIDTH = 600
        self.LHS_WIDTH = 200
        self.TOP_HEIGHT = 300
        self.BOTTOM_HEIGHT = 300
        self.WIDTH = self.RHS_WIDTH + self.LHS_WIDTH
        self.HEIGHT = self.TOP_HEIGHT + self.BOTTOM_HEIGHT

        self.size = 10
        self.normal = font.Font(family='Arial', size=self.size)
        self.bold = font.Font(family='Arial', size=self.size, weight='bold')
        self.normal_fixed = font.Font(family='Courier New', size=self.size)
        self.bold_fixed = font.Font(family='Courier New', size=self.size, weight='bold')

        # Set up the UI...

        self.create_ui()
        self.create_menus(master)
        self.define_hot_keys(master)

        # self.build_database_tree()

    # noinspection PyAttributeOutsideInit
    def create_ui(self):
        """
        Set up the basic GUI components...
        """

        # Main container frames...

        self.tree_frame = Frame(self, width=self.LHS_WIDTH, height=self.HEIGHT)
        self.query_frame = Frame(self, width=self.RHS_WIDTH, height=self.TOP_HEIGHT)
        self.result_holding_frame = Frame(self, width=self.RHS_WIDTH, height=self.BOTTOM_HEIGHT)

        self.tree_frame.grid(row=0, column=0, rowspan=2, sticky=(N, E, S, W))
        self.query_frame.grid(row=0, column=1, sticky=(N, E, S, W))
        self.result_holding_frame.grid(row=1, column=1, sticky=(N, E, S, W))

        self.rowconfigure(0, weight=1, minsize=100)
        self.rowconfigure(1, weight=1, minsize=100)
        self.columnconfigure(0, weight=1, minsize=100)
        self.columnconfigure(1, weight=1, minsize=400)

        # Treeview database listing area...

        self.db_tree = ttk.Treeview(self.tree_frame, height=25)
        self.db_tree.grid(sticky=(N, E, S, W))

        # Query input area and run button...

        self.query_text = ScrolledText(self.query_frame, font=self.normal_fixed, width=75, height=14)
        # self.query_text.insert('1.0', 'select * from customers')
        self.query_text.grid(row=0, column=0, sticky=(N, E, S, W))

        self.query_button = Button(self.query_frame, text='Run', command=self.run_query, font=self.normal)
        self.query_button.grid(row=1, column=0)

        # Query result area...

        self.result_canvas = Canvas(self.result_holding_frame, width=self.RHS_WIDTH)
        self.result_frame = Frame(self.result_canvas)

        self.vsb = Scrollbar(self.result_holding_frame, orient="vertical", command=self.result_canvas.yview)
        self.hsb = Scrollbar(self.result_holding_frame, orient="horizontal", command=self.result_canvas.xview)
        self.result_canvas.configure(yscrollcommand=self.vsb.set)
        self.result_canvas.configure(xscrollcommand=self.hsb.set)

        self.result_canvas.grid(row=0, column=0, sticky=(N, E, S, W))
        self.vsb.grid(row=0, column=1, sticky=(N, S))
        self.hsb.grid(row=1, column=0, sticky=(E, W))
        self.result_canvas.create_window((4, 4), window=self.result_frame, anchor="nw", tags="self.result_frame")
        self.result_frame.bind("<Configure>", self.on_frame_configure)

    def on_frame_configure(self, event):
        """
        Reset the scroll region to encompass the inner frame
        """
        self.result_canvas.configure(scrollregion=self.result_canvas.bbox("all"))

    def create_menus(self, master):
        """
        Set up the menus...
        :param master:
        """
        menu_bar = Menu(master, border=0)
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Open database...", font=self.normal, command=self.get_database_name)
        file_menu.add_command(label="Open SQL script...", font=self.normal, command=self.open_script_file)
        file_menu.add_command(label="Save...", font=self.normal, command=self.save_script_file)
        file_menu.add_command(label="Exit", font=self.normal, command=lambda: root.destroy())
        menu_bar.add_cascade(label='File', font=self.normal, menu=file_menu)

        query_menu = Menu(menu_bar, tearoff=0)
        query_menu.add_command(label="Run", font=self.normal, command=self.run_query, accelerator='F5')
        menu_bar.add_cascade(label='Query', font=self.normal, menu=query_menu)

        master.config(menu=menu_bar)

    def define_hot_keys(self, master):
        """
        Set up the hot keys...
        """
        master.bind_all("<F5>", lambda x: self.run_query())

    def zoom(self, diff):
        """
        Change font size
        :param diff: amount to vary or 0 to reset
        """
        if diff:
            self.size += diff
        else:
            self.size = 10

        self.normal.configure(size=self.size)
        self.bold.configure(size=self.size)
        self.normal_fixed.configure(size=self.size)
        self.bold_fixed.configure(size=self.size)

    def get_database_name(self):
        """
        Allow the user to select a database...
        """
        name = askopenfilename(initialdir=".", title="choose your SQLite DB file",
                               filetypes=(("SQLite files", "*.db"), ("all files", "*.*")))

        if name is not None:
            self.database = name
            self.build_database_tree()

    def open_script_file(self):
        """
        Allow the user to select an SQL script...
        """
        name = askopenfilename(initialdir=".", title="choose your SQL script file",
                               filetypes=(("SQL files", "*.sql"), ("all files", "*.*")))

        if name is not None:
            with open (name, "r") as script_file:
                data=script_file.read()
                self.query_text.delete('1.0', END)
                self.query_text.insert('1.0', data)
 
    def save_script_file(self):
        """
        Allow the user to save an SQL script...
        """
        outfh = asksaveasfile(mode='w', initialdir=".", title="Save...",
                               filetypes=(("SQL files", "*.sql"), 
                               ("all files", "*.*")))
                               
        outfh.write(self.query_text.get('1.0', END))
        outfh.close()        
                
    def open_database(self):
        """
        Open the database file - if it exists
        :return: database object
        """
        if not os.path.isfile(self.database):
            Label(self.result_frame, text='No such database:' + self.database, font=self.normal_fixed, fg='red'). \
                grid(row=0, column=0, sticky=W)
            return None

        db = sqlite3.connect(self.database)
        return db

    # noinspection PyAttributeOutsideInit
    def build_database_tree(self):
        """
        Create a Treeview structure of database information...
        """
        self.clear_results()
        self.db_tree.delete(*self.db_tree.get_children())

        self.top = self.db_tree.insert('', 0, text=os.path.basename(self.database))

        db = self.open_database()
        cur = db.cursor()
        cur2 = db.cursor()

        query = """
            SELECT name
            FROM sqlite_master
            WHERE type = 'table'
        """

        cur.execute(query)
        for row in cur:
            table_name = row[0]
            table_node = self.db_tree.insert(self.top, END, text=table_name)
            cur2.execute("PRAGMA table_info(" + table_name + ")")
            for column_metadata in cur2:
                column_display = column_metadata[1] + '   ' + column_metadata[2]
                if column_metadata[5]:
                    column_display += ' (PK)'
                self.db_tree.insert(table_node, END, text=column_display)

    def clear_results(self):
        """
        Empty the results before running a new query...
        :return:
        """
        for widget in self.result_frame.winfo_children():
            widget.destroy()

    def run_query(self):
        """
        Run a query and display the results...
        :return:
        """
        self.clear_results()
        db = self.open_database()

        cur = db.cursor()
        query = self.query_text.get('1.0', END)

        try:
            cur.execute(query)
        except (sqlite3.OperationalError, sqlite3.Warning) as e:
            Label(self.result_frame, text=', '.join(e.args), font=self.normal_fixed, fg='red'). \
                grid(row=0, column=0, sticky=W)
        else:
            for i, column_name in enumerate([col[0] for col in cur.description], start=1):
                Label(self.result_frame, text=column_name, font=self.bold_fixed, borderwidth=4). \
                    grid(row=0, column=i, sticky=W)

            for i, row in enumerate(cur, start=1):
                Label(self.result_frame, text=str(i)+'.', font=self.bold_fixed, borderwidth=4). \
                    grid(row=i, column=0, sticky=W)
                for j, field in enumerate(row, start=1):
                    if field is None:
                        field = '[NULL]'

                    stickiness = E if isinstance(field, int) or isinstance(field, float) else W
                    Label(self.result_frame, text=field, font=self.normal_fixed, borderwidth=4). \
                        grid(row=i, column=j, sticky=stickiness)


# =====================================================================
#  Main processing...
# =====================================================================

root = Tk()
root.title('PySQLiteExplorer (v0.4)')
img = PhotoImage(file='browser.gif')
root.iconphoto(True, img)

app = Application(master=root)
app.mainloop()
