import os, sys, subprocess

try:
    os.chdir('C:\\adb')
except Exception as e:
    print('Check adb root')
    sys.exit()

adb_devices_output = subprocess.run(['adb', 'devices'], capture_output=True, text=True)
if 'unauthorized' in adb_devices_output.stdout:
    input('USB 디버깅을 허용하고 Enter 다시 실행해주세요')
    sys.exit()
    
subprocess.run(['adb', 'shell', 'settings', 'put', 'system', 'csc_pref_camera_forced_shuttersound_key', '0'])
input('완료되었습니다. Enter를 눌러 종료해주세요.')
print('완료되었습니다')