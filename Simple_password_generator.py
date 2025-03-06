<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Password Generator</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background: linear-gradient(135deg, #ff9a9e, #fad0c4, #fad0c4);
        }
        .container {
            text-align: center;
            background: rgba(255, 255, 255, 0.9);
            padding: 30px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
            border-radius: 15px;
            animation: fadeIn 1s ease;
        }
        input, button {
            margin: 10px;
            padding: 12px;
            border: none;
            border-radius: 5px;
        }
        button {
            background: #ff6b6b;
            color: white;
            cursor: pointer;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            transition: transform 0.2s;
        }
        button:hover {
            transform: translateY(-2px);
            background: #ff4757;
        }
        #result {
            margin-top: 20px;
            font-size: 1.2em;
            color: #ff4757;
            word-break: break-all;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-20px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>✨ Fancy Password Generator ✨</h1>
        <p>Enter the desired password length:</p>
        <input type="number" id="length" min="1" max="100" placeholder="Length">
        <button onclick="generatePassword()">Generate Password</button>
        <p id="result"></p>
    </div>

    <script>
        function generatePassword() {
            const length = parseInt(document.getElementById('length').value);
            const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+';
            let password = '';

            if (length > 0) {
                for (let i = 0; i < length; i++) {
                    password += characters.charAt(Math.floor(Math.random() * characters.length));
                }

                const result = document.getElementById('result');
                result.innerHTML = `🔒 Your password: <strong>${password}</strong>`;
            } else {
                alert('Please enter a valid length!');
            }
        }
    </script>
</body>
</html>



