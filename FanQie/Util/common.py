Android = False
iPhone = True
iphone_Simulator = False
if Android:
    find_device = 'adb device'
else:
    find_device = 'idevice_id -l'