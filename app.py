from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>CyberGuard AI</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #0B1220;
                color: #F8FAFC;
                margin: 0;
                padding: 40px 20px;
            }

            .container {
                max-width: 900px;
                margin: auto;
            }

            h1 {
                color: #3B82F6;
            }

            .card {
                background: #111C2E;
                padding: 25px;
                margin-top: 20px;
                border-radius: 12px;
                border: 1px solid #1E293B;
            }

            a {
                display: inline-block;
                margin-top: 10px;
                padding: 12px 18px;
                background: #3B82F6;
                color: white;
                text-decoration: none;
                border-radius: 8px;
            }

            a:hover {
                background: #06B6D4;
            }
        </style>
    </head>

    <body>
        <div class="container">

            <h1>CyberGuard AI</h1>

            <div class="card">
                <h2>Project Overview</h2>
                <p>
                    An AI-based cybersecurity project focused on analyzing
                    security-related data and supporting cybersecurity analysis.
                </p>
            </div>

            <div class="card">
                <h2>Project Workflow</h2>
                <p>
                    Data/Input → Processing → Analysis → AI-based Interpretation
                </p>
            </div>

            <div class="card">
                <h2>Python Source Code</h2>
                <p>
                    The original CyberGuard AI Python implementation is
                    available on GitHub.
                </p>

                <a href="https://github.com/durgamalleswari018/Cyberguard-ai/blob/bcd011cae89c427e6e99764bba40917806f53aae/cyber.py"
                   target="_blank">
                    View Python Code
                </a>
            </div>

        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
