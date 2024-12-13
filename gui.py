from tkinter import ttk
import tkinter as tk
import voter_id_handler as logic


class Gui:
    def __init__(self, master) -> None:
        """
        initializes the GUI
        """
        self.master = master
        self.master.title('Dominion Voting Machine')
        self.master.geometry('300x300')

        self.id_label = ttk.Label(master, text='Voter ID')
        self.id_label.pack()

        self.input_var = tk.StringVar()

        self.input_id = ttk.Entry(master, width=40)
        self.input_id.pack(pady=5)

        self.guide_label = ttk.Label(master, text='ENTER VALID VOTER ID')
        self.guide_label.pack(pady=5)

        self.submit_button1 = ttk.Button(master, text='Submit', command=self.submit)
        self.submit_button1.pack(pady=5)

        self.selected_option = tk.StringVar()

        self.radio1 = tk.Radiobutton(master, text='John McCain', variable=self.selected_option, value='John McCain')
        self.radio1.pack(pady=20)

        self.radio2 = tk.Radiobutton(master, text='Barrack Obama', variable=self.selected_option, value='Barrack Obama')
        self.radio2.pack(pady=10)

        self.selected_option.set('Neither')

        self.count_label_mccain = ttk.Label(master, text=f'McCain: {logic.count()[0]}')
        self.count_label_mccain.pack()

        self.count_label_obama = ttk.Label(master, text=f'Obama: {logic.count()[1]}')
        self.count_label_obama.pack()

    def count_update(self) -> None:
        """
        Updates candidate count labels in GUI
        """
        self.count_label_mccain.config(text=f'McCain: {logic.count()[0]}')
        self.count_label_obama.config(text=f'Obama: {logic.count()[1]}')

    def warning(self) -> None:
        """
        Changes guide label to alert user that duplicate voter ID was entered
        """
        self.guide_label.config(foreground='red')
        self.guide_label.config(text='VOTER FRAUD DETECTED')

    def un_warning(self) -> None:
        """
        Changes guide label to inform user that ID and vote was accepted
        """
        self.guide_label.config(foreground="green")
        self.guide_label.config(text='VOTER ID ACCEPTED')

    def incorrect_input(self) -> None:
        """
        Changes guide label to alert user that input was not accepted due to being non-numeric
        """
        self.guide_label.config(foreground='red')
        self.guide_label.config(text='ENTER NUMERICAL ID')

    def no_selection(self) -> None:
        """
        Changes guide label to alert user that no input was found for candidate radio buttons
        """
        self.guide_label.config(foreground='red')
        self.guide_label.config(text='SELECT A CANDIDATE')

    def reset_fields(self) -> None:
        """
        Clears Voter ID field and candidate radio buttons, and resets guide label text.
        Deprecated.
        """
        self.guide_label.config(foreground='black')
        self.guide_label.config(text='ENTER VALID VOTER ID')
        self.selected_option.set('Neither')
        self.input_var.set('')

    def submit(self) -> None:
        """
        Takes user input and passes it to
        voter_id_handler.py
        """
        user_input = self.input_id.get()
        vote = self.selected_option.get()
        print(f'User input: {user_input}')
        logic.submit_logic(user_input, vote, self.warning, self.un_warning, self.incorrect_input,
                           self.no_selection, self.count_update)

