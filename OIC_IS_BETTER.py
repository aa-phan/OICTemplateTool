from datetime import datetime
import os
import win32api
import win32net



def get_datetime():
    return datetime.now().strftime("%m/%d/%Y %#I:%M %p")

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


def NID_Install_Message(location):
  """
  Prints the standard message for successful NID installs. Used for ADVA 114 but could be adjusted in the future
  """
  return f"{get_datetime()} {user} Install complete. Customer handoff is copper port 3 on Adva 114 Pro labeled with TID/CID, TACACS enabled, full duplex, connectivity verified, Speed: auto, Location: {location}"
def WIA_Install_Message():
  """
  Prints the standard message for successful NID installs. Used for ADVA 114 but could be adjusted in the future
  """
  return f"{get_datetime()} {user} Install complete tech verified connectivity on LAN port 1"

def Dispatch_Confirmation_Message(date, techName):
  """
  Prints the standard message for successful NID installs. Used for ADVA 114 but could be adjusted in the future
  """
  return f"{get_datetime()} {user} Dispatch confirmed for {date} FT {techName}"

def Dispatch_Request_Message(date):
  """
  Prints the standard message for successful NID installs. Used for ADVA 114 but could be adjusted in the future
  """
  return f"{get_datetime()} {user} Dispatch requested for {date} pending vendor confirmation"

def ATT_Install(ip_address):
    """
    Standard message for AT&T NID Installs
    """
    return f"{get_datetime()} {user} NID staged w/ AT&T's help. Remote mgmt connection has been established. Pending service provisioning once install date has been set by PM. Adva IP: {ip_address}"

def CPW():
    return f"{get_datetime()} {user} CPW Complete"

def Pre_Install():
    return f"{get_datetime()} {user} Pre-Install Complete"

def Final_Install():
    return f"{get_datetime()} {user} Final Install Complete"

def Survey_Complete():
    return f"{get_datetime()} {user} Site Survey Complete, pending quote from vendor"
    
def Survey_Quote():
    return f"{get_datetime()} {user} Survey doc and quote attached to order"