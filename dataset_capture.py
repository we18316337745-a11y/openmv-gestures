"""手势数据采集用画面：不叠加方框、十字或文字。

在 OpenMV IDE 中新建/打开数据集、运行本脚本并选择类别后，
使用 IDE 的 Capture Data 功能将当前画面保存到电脑。
本脚本本身不向摄像头存储器写图片。
"""

import sensor
import time

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_vflip(True)
sensor.set_hmirror(True)
sensor.skip_frames(time=2000)
sensor.set_auto_gain(False)
sensor.set_auto_whitebal(False)

while True:
    img = sensor.snapshot()
