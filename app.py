from flask import Flask, render_template, url_for, request

import K_NN_ML_DS

app = Flask(__name__)

'''def encrypt(text,s):
    result = ""
 
    # traverse text
    for i in range(len(text)):
        char = text[i]
 
        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
 
        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result 
 '''

@app.route('/',methods=['POST', 'GET'])
@app.route('/home',methods=['POST', 'GET'])
def home():
    return render_template("index.html")



@app.route('/result',methods=['POST', 'GET'])
def result():
    output = request.form.to_dict()
    print(output)
    name = output["name"]
    i1=int (output["args1"])
    i2=int (output["args2"])
    i3=int (output['args3'])
    i4=int (output['args4'])
    i5=int (output["args5"])
    i6=int (output["args6"])
    i7=int (output['args7'])
    i8=int (output['args8'])
    i9=int (output["args9"])
    i10=int (output["args10"])
    i11=int (output['args11'])
    i12=int (output['args12'])
    i13=int (output["args13"])
    i14=int (output["args14"])
    i15=int (output['args15'])
    i16=int (output['args16'])
    print(type(i1))
    result = K_NN_ML_DS.K_NN_DS_ALGO(i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16)
    print(result)
    
    if result==True :
        return render_template('married.html', name = name)
    else : 
        return render_template('divorse.html', name = name)

if __name__ == "__main__":
    app.run(debug=True)