import cv2
import numpy as np

# 初始化点的列表
points = []



# 回调函数，用于处理鼠标点击事件
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        if len(points) < 4:
            points.append((x, y))

        # 当四个点被点击时，绘制一个黑色四边形
        if len(points) == 4:
            cv2.fillConvexPoly(img, np.array(points), (0, 0, 0))
            cv2.fillConvexPoly(white_img, np.array(points), (0, 0, 0))
            cv2.imshow('image', img)
            # 保存更改后的图片
            resized_img = cv2.resize(img, (256, 256))
            resized_white_img = cv2.resize(white_img, (256, 256))
            cv2.imwrite('D:\web_load\RePaint-main\data\data_test\gts\edited_image.png', resized_img)
            cv2.imwrite('D:\web_load\RePaint-main\data\data_test\gt_keep_masks\\black_shape_on_white.png', resized_white_img)


# 加载图片
img = cv2.imread('D:\web_load\RePaint-main\ceramic\\0D632AAF6052FDCB80866ACF2D2C249E.png')  # 替换成你的图片路径
original_img = img.copy()
origin = cv2.resize(original_img, (256, 256))
cv2.imwrite('/data/data_test/gts/origin.png', origin)
# 创建一个白色的图片，与原图大小相同
white_img = 255 * np.ones_like(img)

cv2.imshow('image', img)
# 设置鼠标回调函数
cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
