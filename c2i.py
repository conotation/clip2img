from PIL import ImageGrab
from datetime import datetime
import os


img = ImageGrab.grabclipboard()

if img == None: # 이미지가 아닐 경우 예외처리
    raise SystemExit

ln = os.path.expanduser('~') + '\\Desktop\\C2I\\'
name = datetime.now().strftime('%Y%m%d-%H%M%S')

if not os.path.isdir(ln):
    os.mkdir(ln)

img.save(ln + name + '.png', 'PNG')