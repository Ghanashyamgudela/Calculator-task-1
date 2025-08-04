<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>hm... a Calculator</title>
  <style>
    body {
      font-family: 'Courier New', monospace;
      background-color: #1e1e1e;
      color: #d4d4d4;
      padding: 2rem;
      line-height: 1.6;
    }
    h1, h2 {
      color: #ffcb6b;
    }
    code {
      background: #333;
      padding: 0.2rem 0.4rem;
      border-radius: 4px;
      color: #c3e88d;
    }
    pre {
      background: #2d2d2d;
      padding: 1rem;
      border-radius: 8px;
      overflow-x: auto;
    }
    ul {
      list-style: square;
      margin-left: 1.5rem;
    }
    a {
      color: #82aaff;
      text-decoration: none;
    }
  </style>
</head>
<body>

  <h1>🤔 hm... A Calculator?</h1>

  <p>Yeah. I made a calculator.<br>
  In Python.<br>
  In the terminal.<br>
  Simple? Definitely.<br>
  Boring? Not really. Keep scrolling.</p>

  <h2>🧮 What it does</h2>
  <ul>
    <li>➕ Add</li>
    <li>➖ Subtract</li>
    <li>✖️ Multiply</li>
    <li>➗ Divide (but like... no zero please)</li>
  </ul>

  <p>No buttons. Just text. Pure terminal vibes.</p>

  <h2>🛠️ Setup</h2>
  <pre><code>git clone https://github.com/your-username/hm-calculator.git
cd hm-calculator
python calculator.py</code></pre>

  <h2>🔍 Peek inside</h2>
  <pre><code>operations = {
    '1': ('Addition', add),
    '2': ('Subtraction', subtract),
    ...
}</code></pre>
  <p>Each number is tied to a function. You pick. It calculates.</p>

  <h2>🧪 Sample Run</h2>
  <pre><code>==== Simple Calculator ====
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit
Choose an option (1-5): 3
Enter first number: 6
Enter second number: 7
Multiplication result: 42.0</code></pre>

  <h2>🧩 Want more?</h2>
  <p>Add your own logic!</p>
  <pre><code>def power(a, b): return a ** b</code></pre>

  <h2>🧘‍♂️ Final thoughts</h2>
  <p>This isn't just a calculator.<br>
  It's clean code.<br>
  It's chill logic.<br>
  It's a vibe.</p>

  <h2>📜 License</h2>
  <p>MIT — use it, fork it, remix it.</p>

  <p><em>– Made with curiosity and Python<br>– <strong>hm...</strong></em></p>

</body>
</html>
