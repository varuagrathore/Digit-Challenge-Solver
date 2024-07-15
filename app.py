from flask import Flask, request, render_template_string
import itertools

app = Flask(__name__)

def solve_digit_challenge(equation):
    lhs, rhs = equation.split('=')
    rhs = int(rhs.strip())
    placeholders = lhs.count('_')
    digit_combinations = itertools.permutations(range(1, 10), placeholders)
    
    solutions = []
    for combination in digit_combinations:
        test_equation = lhs
        for digit in combination:
            test_equation = test_equation.replace('_', str(digit), 1)
        try:
            if eval(test_equation) == rhs:
                solutions.append(test_equation)
        except:
            continue
    
    return solutions

@app.route('/', methods=['GET', 'POST'])
def index():
    result_text = ""
    if request.method == 'POST':
        equation = request.form['equation']
        if equation:
            solutions = solve_digit_challenge(equation)
            if solutions:
                result_text = "Possible solutions:\n" + "\n".join(solutions)
            else:
                result_text = "No solutions found."
    
    return render_template_string('''
        <!doctype html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Digit Challenge Solver</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }
                .container {
                    background: white;
                    padding: 20px;
                    border-radius: 8px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                    text-align: center;
                    width: 90%;
                    max-width: 400px;
                }
                input[type="text"] {
                    width: 100%;
                    padding: 10px;
                    margin-bottom: 10px;
                    font-size: 16px;
                    border: 1px solid #ccc;
                    border-radius: 4px;
                }
                input[type="submit"] {
                    padding: 10px 20px;
                    font-size: 16px;
                    color: white;
                    background: green;
                    border: none;
                    border-radius: 4px;
                    cursor: pointer;
                    margin-bottom: 10px;
                    width: 100%;
                }
                pre {
                    text-align: left;
                    background: #f9f9f9;
                    padding: 10px;
                    border-radius: 4px;
                    border: 1px solid #ccc;
                    height: 150px;
                    overflow-y: auto;
                    white-space: pre-wrap;
                    word-wrap: break-word;
                }
                .grid-container {
                    display: grid;
                    grid-template-columns: repeat(4, 1fr);
                    gap: 10px;
                    margin: 10px 0;
                }
                .grid-item {
                    padding: 20px;
                    font-size: 16px;
                    border: none;
                    border-radius: 4px;
                    cursor: pointer;
                    background-color: #eee;
                }
                .operator {
                    background-color: #ddd;
                }
                .clear {
                    background-color: red;
                    color: white;
                }
                @media (max-width: 600px) {
                    .grid-item {
                        padding: 15px;
                        font-size: 14px;
                    }
                    input[type="text"] {
                        font-size: 14px;
                    }
                    input[type="submit"] {
                        font-size: 14px;
                    }
                    .container {
                        width: 100%;
                        max-width: none;
                        padding: 10px;
                    }
                }
                @media (max-width: 400px) {
                    .grid-item {
                        padding: 10px;
                        font-size: 12px;
                    }
                    input[type="text"] {
                        font-size: 12px;
                    }
                    input[type="submit"] {
                        font-size: 12px;
                    }
                    .container {
                        width: 100%;
                        max-width: none;
                        padding: 5px;
                    }
                }
            </style>
            <script>
                function appendToEquation(char) {
                    document.getElementById('equation').value += char;
                }
                function clearEquation() {
                    document.getElementById('equation').value = '';
                }
            </script>
        </head>
        <body>
            <div class="container">
                <h1>Digit Challenge Solver</h1>
                <form method="post">
                    <input type="text" name="equation" id="equation" placeholder="Enter equation" value="{{ request.form.equation }}">
                    <div class="grid-container">
                        <button type="button" class="grid-item" onclick="appendToEquation('1')">1</button>
                        <button type="button" class="grid-item" onclick="appendToEquation('2')">2</button>
                        <button type="button" class="grid-item" onclick="appendToEquation('3')">3</button>
                        <button type="button" class="grid-item operator" onclick="appendToEquation('+')">+</button>
                        <button type="button" class="grid-item" onclick="appendToEquation('4')">4</button>
                        <button type="button" class="grid-item" onclick="appendToEquation('5')">5</button>
                        <button type="button" class="grid-item" onclick="appendToEquation('6')">6</button>
                        <button type="button" class="grid-item operator" onclick="appendToEquation('-')">-</button>
                        <button type="button" class="grid-item" onclick="appendToEquation('7')">7</button>
                        <button type="button" class="grid-item" onclick="appendToEquation('8')">8</button>
                        <button type="button" class="grid-item" onclick="appendToEquation('9')">9</button>
                        <button type="button" class="grid-item operator" onclick="appendToEquation('*')">*</button>
                        <button type="button" class="grid-item" onclick="appendToEquation('_')">_</button>
                        <button type="button" class="grid-item" onclick="appendToEquation('0')">0</button>
                        <button type="button" class="grid-item operator" onclick="appendToEquation('=')">=</button>
                        <button type="button" class="grid-item operator" onclick="appendToEquation('/')">/</button>
                        <button type="button" class="grid-item" onclick="appendToEquation('(')">(</button>
                        <button type="button" class="grid-item" onclick="appendToEquation(')')">)</button>
                        <button type="button" class="grid-item clear" onclick="clearEquation()">C</button>
                        <button type="button" class="grid-item operator" onclick="appendToEquation('%')">%</button>
                    </div>
                    <input type="submit" value="Solve">
                </form>
                <pre>{{ result_text }}</pre>
            </div>
        </body>
        </html>
    ''', result_text=result_text)

if __name__ == '__main__':
    app.run(debug=True)
