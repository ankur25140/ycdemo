from flask import Flask ,url_for, redirect, request, render_template, jsonify,session,make_response
import os
import sys
import subprocess
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome!"

@app.route("/ycdemo")
def ycdemo() :
    return render_template('index.html')

@app.route("/analyseimage")
def analyseimage() :
         image_path = request.args.get('image_path',default="NONE", type=None)
         print image_path
        #  os.system('python test.py')
         s2_out = subprocess.check_output([sys.executable, "test.py", image_path ])
         print s2_out
         return jsonify(s2_out)




if __name__ == "__main__":
    app.run(debug = False,port='9090')
    app.run()
