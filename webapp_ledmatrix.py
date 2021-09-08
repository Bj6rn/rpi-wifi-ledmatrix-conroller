#!/usr/bin/python3
#-*- coding: utf-8 -*-
from time import sleep
from flask import Flask, render_template, request
import myledmatrix 
import os, fnmatch

app = Flask(__name__)

def get_matrix_examples():
    img_array = []
    path = "static/img/"
    directory_list = os.listdir(path)
    pattern = "*.png"
    for file in directory_list:
        if fnmatch.fnmatch(file, pattern):
            img_array.append(file)
            
    return img_array

@app.route('/led-matrix', methods=['GET','POST'])
def led_matrix():
    if request.method == 'POST': # POST request
        data = request.get_json()
        if "matrix-board" in data: # if a "pixel-array" is transmitted in the request, then it gets output to the matrix
            myledmatrix.drawpixelarray(data["matrix-board"])
        elif "matrix-example" in data: # if one of the example-images is transmitted in the request, then it gets output to the matrix
            filepath = "static/img/" + data["matrix-example"]
            myledmatrix.drawimage(filepath)
        elif "usertext" in data: # if some usertext is transmitted in the request, then it gets output as a scrolling text to the matrix
            myledmatrix.scrollingtext(data["usertext"])
        else: 
            myledmatrix.resetmatrix()
        return 'OK', 200
    else: # GET request
        pass
    
    templateData = {
        'title':'LED-Matrix Controller',
        'examples':get_matrix_examples()
        }
    return render_template('index.html', **templateData)

if __name__ == "__main__":
    app.run(port=6060, host='0.0.0.0',debug=True)
