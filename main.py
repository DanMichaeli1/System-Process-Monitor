import Tkinter as tk
import ttk


class Gui(tk.Frame):
    def _init_(self, master=None):
        tk.Frame._init_(self, master)
        #self.parent = parent
        self.init_main()

    def init_main(self):
        toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file="new.gif")
        btn_open_dialog = tk.Button(toolbar, text=' New scan ', command=self.open_dialog, bg='#d7d8e0', bd=0,
                                    compound=tk.TOP, image=self.add_img)
        btn_open_dialog.pack(side=tk.LEFT)

        self.add_restart_img = tk.PhotoImage(file="new.gif")
        btn_restartButt = tk.Button(toolbar, text=' Restart ', bg='#d7d8e0', bd=0, compound=tk.TOP,
                                    image=self.add_restart_img)
        btn_restartButt.pack(side=tk.LEFT)

        self.add_pause_img = tk.PhotoImage(file="new.gif")
        self.pauseButt = tk.Button(toolbar, text=' Pause ', bg='#d7d8e0', bd=0, compound=tk.TOP,
                                   image=self.add_pause_img)
        self.pauseButt.pack(side=tk.LEFT, padx=0, pady=0)

        self.add_stop_img = tk.PhotoImage(file="new.gif")
        self.stopButt = tk.Button(toolbar, text=' Stop ', bg='#d7d8e0', bd=0, compound=tk.TOP, image=self.add_stop_img)
        self.stopButt.pack(side=tk.LEFT, padx=0, pady=0)

        self.add_save_img = tk.PhotoImage(file="new.gif")
        self.saveButt = tk.Button(toolbar, text=' Save ', bg='#d7d8e0', bd=0, compound=tk.TOP, image=self.add_save_img)
        self.saveButt.pack(side=tk.LEFT, padx=0, pady=0)

        self.tree = ttk.Treeview(self, columns=('Time', 'User', 'Name', 'PID', 'Path', 'Status'),
                                 height=10, show='headings')
        self.tree.column("Time", width=150, anchor=tk.CENTER)
        self.tree.column("User", width=200, anchor=tk.CENTER)
        self.tree.column("Name", width=200, anchor=tk.CENTER)
        self.tree.column("PID", width=100, anchor=tk.CENTER)
        self.tree.column("Path", width=100, anchor=tk.CENTER)
        self.tree.column("Status", width=100, anchor=tk.CENTER)

        self.tree.heading("Time", text='Time')
        self.tree.heading("User", text='User')
        self.tree.heading("Name", text='Name')
        self.tree.heading("PID", text='PID')
        self.tree.heading("Path", text='Path')
        self.tree.heading("Status", text='Status')

        self.tree.pack()

    @staticmethod
    def open_dialog():
        Child()


class Child(tk.Toplevel):
    def _init_(self):
        tk.Toplevel._init_(self, root)
        self.init_child()

    def init_child(self):
        self.title('New Scan Parameters')
        self.geometry('400x220+320+130')
        self.resizable(False, False)

        label_description = tk.Label(self, text='Save logs to: ')
        label_description.place(x=50, y=50)
        label_sum = tk.Label(self, text='Update Interval (sec):')
        label_sum.place(x=50, y=80)

        self.entry_description = ttk.Entry(self)
        self.entry_description.place(x=200, y=50)
        self.entry_description.winfo_toplevel()

        self.entry_interval = ttk.Entry(self)
        self.entry_interval.place(x=200, y=80)
        self.entry_interval.winfo_toplevel()

        btn_ok = ttk.Button(self, text='Start')
        btn_ok.place(x=170, y=150)
        btn_ok.bind('<Button-1>')

        self.grab_set()
        self.focus_set()


#if __name__ == "__main__":
root = tk.Tk()
app = Gui(root)
app.pack()
root.title("Process Scanner")
root.geometry("1000x450+50+50")
root.resizable(True, True)
root.mainloop()
