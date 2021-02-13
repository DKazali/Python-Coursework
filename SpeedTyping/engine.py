from generator import *
from verification import *
from tkinter import *
import time


class Engine:
    V = Verification()              # С тази променлива можем да ползваме методите и променливите от класа Verification
    G = Generator()                 # С тази променлива можем да ползваме методите и променливите от класа Generator
    rW = None                       # rW = Random Word, на тази промелнива се задава стойност - случайно генерирана дума
    uW = None                       # uW = User Word, тук се записва въведената дума от потребителя
    tStart = None                   # tStart = Timer Start, тук запазваме времето на започване на въвеждане на думата
    tFinish = None                  # tFinish = Timer Finish, тук запазваме времето на приключване на писането на думата
    fastestType = None              # Най-доброто постигнато време
    fastestWord = None              # Думата с която сме постигнали най-доброто време
    ET = None                       # Времето за което сме въвели последната показана дума
    ET_formatted = None             # ЕТ но форматирана до втория знак след запетаята
    total_time = 0                  # Общото ни време което сме прекарали в писане
    words_typed = 0                 # брой на написаните думи
    x = 0                           # Променлива нужна за работата на Радио бутоните
    mode = None                     # Служи за смяна на нивото на трудност
    avrg_time = 0                   # Средно време на писане на дума
    window = None                   # За създаването на прозореца
    tt_f = None                     # TotalTime но форматирана
    at_f = None                     # AverageTime форматирана
    rb_easy = None
    rb_normal = None
    rb_hard = None
    rb_extreme = None
    btn1 = None
    btn2 = None
    label = None
    label2 = None
    label3 = None
    label4 = None
    label5 = None
    label6 = None
    label7 = None
    label8 = None
    label9 = None
    label10 = None
    u_entry = None
    ftf = None                      # FastestType форматирана
    Lost = False                    # Без нея излиза грешка за btn2 в main_frame
    Win_created = False             # Служи за да не се създава нов прозорец многократно

    def to_mainframe(self, event):
        if self.mode is None:
            self.rb_n("<ButtonPress event num=1 x=52 y=12>")
        self.rb_easy.destroy()
        self.rb_normal.destroy()
        self.rb_hard.destroy()
        self.rb_extreme.destroy()
        self.rb_easy = None
        self.rb_normal = None
        self.rb_hard = None
        self.rb_extreme = None
        self.btn1.destroy()
        self.btn1 = None
        self.btn2 = Button(self.window, text="Finish", fg='black')
        self.btn2.place(x=128, y=270)
        self.label2 = Label(self.window, text="You typed the word in: ", fg='black', font=("Times New Roman", 12))
        self.label2.place(x=5, y=165)
        self.label3 = Label(self.window, text="  :  ", fg='black', font=("Times New Roman", 12))
        self.label3.place(x=150, y=165)
        self.label4 = Label(self.window, text="seconds", fg='black', font=("Times New Roman", 12))
        self.label4.place(x=190, y=165)
        self.label5 = Label(self.window, text="Current Best Time:", fg='black', font=("Times New Roman", 12))
        self.label5.place(x=5, y=185)
        self.label6 = Label(self.window, text="  :  ", fg='black', font=("Times New Roman", 12))
        self.label6.place(x=125, y=185)
        self.label8 = Label(self.window, text="seconds", fg='black', font=("Times New Roman", 12))
        self.label8.place(x=165, y=185)
        self.label9 = Label(self.window, text="with the word:", fg='black', font=("Times New Roman", 12))
        self.label9.place(x=5, y=205)
        self.label7 = Label(self.window, text="     ", fg='black', font=("Times New Roman", 12))
        self.label7.place(x=95, y=205)
        self.u_entry = Entry(self.window)
        self.u_entry.place(x=75, y=120)
        self.Lost = False
        self.main_frame()

    def to_stats(self, event):
        self.u_entry.destroy()
        self.label.config(text="Total time in seconds:", font=("Times New Roman", 12))
        self.label.place(x=10, y=10)
        self.tt_f = "{:.2f}".format(self.total_time)
        self.label2.config(text=self.tt_f)
        self.label2.place(x=145, y=10)
        self.label3.config(text="Average Time in seconds:")
        self.label3.place(x=10, y=35)
        self.at_f = "{:.2f}".format(self.avrg_time)
        self.label4.config(text=self.at_f)
        self.label4.place(x=170, y=35)
        self.label5.config(text="Best time in seconds:")
        self.label5.place(x=10, y=60)
        if self.fastestType is None:
            self.fastestType = 0
            self.fastestWord = "    "
        self.ftf = "{:.2f}".format(self.fastestType)
        self.label6.config(text=self.ftf)
        self.label6.place(x=145, y=60)
        self.label7.config(text="With the word:")
        self.label7.place(x=10, y=85)
        self.label8.config(text=self.fastestWord)
        self.label8.place(x=105, y=85)
        self.label9.config(text="Total mistakes made:")
        self.label9.place(x=10, y=110)
        self.label10 = Label(self.window, text=self.V.attempts, fg='black', font=("Times New Roman", 12))
        self.label10.place(x=145, y=110)
        self.btn1 = Button(self.window, text="Quit", fg='black')
        self.btn1.place(x=255, y=270)
        self.btn2.config(text="To Mode Selection")
        self.btn2.place(x=10, y=270)
        self.V.reset_attempts()
        self.stats()

    def to_mode_selection(self, event):
        self.window.destroy()
        self.Win_created = False
        self.window = None
        self.tt_f = None
        self.at_f = None
        self.rb_easy = None
        self.rb_normal = None
        self.rb_hard = None
        self.rb_extreme = None
        self.btn1 = None
        self.btn2 = None
        self.label = None
        self.label2 = None
        self.label3 = None
        self.label4 = None
        self.label5 = None
        self.label6 = None
        self.label7 = None
        self.label8 = None
        self.label9 = None
        self.label10 = None
        self.u_entry = None
        self.rW = None
        self.uW = None
        self.tStart = None
        self.tFinish = None
        self.fastestType = None
        self.fastestWord = None
        self.ET = None
        self.ET_formatted = None
        self.total_time = 0
        self.avrg_time = 0
        self.fastestType = None
        self.fastestWord = None
        self.V.reset_attempts()
        self.start()

    def exit_app(self, event):
        self.Win_created = False
        self.window.destroy()

    def stats(self):
        self.btn2.bind('<Button-1>', self.to_mode_selection)
        self.btn1.bind('<Button-1>', self.exit_app)
        self.window.mainloop()

    def get_entry(self, event):
        self.uW = self.u_entry.get()
        self.u_entry.delete(0, 'end')
        self.main_frame()

    def rb_e(self, event):
        self.mode = 'Easy'
        self.V.set_mode(self.mode)

    def rb_n(self, event):
        self.mode = 'Normal'
        self.V.set_mode(self.mode)

    def rb_h(self, event):
        self.mode = 'Hard'
        self.V.set_mode(self.mode)

    def rb_x(self, event):
        self.mode = 'Extreme'
        self.V.set_mode(self.mode)

    def start(self):
        if self.Win_created is False:
            self.window = Tk()
            self.window.title("SpeedTyping")
            self.window.geometry("300x300")
            self.Win_created = True

        self.label = Label(self.window, text="Select Mode: ", fg='black', font=("Times New Roman", 18))
        self.label.place(x=80, y=20)

        self.rb_easy = Radiobutton(self.window, text="Easy", variable=self.x, value=1)
        self.rb_easy.place(x=80, y=60)

        self.rb_normal = Radiobutton(self.window, text="Normal", variable=self.x, value=2)
        self.rb_normal.place(x=80, y=80)
        self.rb_normal.select()

        self.rb_hard = Radiobutton(self.window, text="Hard", variable=self.x, value=3)
        self.rb_hard.place(x=80, y=100)

        self.rb_extreme = Radiobutton(self.window, text="Extreme", variable=self.x, value=4)
        self.rb_extreme.place(x=80, y=120)

        self.btn1 = Button(self.window, text="Start", fg='black')
        self.btn1.place(x=132, y=250)

        self.rW = None

        if self.mode is not None:
            self.mode = None

        self.mode_selection()

    def main_frame(self):
        if self.rW is None:
            self.rW = self.G.generate()
            self.label.config(text=self.rW)

        if self.rW is not None and self.tStart is None:
            self.tStart = time.perf_counter()

        self.u_entry.bind('<Return>', self.get_entry)

        if self.rW is not None and self.uW is not None:
            if self.V.ver(self.rW, self.uW):
                self.tFinish = time.perf_counter()
                self.ET = self.tFinish - self.tStart
                self.ET_formatted = "{:.2f}".format(self.ET)
                self.label3.config(text=self.ET_formatted)
                if self.fastestType is None:
                    self.fastestType = self.ET
                    self.fastestWord = self.rW

                self.ftf = "{:.2f}".format(self.fastestType)
                if self.ET_formatted < self.ftf:
                    self.fastestType = self.ET
                    self.fastestWord = self.rW

                self.ftf = "{:.2f}".format(self.fastestType)
                self.label6.config(text=self.ftf)
                self.label7.config(text=self.fastestWord)
                self.rW = self.G.generate()
                self.label.config(text=self.rW)
                self.total_time += self.ET
                self.words_typed += 1
                self.avrg_time = self.total_time / self.words_typed
                self.tStart = None
                self.tFinish = None
                if self.rW is not None and self.tStart is None:
                    self.tStart = time.perf_counter()
            if self.V.n_attempts() == 'Lose':
                self.V.win_lose = None
                self.Lost = True
                self.to_stats("<ButtonPress event num=1 x=13 y=10>")
        if self.Lost is False:
            self.btn2.bind('<Button-1>', self.to_stats)
        self.window.mainloop()

    def mode_selection(self):
        self.btn1.bind('<Button-1>', self.to_mainframe)
        self.rb_easy.bind('<Button-1>', self.rb_e)
        self.rb_normal.bind('<Button-1>', self.rb_n)
        self.rb_hard.bind('<Button-1>', self.rb_h)
        self.rb_extreme.bind('<Button-1>', self.rb_x)
        self.window.mainloop()
