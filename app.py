from flask import Flask, render_template, request, jsonify
import OIC_IS_BETTER
import webbrowser
import os
import signal
import time
app = Flask(__name__)

"""
All Buttons and their function calls
"""
def NID_Button(location):
    result = OIC_IS_BETTER.NID_Install_Message(location)
    return result

def WIA_Button():
    result = OIC_IS_BETTER.WIA_Install_Message()
    return result
def Dispatch_Request_Button(text):
    result = OIC_IS_BETTER.Dispatch_Request_Message(text)
    return result

def Dispatch_Confirm_Button(date, name):
    result = OIC_IS_BETTER.Dispatch_Confirmation_Message(date, name)
    return result
def ATT_Install(ip_address):
    result = OIC_IS_BETTER.ATT_Install(ip_address)
    return result
def CPW_Button():
    result = OIC_IS_BETTER.CPW()
    return result
def Pre_Install_Button():
    result = OIC_IS_BETTER.Pre_Install()
    return result
def Final_Install_Button():
    result = OIC_IS_BETTER.Final_Install()
    return result
def Site_Survey_Button():
    result = OIC_IS_BETTER.Survey_Complete()
    return result
def Survey_Quote():
    result = OIC_IS_BETTER.Survey_Quote()
    return result




@app.route('/')
def index():
    return render_template('index.html')

"""
All App Routes
"""
@app.route('/shutdown', methods=['GET'])
def shutdown():
    os.kill(os.getpid(), signal.SIGINT)
    time.sleep(1)
    return jsonify({"success": True, "message": "Server is shutting down..."})

@app.route('/trigger_NID', methods=['POST'])
def trigger_nid_message():
    location = request.form.get('location')
    result = NID_Button(location)
    return jsonify({'message': result})

@app.route('/trigger_wia_message', methods=['POST'])
def trigger_wia_message():
    result = WIA_Button()
    return jsonify({'message': result})

@app.route('/trigger_DR', methods=['POST'])
def trigger_DR_button():
    date = request.form.get('date')
    result = Dispatch_Request_Button(date)
    return jsonify({'message':result})

@app.route('/trigger_DC', methods=['POST'])
def trigger_DC_button():
    date = request.form.get('date')
    name = request.form.get('name')
    result = Dispatch_Confirm_Button(date, name)
    return jsonify({'message':result})

@app.route('/trigger_ATT', methods=['POST'])
def trigger_ATT_button():
    ip = request.form.get('ip')
    result = ATT_Install(ip)
    return jsonify({'message':result})

@app.route('/trigger_CPW', methods=['POST'])
def trigger_cpw_message():
    result = CPW_Button()
    return jsonify({'message': result})

@app.route('/trigger_PI', methods=['POST'])
def trigger_pi_message():
    result = Pre_Install_Button()
    return jsonify({'message': result})

@app.route('/trigger_FI', methods=['POST'])
def trigger_fi_message():
    result = Final_Install_Button()
    return jsonify({'message': result})

@app.route('/trigger_SS', methods=['POST'])
def trigger_ss_message():
    result = Site_Survey_Button()
    return jsonify({'message': result})

@app.route('/trigger_SQ', methods=['POST'])
def trigger_sq_message():
    result = Survey_Quote()
    return jsonify({'message': result})

if __name__ == '__main__':
    app_url = "http://127.0.0.1:5000"
    webbrowser.open(app_url)
    app.run(debug=False)