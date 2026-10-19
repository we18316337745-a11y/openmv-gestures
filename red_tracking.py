"""OpenMV H7 红色跟踪：输出目标中心和相对画面中心的偏差。"""

import sensor
import time

# 由实际场景中的阈值编辑器调出；换光照或目标后可能需要重调。
RED_THRESHOLD = (0, 100, 31, 127, -128, 127)

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
    blobs = img.find_blobs(
        [RED_THRESHOLD],
        pixels_threshold=150,
        area_threshold=150,
        merge=True,
    )

    if blobs:
        target = max(blobs, key=lambda blob: blob.pixels())
        x = target.cx()
        y = target.cy()

        img.draw_rectangle(target.rect(), color=(0, 255, 0))
        img.draw_cross(x, y, color=(0, 255, 0), size=10)

        x_error = x - img.width() // 2
        y_error = y - img.height() // 2
        print("x:", x, "y:", y,
              "x_error:", x_error, "y_error:", y_error)
