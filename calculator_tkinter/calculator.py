import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText as st
import math

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Lang Nhat Tan. Calculator")
        self.window.iconbitmap("calculator.ico")
        self.window.config(bg = "skyblue")
        width, height = 500, 500
        screen_width, screen_heigth = self.window.winfo_screenwidth(), self.window.winfo_screenheight()
        x, y = int(screen_width / 2 - width / 2), int(screen_heigth / 2 - height / 2)
        self.window.geometry(f"{width}x{height}+{x}+{y}")
        self.control = ttk.Notebook(self.window)
        self.initial = ""
        self.nums = ""
        self.equation = tk.StringVar()
        self.result = tk.StringVar()
        self.check = tk.IntVar()
        self._nums = tk.StringVar()
        self.stack = []
        self.flag = False
        self.flag_pow = False
        self._gcd = False
        self._lcm = False
    # --------- Implement method -------------------


    def press(self, num):
        if not self.flag and not self.flag_pow and not self._gcd and not self._lcm:
            if str(num).isnumeric(): self.nums += str(num)
            else : self.nums = ""
            self.initial += str(num)
            self.equation.set(self.initial)
        else:
            if self.flag:
                for _ in range(num):
                    self.initial += "0"
            else:
                temp = self.initial
                self.initial = ""
                if self.nums == "" : self.nums = temp
                for i in range(len(temp) - 1, -1, -1):
                    if not temp[i].isnumeric():
                        for j in range(i + 1):
                            self.initial += temp[j]
                        break
                if self.flag_pow : self.initial += str(pow(int(eval(self.nums)), num))
                elif self._gcd: self.initial += str(math.gcd(int(self.nums), num))
                else: self.initial += str((int(self.nums) * num) //  math.gcd(int(self.nums), num))
            self.equation.set(self.initial)
            self.flag = False
            self.flag_pow = False
            self._gcd = False
            self._lcm = False
            self.nums = ""
        


    def x_10(self):
        temp = self.initial + "*10^x"
        self.equation.set(temp)
        self.pre = self.initial
        self.flag = True


    
    def pow_x(self):
        temp = self.initial + "^x"
        self.equation.set(temp)
        self.flag_pow = True
    




    def ans(self):
        if len(self.stack) != 0:
            self.initial += self.stack[-1]
            self.equation.set(self.initial)



    def gcd(self):
        temp = self.initial + " GCD"
        self.equation.set(temp)
        self._gcd = True
    


    def lcm(self):
        temp = self.initial + " LCM"
        self.equation.set(temp)
        self._lcm = True




    def process(self):
        try:
            total = str(eval(self.initial))
            self.result.set(total)
            self.stack.append(total)
        except:
            self.result.set("Error")
        self.initial = ""




    def clear(self):
        self.initial = ""
        self.equation.set("")
        self.result.set("")
        self.flag = False
        self.flag_pow = False
        self._gcd = False
        self._lcm = False

    def sieve_of_eratosthenes(self, n):
        primes = [True] * (n + 1)
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                for j in range(i ** 2, n + 1, i):
                    primes[j] = False
        display = [i for i in range(2, n + 1) if primes[i]]
        string_num = "".join([str(display[i]) + ', ' for i in range (len(display)-1)])
        string_num += str(display[-1]) + '.'
        return string_num
    
    def check_perfect(self, num):
        def IsPrime(n):
            if n <2:
                return False
            m = int(math.sqrt(n))
            for i in range(2,m+1):
                if n % i ==0:
                    return False
                return True
        p = 2
        s = 0
        while s < num:
            b = pow(2, p) - 1
            if IsPrime(b):
                a = pow(2, p-1)
                s = a * b
            p+=1
        return s == num


    # ---------------- Tab 1 -------------------------
    def tab_1(self):
        # --------------- Screen ---------------
        tab_1 = tk.Frame(self.control, background = "SeaGreen1")
        self.control.add(tab_1, text = "Basic Calculator")
        self.control.grid(row = 0, column = 0)
        screen = tk.LabelFrame(tab_1, text = "Screen")
        screen.grid(row = 1, column = 0, padx = 8, pady = 4)
        screen.config(fg = "blue", bg = "bisque")
        entry = tk.Entry(screen, textvariable = self.equation, width = 40, background = "snow3")
        entry.grid(row = 1, column = 0, columnspan = 4, ipadx = 70)

        # ----------------- Output ----------------
        output = tk.LabelFrame(tab_1, text = "Output", background = "old lace")
        output.grid(row = 2, column = 0, ipadx = 8, pady = 4)
        output.config(fg = "blue")
        entry_output = tk.Entry(output, textvariable = self.result, background = "snow3")
        entry_output.grid(row = 0, column = 0, ipadx = 10)
        # ---------------- Input ----------------
        input_num = tk.LabelFrame(tab_1, text = "Input", background = "cyan")
        input_num.grid(row = 3, column = 0, padx = 8, pady = 4)
        input_num.config(fg = "blue")
        num_1 = tk.Button(input_num, text = "1", borderwidth = 0, width = 10, command = lambda : self.press(1), background = "gray70")
        num_1.grid(row = 3, column = 0)
        num_2 = tk.Button(input_num, text = "2", borderwidth = 0, width = 10, command = lambda : self.press(2), background = "gray70")
        num_2.grid(row = 3, column = 1)
        num_3 = tk.Button(input_num, text = "3", borderwidth = 0, width = 10, command = lambda : self.press(3), background = "gray70")
        num_3.grid(row = 3, column = 2)
        num_4 = tk.Button(input_num, text = "4", borderwidth = 0, width = 10, command = lambda : self.press(4), background = "gray70")
        num_4.grid(row = 4, column = 0)
        num_5 = tk.Button(input_num, text = "5", borderwidth = 0, width = 10, command = lambda : self.press(5), background = "gray70")
        num_5.grid(row = 4, column = 1)
        num_6 = tk.Button(input_num, text = "6", borderwidth = 0, width = 10, command = lambda : self.press(6), background = "gray70")
        num_6.grid(row = 4, column = 2)
        num_7 = tk.Button(input_num, text = "7", borderwidth = 0, width = 10, command = lambda : self.press(7), background = "gray70")
        num_7.grid(row = 5, column = 0)
        num_8 = tk.Button(input_num, text = "8", borderwidth = 0, width = 10, command = lambda : self.press(8), background = "gray70")
        num_8.grid(row = 5, column = 1)
        num_9 = tk.Button(input_num, text = "9", borderwidth = 0, width = 10, command = lambda : self.press(9), background = "gray70")
        num_9.grid(row = 5, column = 2)
        num_0 = tk.Button(input_num, text = "0", borderwidth = 0, width = 10, command = lambda : self.press(0), background = "gray70")
        num_0.grid(row = 6, column = 0)
        add_operator = tk.Button(input_num, text = "+", borderwidth = 0, width = 10, command = lambda : self.press("+"), background = "dark orange")
        add_operator.grid(row = 3, column = 3)
        subtract_operator = tk.Button(input_num, text = "-", borderwidth = 0, width = 10, command = lambda : self.press("-"), background = "dark orange")
        subtract_operator.grid(row = 3, column = 4)
        multiple_operator = tk.Button(input_num, text = "*", borderwidth = 0, width = 10, command = lambda : self.press("*"), background = "dark orange")
        multiple_operator.grid(row = 4, column = 3)
        divide_operator = tk.Button(input_num, text = "/", borderwidth = 0, width = 10, command = lambda : self.press("/"), background = "dark orange")
        divide_operator.grid(row = 4, column = 4)
        bracket_open = tk.Button(input_num, text = "(", borderwidth = 0, width = 10, command = lambda : self.press("("), background = "dark orange")
        bracket_open.grid(row = 5, column = 3)
        bracket_close = tk.Button(input_num, text = ")", borderwidth = 0, width = 10, command = lambda : self.press(")"), background = "dark orange")
        bracket_close.grid(row = 5, column = 4)
        dot = tk.Button(input_num, text = ".", borderwidth = 0, width = 10, command = lambda : self.press("."), background = "gray63")
        dot.grid(row = 6, column = 1)
        x_pow_10 = tk.Button(input_num, text = "*10^x", borderwidth = 0, width = 10, command = self.x_10, background = "gray63")
        x_pow_10.grid(row = 6, column = 2)
        Ans = tk.Button(input_num, text = "Ans", borderwidth = 0, width = 10, command = self.ans, background = "gray63")
        Ans.grid(row = 6, column = 3)
        equal = tk.Button(input_num, text = "=", borderwidth = 0, width = 10, command = self.process, background = "dark orange")
        equal.grid(row = 6, column = 4)
        clear = tk.Button(input_num, text = "Clear", borderwidth = 0, width = 10, command = self.clear, background = "khaki1")
        clear.grid(row = 6, column = 5)
        pow_x = tk.Button(input_num, text = "^x", borderwidth = 0, width = 10, command = self.pow_x, background = "khaki1")
        pow_x.grid(row = 5, column = 5)
        gcd = tk.Button(input_num, text = "GCD", borderwidth = 0, width = 10, command = self.gcd, background = "khaki1")
        gcd.grid(row = 4, column = 5)
        lcm = tk.Button(input_num, text = "LCM", borderwidth = 0, width = 10, command = self.lcm, background = "khaki1")
        lcm.grid(row = 3, column = 5)



    # ----------------------------- Tab 2 -------------------------------
    def tab_2(self):
        tab_2 = tk.Frame(self.control, background = "bisque2")
        self.control.add(tab_2, text = "Calculate advanced")
        self.control.grid(row = 0, column = 0)
        screen = tk.LabelFrame(tab_2, text = "Input", background = "#FBD786")
        screen.grid(row = 1, column = 0, padx = 8, pady = 4)
        screen.config(fg = "blue")
        display_a = tk.Label(screen, text = "Enter value a", background = "wheat1")
        display_a.grid(row = 0, column = 0)
        display_b = tk.Label(screen, text = "Enter value b", background = "wheat1")
        display_b.grid(row = 0, column = 1)
        display_c = tk.Label(screen, text = "Enter value c", background = "wheat1")
        display_c.grid(row = 0, column = 2)
        # ----------------------- Input ----------------------
        entry = tk.Entry(screen, width = 10, background = "LightBlue3")
        entry.grid(row = 1, column = 0)
        entry_v1 = tk.Entry(screen, width = 10, background = "LightBlue3")
        entry_v1.grid(row = 1, column = 1)
        entry_v2 = tk.Entry(screen, width = 10, background = "LightBlue3")
        entry_v2.grid(row = 1, column = 2)
        def prime_number():
            try:
                value = int(entry.get())
                display = self.sieve_of_eratosthenes(value)
                output.insert(tk.INSERT, display + '\n')
            except:
                output.insert(tk.INSERT, "Error")
        
        def isPerfect():
            try:
                value = int(entry.get())
                display = [i for i in range(value + 1) if self.check_perfect(i)]
                string_nums = "".join([str(display[i]) + ", " for i in range(len(display)-1)])
                string_nums += str(display[-1]) + '.'
                output.insert(tk.INSERT, string_nums + '\n')
                
            except:
                output.insert(tk.INSERT, "Error")
        
        def fibonanci():
            try:
                value = int(entry.get())
                dp = [0, 0, 1]
                for _ in range(2, value + 1):
                    dp.append(dp[-1] + dp[-2])
                string_nums = "".join([str(dp[i]) + ', ' for i in range(len(dp)-1)])
                string_nums += str(dp[-1]) + '.'
                output.insert(tk.INSERT, string_nums + '\n')
            except:
                output.insert(tk.INSERT, "Error\n")

        def equation_2_():
            try:
                a, b, c = int(entry.get()), int(entry_v1.get()), int(entry_v2.get())
                delta = math.sqrt(pow(b, 2)) + (4 * a * c)
                if delta < 0: output.insert(tk.INSERT, "Phuong trinh vo nghiem \n")
                elif delta == 0: output.insert(tk.INSERT, f"Phuong trinh co nghiem kep\n x = {round((-c / b), 2)}\n")
                else: output.insert(tk.INSERT, f"Phuong trinh co 2 nghiem\n x1 = {round((-b + math.sqrt(delta)) / (2 * a), 2)}\n x2 = {round((-b - math.sqrt(delta)) / (2 * a), 2)}\n")
            except: output.insert(tk.INSERT, "Input not valid\n")
        
        def equation_1_():
            try:
                a, b = int(entry.get()), int(entry_v1.get())
                if b == 0: output.insert(tk.INSERT, "gia tri b phai khac 0 \n")
                else: output.insert(tk.INSERT, f"Phuong trinh co nghiem\n x = {round((-b / a), 2)}\n")
            except: output.insert(tk.INSERT, "Input not valid\n")
        
        def clear_():
            output.delete('1.0', 'end')
        

        prime = tk.Button(screen, text = "Display first N prime number", width = 25, command = prime_number, background = "tan1")
        prime.grid(row = 2, column = 1)
        fibo = tk.Button(screen, text = "Display first N fibonanci number", width = 25, command = fibonanci, background = "tan1")
        fibo.grid(row = 3, column = 1)
        perfect_num = tk.Button(screen, text = "Display first N perfect number", width = 25, command = isPerfect, background = "tan1")
        perfect_num.grid(row = 4, column = 1)
        equation_1 = tk.Button(screen, text = "ax + b = 0", width = 25, command = equation_1_, background = "tan1")
        equation_1.grid(row = 5, column = 1)
        equation_2 = tk.Button(screen, text  ="ax^2 + bx + c = 0", width = 25, command = equation_2_, background = "tan1")
        equation_2.grid(row = 6, column = 1)
        clear = tk.Button(screen, text = "Clear", width = 10, command = clear_, background = "tan1")
        clear.grid(row = 7, column = 1)

        # ----------------- Output ---------------------
        output_frame = tk.LabelFrame(tab_2, text = "Output", background = "#6DD5FA")
        output_frame.grid(row = 3, column = 0)
        output_frame.config(fg = "blue")
        output = st(output_frame, width = 50, height = 5)
        output.grid(row = 4, column = 0)
        output.config(background = "thistle1")
    # ---------------------- Run program ------------------------
    def main(self):
        self.tab_1()
        self.tab_2()
        self.window.mainloop()

if __name__ == "__main__":
    cal = Calculator()
    cal.main()