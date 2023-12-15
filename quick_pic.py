import cv2
import numpy as np
import os
import random

def generate_random_points(img_shape, max_area):
    h, w = img_shape[:2]
    while True:
        points = [(random.randint(0, w), random.randint(0, h)) for _ in range(4)]
        if cv2.contourArea(np.array(points)) < max_area:
            return points

def process_images(folder_path, num_images=10, max_area_ratio=0.1):
    file_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.png')][:num_images]

    for i, file_path in enumerate(file_paths):
        img = cv2.imread(file_path)
        if img is None:
            continue

        original_img = img.copy()
        original_img = cv2.resize(original_img, (256, 256))
        white_img = 255 * np.ones_like(img)
        max_area = max_area_ratio * img.shape[0] * img.shape[1]

        points = generate_random_points(img.shape, max_area)
        cv2.fillConvexPoly(img, np.array(points), (0, 0, 0))
        cv2.fillConvexPoly(white_img, np.array(points), (0, 0, 0))

        resized_img = cv2.resize(img, (256, 256))
        resized_white_img = cv2.resize(white_img, (256, 256))

        cv2.imwrite(os.path.join(f"D:\web_load\RePaint-main\data\data_test\gts\origin{i}.png"), original_img)
        cv2.imwrite(os.path.join(f"D:\web_load\RePaint-main\data\data_test\gt_keep_masks\\black{i}.png"), resized_white_img)
        cv2.imwrite(os.path.join(f"D:\web_load\RePaint-main\data\data_test\gt_keep_masks\\pic_black{i}.png"), resized_img)

# 使用示例
process_images('D:\web_load\RePaint-main\ceramic')
