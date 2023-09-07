import cv2
import time
from datetime import datetime, timedelta

# 初始化 VideoCapture 物件
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# 設定 FPS 為 20
fps = 10
delay = int(1000 / fps)

# 初始化變數
show_frame = True
frame = None

# 滑鼠回調函數，用於捕捉滑鼠事件
def mouse_callback(event, x, y, flags, param):
    global show_frame
    if event == cv2.EVENT_LBUTTONDOWN:
        show_frame = not show_frame
        cv2.putText(frame, f'{GMT8_time.strftime("%Y/%m/%d %H:%M:%S")} stop', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
        cv2.imshow("WebCam", frame)

# 設定滑鼠回調函數
cv2.namedWindow("WebCam")
cv2.setMouseCallback("WebCam", mouse_callback)

while True:
    # 讀取一幀影像
    if show_frame:
        ret, frame = cap.read()
        if ret:           # 如果成功讀取，則顯示
            GMT8_time = datetime.utcnow() + timedelta(hours=8)
            cv2.putText(frame, GMT8_time.strftime("%Y/%m/%d %H:%M:%S"), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2, cv2.LINE_AA)
            cv2.imshow("WebCam", frame)

    # 檢查是否按下 'Esc' 鍵
    if cv2.waitKey(delay) == 27:
        break
        
    if cv2.getWindowProperty('WebCam', cv2.WND_PROP_VISIBLE) < 1:
        print("ALL WINDOWS ARE CLOSED")
        break

# 釋放 VideoCapture 物件和銷毀所有 OpenCV 視窗
cap.release()
cv2.destroyAllWindows()
