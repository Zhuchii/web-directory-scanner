from flask import Flask, request, jsonify, render_template
import subprocess
import time

app = Flask(__name__)

@app.route("/")
def root():
    return render_template("index.html")

@app.route('/scan', methods=['POST'])
def run_gobuster():
    data = request.get_json()
    target = data.get("target")
    wordlist = data.get("wordlist")
    
    if not target or not wordlist:
        return jsonify({"error": "Target and wordlist are required"}), 400
    
    try:
        start_time = time.time()
        
        result = subprocess.run([
            "gobuster", "dir", "-u", target, "-w", wordlist, "-o", "result.txt"
        ], capture_output=True, text=True)
        
        end_time = time.time()
        elapsed_time = end_time - start_time
        
        with open("result.txt", "r") as f:
            output_lines = f.readlines()
        
        return jsonify({
            "results": output_lines,
            "time_taken": elapsed_time
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
