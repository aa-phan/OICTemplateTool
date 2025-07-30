from datetime import datetime
import os
import win32api
import win32net
import re
import json

def get_windows_display_name_pywin32():
  try:
    # Get the current logged-in username (SAM Account Name)
    username = win32api.GetUserName() 

    # Get information about the user, including the full name
    user_info = win32net.NetUserGetInfo(win32net.NetGetAnyDCName(), username, 2) 

    # Extract the full name (display name)
    display_name = user_info["full_name"] 
    name_parts = display_name.split(', ')
    
    first_name = name_parts[1]
    last_name = name_parts[0]
    
    first_initial = first_name[0]
    
    return f"{first_initial}{last_name}"
  except Exception as e:
    print(f"Error getting display name with pywin32: {e}")
    return None

user = get_windows_display_name_pywin32()

def get_datetime():
    return f"{datetime.now().strftime("%m/%d | %#I:%M %p")} | {user} |"

def NID_Install_Message():
  """
  Prints the standard message for successful NID installs. Used for ADVA 114 but could be adjusted in the future
  """
  return f"{get_datetime()} Install complete. Customer handoff is copper port 3 on Adva 114 Pro labeled with TID/CID, TACACS enabled, full duplex, connectivity verified, Speed: auto"
def WIA_Install_Message():
  """
  Prints the standard message for successful NID installs. Used for ADVA 114 but could be adjusted in the future
  """
  return f"{get_datetime()} Install complete tech verified connectivity on LAN port "

def Dispatch_Confirmation_Message(date, techName):
  """
  Prints the standard message for successful NID installs. Used for ADVA 114 but could be adjusted in the future
  """
  if ((not techName or not "," in techName) and not date):
    return "Please enter date and Technician Name in LastName, FirstName format."
  elif ((not techName or not "," in techName) and date):
    return "Please enter Technician Name in LastName, FirstName format."
  elif not date:
    return "Please enter date."
  name_parts = techName.split(', ')
    
  first_name = name_parts[1]
  last_name = name_parts[0]
    
  last_initial = last_name[0]
  return f"{get_datetime()} Dispatch confirmed for {date} FT {first_name+last_initial}"

def Dispatch_Request_Message(date):
  """
  Prints the standard message for successful NID installs. Used for ADVA 114 but could be adjusted in the future
  """    
  if not date:
    return "Please enter date."
  return f"{get_datetime()} Dispatch requested for {date} pending vendor confirmation"

def ATT_Install(ip_address):
    """
    Standard message for AT&T NID Installs
    """
    return f"{get_datetime()} NID staged w/ AT&T's help. Remote mgmt connection has been established. Pending service provisioning once install date has been set by PM. Adva IP: {ip_address}"

def CPW():
    return f"{get_datetime()} CPW Complete"

def Pre_Install():
    return f"{get_datetime()} Pre-Install Complete"

def Final_Install():
    return f"{get_datetime()} Final Install Complete"

def Survey_Complete():
    return f"{get_datetime()} Site Survey Complete, pending quote from vendor"
    
def Survey_Quote():
    return f"{get_datetime()} Survey doc and quote attached to order"
  
def Install_Failed():
    return f"{get_datetime()} Install failed see attached failure package"
  
def Labels_Template(circuit_ID, device_ID, config_text):
  delimiter = "dhcp-host-name-type system-name\r\n\r\n"
  #parts = re.split(delimiter, config_text)
  parts = config_text.split(delimiter)
  email_step = parts[0] + delimiter +"\r\n"
  
  email_template = f"""
  LABELS

  Circuit ID: {circuit_ID}


  Device ID: {device_ID}



  1. Connect our Advas network port 1 to the carriers handoff port. 
  2. Match whatever handoff media the carrier left for us (SM/MM fiber or copper) 
  3. Connect your computers Ethernet port to the MGMT LAN port of the Adva using an Ethernet copper cable. 
  4. Change your computers IP settings and log into Adva to past in the config below

  IP SETTINGS
  On your laptop do the following to access IP settings:
  Open Run prompt > Type ncpa.cpl in the box, then hit enter> Right click your Ethernet adapter > Select Properties > double click on Internet Protocol Version 4 (TCP/IP) > Select "use the following IP address"  and type the following IPs


  Configure your laptop with the following:
  IP: 192.168.0.3
  SM: 255.255.255.0
  No default gateway or DNS servers needed.

  Open Putty, select the SSH option, under Hostname (or IP address), type in the ADVA's IP:
  192.168.0.2

  ************************

  ####CONFIGS####
  {email_step}
  
  ###AFTER DROPPING THE MAIN SCRIPT ABOVE AND CONNECTING THE ADVA, DROP THE FOLLOWING LINES TO VERIFY IF THE ADVA IS GETTING AN IP###

  home

  configure communication

  show mgmttnl mgmt_tnl-1
  """
  
  parts[1] = parts[1].replace("remote\r\n", "local\r\n")
  parts[1] = parts[1].replace("""home\r\nconfigure user-security\r\naccounting enabled\r\ntacacs-authorization-user-interfaces cli disabled\r\ntacacs-authorization-user-interfaces gui disabled\r\ntacacs-authorization-user-interfaces netconf disabled\r\ntacacs-accounting-record-types config enabled\r\n""", "")
  delimiter = """\r\ntimeout 2\r\nretries 1\r\ncontrol enabled\r\n"""
  
  parts = parts[1].split(delimiter)
  first_step = "\r\n" + parts[0]
  second_step = delimiter
  third_step = """\r\nhome\r\nconfigure user-security\r\nadd comm_engineer comm#EngPWD comm#EngPWD superuser\r\n"""
  fourth_step = "\r\nadd comm_support comm#SupPWD comm#SupPWD maintenance\r\n"
  delimiter = "#Note: You must log out out of root and log back in with the comm_engineer user before proceeding.\r\n"
  parts = parts[1].split(delimiter)
  fifth_step = parts[1]
  response_data = {
    "email_template" : email_template,
    "first_step" : first_step,
    "second_step" : second_step,
    "third_step" : third_step,
    "fourth_step" : fourth_step,
    "fifth_step" : fifth_step
  }
  return json.dumps(response_data)