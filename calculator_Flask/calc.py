from flask import Flask, render_template, request
import math
app = Flask(__name__)
# app.config.from_object(__name__)

save = 0

@app.route('/')
def welcome():
    return render_template('calculator.html')

@app.route('/', methods=['POST'])

def result():
    global save
    x1 = request.form.get("var_1", type = int, default = 0)
    x2 = request.form.get("var_2", type = int, default = 0)
    x3 = request.form.get("var_3", type = int, default = 0)
    expression = request.form.get("expression", type = str, default = "")
    op = request.form.get("operation")
    ans = 0
    if op == "ax + b = 0":
        if x1 == 0: ans = "Phương_trình_vô_nghiệm"
        else: ans = f"x={-x2 / x1}"
    elif op == "ax^2 + bx + c = 0":
        try:
            delta = (x2 ** 2) - (4 * x1 * x3)
            if delta < 0:
                ans = "Phương_trình_vô_nghiệm"
            elif delta == 0:
                ans = f"x={-x2 / 2 * x1}"
            else:
                a = (-x2 + math.sqrt(delta)) / (2 * x1)
                b = (-x2 - math.sqrt(delta)) / (2 * x1)
                ans = f"x1={a},x2={b}"
        except:
            ans = "Error"
    elif op == "GCD (a, b)":
        try: ans = math.gcd(x1, x2)
        except: ans = "Error"
    elif op == "LCM (a, b)":
        try:
            gcd = math.gcd(x1, x2)
            lcm = (x1 * x2) // gcd
            ans = lcm
        except: ans = "Error"
    elif op == "First N fibonanci":
        dp = [0, 1, 1]
        for i in range(2, x1):
            dp.append(dp[-1] + dp[-2])
        string = ''.join(str(dp[i]) + "," for i in range(len(dp) - 1))
        string += str(dp[-1]) + '.'
        ans = string
    elif op == "First N prime number":
        primes = [True] * (x1 + 1)
        for i in range(2, int(x1 ** 0.5) + 1):
            if primes[i]:
                for j in range(i ** 2, x1 + 1, i):
                    primes[j] = False
        display = [i for i in range(2, x1 + 1) if primes[i]]
        string_num = "".join([str(display[i]) + ',' for i in range (len(display)-1)])
        string_num += str(display[-1]) + '.'
        ans = string_num
    elif op == "Show more prime number":
        n = x1
        primes = [True] * (n + 1)
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                for j in range(i ** 2, n + 1, i):
                    primes[j] = False
        display = [i for i in range(2, n + 1) if primes[i]]
        string_num = "".join([str(display[i]) + ', ' for i in range (len(display)-1)])
        string_num += str(display[-1]) + '.'
        return string_num
    elif op == "Show more fibonanci number":
        dp = [0, 1, 1]
        for i in range(2, x1):
            dp.append(dp[-1] + dp[-2])
        string = ''.join(str(dp[i]) + "," for i in range(len(dp) - 1))
        string += str(dp[-1]) + '.'
        return string
    elif op == "First N perfect number":
        def check_perfect(num):
            def IsPrime(n):
                if n < 2:
                    return False
                m = int(math.sqrt(n))
                for i in range(2, m + 1):
                    if n % i == 0:
                        return False
                    return True
            p = 2
            s = 0
            while s < num:
                b = pow(2, p) - 1
                if IsPrime(b):
                    a = pow(2, p - 1)
                    s = a * b
                p += 1
            return s == num
        display = [i for i in range(x1 + 1) if check_perfect(i)]
        string_nums = "".join([str(display[i]) + "," for i in range(len(display)-1)])
        string_nums += str(display[-1]) + '.'
        ans = string_nums
    
    elif op == "First N square number":
        def check_square_number(n):
            return int(math.sqrt(n)) ** 2 == n
        display = [i for i in range(x1 + 1) if check_square_number(i)]
        string_nums = "".join([str(display[i]) + "," for i in range(len(display)-1)])
        string_nums += str(display[-1]) + '.'
        ans = string_nums
    elif op == "Show more square number":
        def check_square_number(n):
            return int(math.sqrt(n)) ** 2 == n
        display = [i for i in range(x1 + 1) if check_square_number(i)]
        string_nums = "".join([str(display[i]) + "," for i in range(len(display)-1)])
        string_nums += str(display[-1]) + '.'
        return string_nums

    else:
        new_ex = ""
        nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        p, s = False, False
        n1, n2 = "", ""
        i = 0
        while i < len(expression):
            if expression[i] == 'p':
                p = True
                i += 1
            elif expression[i] == 's':
                s = True
                i += 1
            elif expression[i] == "A":
                new_ex += str(save)
                i += 2
            elif expression[i] == 'm':
                i += 2
                while expression[i] in nums:
                    n1 += expression[i]
                    i += 1
                new_ex += str(int(n1) / 100)
            elif not p and not s: new_ex += expression[i]
            else:
                if p:
                    j = i
                    while expression[j] != ',':
                        n1 += expression[j]
                        j += 1
                    j += 1
                    while expression[j] in nums:
                        n2 += expression[j]
                        j += 1
                    # print(n1, n2)
                    new_ex += str(pow(int(n1), int(n2)))
                    p = False
                    n1, n2 = "", ""
                    i = j
                if s:
                    j = i
                    while expression[j] != ',':
                        n1 += expression[j]
                        j += 1
                    j += 1
                    while expression[j] in nums:
                        n2 += expression[j]
                        j += 1
                    # print(n1, n2)
                    new_ex += str(pow(int(n1), 1 / int(n2)))
                    s = False
                    n1, n2 = "", ""
                    i = j
            i += 1
        try:
            ans = eval(new_ex)
        except:
            ans = "Error"
    save = ans
    return render_template("calculator.html", entry = ans)


@app.route('/geometry')
def index():
    return render_template("geometry.html")

@app.route('/geometry', methods=['POST'])
def geometry():
    v1 = request.form.get("var_1", type = int, default = 0)
    v2 = request.form.get("var_2", type = int, default = 0)
    v3 = request.form.get("var_3", type = int, default = 0)
    op = request.form.get("operation")
    ans = 0
    if op == "Perimeter Triangle":
        ans = v1 + v2 + v3
    elif op == "Area Triangle":
        perimeter = v1 + v2 + v3
        area = math.sqrt(perimeter * (perimeter - v1) * (perimeter - v2) * (perimeter - v3))
        ans = area
    elif op == "Perimeter Rectangle": ans = (v1 + v2) * 2
    elif op == "Area Rectangle": ans = v1 * v2
    elif op == "Perimeter Circle": ans = 2 * math.pi * v1
    elif op == "Area Circle": ans = math.pi * (v1 ** 2)
    elif op == "Check Triangle":
        if v1 == v2 == v3: ans = "Đây_là_tam_giác_đều"
        elif v1 == v2 or v2 == v3 or v1 == v3: ans = "Đây_là_tam_giác_cân"
        elif (pow(v1, 2) + pow(v2, 2) == pow(v3, 2)) or (pow(v2, 2) + pow(v3, 2) == pow(v1, 2)) or (pow(v1, 2) + pow(v3, 2) == pow(v2, 2)): ans = "Đây_là_tam_giác_vuông"
        else: ans = "Đây_là_tam_giác_thường"
    elif op == "Perimeter Square": ans = 4 * v1
    elif op == "Area Square": ans = v1 * v1
    return render_template("geometry.html", entry = ans)


if __name__ == '__main__':
    app.run(debug=True)
