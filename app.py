from flask import Flask, make_response, request,render_template
import io
import csv
import pandas as pd

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('input.html')

@app.route('/input', methods=["POST"])
def input():
    c=0
    f = request.files['filename']
    if not f:
        return "No file"
    stream = io.TextIOWrapper(f.stream._file, "UTF8", newline=None)
    csv_input = csv.reader(stream)
    data=pd.read_csv(stream)
    print(len(data))
    return str(len(data))

if __name__ == "__main__":
    app.run(debug=True)
    
