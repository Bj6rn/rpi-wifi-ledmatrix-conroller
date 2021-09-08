#!/usr/bin/python3
#-*- coding: utf-8 -*-
from time import sleep
from signal import pause
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
        if "matrix-board" in data: # wenn Pixel-Liste übergeben wurde, wird sie ausgegeben
            myledmatrix.drawpixelarray(data["matrix-board"])
        elif "matrix-example" in data: # wenn example-image übergeben wurde, wird diese ausgegen
            filepath = "static/img/" + data["matrix-example"]
            myledmatrix.drawimage(filepath)
        elif "usertext" in data: # wenn usertext übergeben wurde, wird diese als scrolling Text ausgegeben
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
