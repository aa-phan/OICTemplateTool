from flask import Flask, render_template, request, jsonify
import OIC_IS_BETTER
import webbrowser
import os
import signal
import time
import sys
import subprocess 
import json
import PCA

app = Flask(__name__)

"""
All Buttons and their function calls
"""
def NID_Button():
    result = OIC_IS_BETTER.NID_Install_Message()
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

def Install_Fail():
    result = OIC_IS_BETTER.Install_Failed()
    return result

def Labels_Template(CID, TID, conf):
    result = OIC_IS_BETTER.Labels_Template(CID, TID, conf)
    return result
def CER_Script(ae_tag, vlan_tag, ipv4_address, ipv6_address):
    result = PCA.CER_Scrub(ae_tag, vlan_tag, ipv4_address, ipv6_address)
    return result
def CES_Script(vlan_tag, interface):
    result = PCA.CES_Scrub(vlan_tag, interface)
    return result
def NID_RAD_Script(ether1, ether2):
    result = PCA.NID_Scrub_Rad(ether1, ether2)
    return result

def terminate_flask_app_windows_simple(flask_app_pid):
    """
    Terminates a Flask application on Windows using taskkill (simpler).
    """
    try:
        subprocess.run(['taskkill', '/F', '/PID', str(flask_app_pid)],
                       check=True,  # Raise an exception if the command fails
                       capture_output=True, # Capture stdout and stderr
                       text=True, # Return output as string
                       creationflags=subprocess.DETACHED_PROCESS, # Detach the new process from the parent
                       shell=False)
        print(f"Successfully terminated PID {flask_app_pid} with taskkill.")
    except subprocess.CalledProcessError as e:
        print(f"Error terminating process with taskkill: {e.stderr}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


@app.route('/')
def index():
    return render_template('index.html')

"""
All App Routes
"""
@app.route('/shutdown', methods=['GET'])
def shutdown():
    #os.kill(os.getpid(), signal.SIGINT)
    #os.system("taskkill /im app.exe /f")
    #time.sleep(1)
    terminate_flask_app_windows_simple(os.getpid())
    
    return jsonify({"success": True, "message": "Server is shutting down..."})

@app.route('/trigger_NID', methods=['POST'])
def trigger_nid_message():
    #location = request.form.get('location')
    result = NID_Button()
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

@app.route('/trigger_IF', methods=['POST'])
def trigger_if_message():
    result = Install_Fail()
    return jsonify({'message': result})

@app.route('/trigger_labels', methods=['POST'])
def trigger_labels_message():
    CID  = request.form.get('circuit_ID')
    TID  = request.form.get('device_ID')
    conf  = request.form.get('config')
    result = Labels_Template(CID, TID, conf)
    #data = json.loads(result)
    #if isinstance(data, dict):
    #    for key, value in data.items():
    #        print(f"{key}: {value}")
    return result

@app.route('/trigger_CER', methods=['POST'])
def trigger_CER_message():
    ae_tag = request.form.get('ae_tag')
    vlan_tag = request.form.get('vlan_tag')
    ipv4 = request.form.get('ipv4_address')
    ipv6 = request.form.get('ipv6_address')
    result = CER_Script(ae_tag, vlan_tag, ipv4, ipv6)
    return jsonify({'message': result})

@app.route('/trigger_CES', methods=['POST'])
def trigger_CES_message():
    vlan_tag = request.form.get('vlan_tag')
    interface = request.form.get('interface')
    result = CES_Script(vlan_tag, interface)
    return jsonify({'message': result})

@app.route('/trigger_NID_RAD', methods=['POST'])
def trigger_RAD_message():
    ether1 = request.form.get('ether1')
    ether2 = request.form.get('ether2')
    result = NID_RAD_Script(ether1, ether2)
    return jsonify({'message': result})

if __name__ == '__main__':
    app_url = "http://127.0.0.1:5000"
    webbrowser.open(app_url)
    app.run(debug=False)