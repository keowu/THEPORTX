import re
import subprocess

class Serial:
    def getSeriais(self):
        msg = """
 _____ _         ______          _  __   __           _     _ 
|_   _| |        | ___ \        | | \ \ / /          | |   (_)   | |  
  | | | |__   ___| |_/ /__  _ __| |_ \ V /   ______  | |    _ ___| |_ 
  | | | '_ \ / _ \  __/ _ \| '__| __|/   \  |______| | |   | / __| __|
  | | | | | |  __/ | | (_) | |  | |_/ /^\ \          | |___| \__ \ |_ 
  \_/ |_| |_|\___\_|  \___/|_|   \__\/   \/          \_____/_|___/\__|
              """
        print msg;
        device_re = re.compile("Bus\s+(?P<bus>\d+)\s+Device\s+(?P<device>\d+).+ID\s(?P<id>\w+:\w+)\s(?P<tag>.+)$", re.I)
        df = subprocess.check_output("lsusb")
        devices = []
        for i in df.split('\n'):
            if i:
                info = device_re.match(i)
                if info:
                    dinfo = info.groupdict()
                    dinfo['device'] = '/dev/bus/usb/%s/%s' % (dinfo.pop('bus'), dinfo.pop('device'))
                    devices.append(dinfo)
        print devices