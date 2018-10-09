# 1.导入库
# import cv2
# # 2.打开摄像头
# Capture = cv2.VideoCapture(0)
# # 3.获取摄像头实时画面
# cv2.namedWindow("摄像头")
# while True:
#     # 3.1 读取摄像头的帧画面
#     ret,frame = Capture.read()
#     # 3.2显示图片(渲染画面)
#     cv2.imshow("james",frame)
#     # 3.3暂停窗口
#     if cv2.waitKey(5) & 0xFF == ord('q'):
#         break
# # 4.释放资源
# Capture.release()
# # 5.关闭窗口
# cv2.destroyAllWindows()
# ===============================
# 1.导入库
import cv2
# 2.加载人脸模型
face = cv2.CascadeClassifier("")
# 3.打开摄像头
Capture = cv2.VideoCapture(0)

# 4.创建窗口
cv2.namedWindow("shexiangtou")
# 5.获取摄像头实时画面
while True:
#     # 5.1 读取摄像头的帧画面
    ret,frame = Capture.read()
#     # 5.2调整图片灰度
    gray = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
#     # 5.3暂停窗口（括号里是像素格大小）
    faces = face.detectMultiScale(gray,1.1,3,0,(100,100))
    # 标记人脸
    for (x, y, w, h) in faces:
        # 四个参数 1.图片 2.坐标原点 3.识别大小 4.颜色 5.线宽
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 10)
    # 显示图片
        cv2.imshow("shexiangtu",frame)
    # 暂停窗口
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break
# 6.释放资源
Capture.release()
# 7.关闭窗口
cv2.destroyAllWindows()

