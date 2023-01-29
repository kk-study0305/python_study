import os
import cv2
import numpy as np
from sklearn.svm import SVC
import flask

# 渡された複数のサンプル画像を読み込む
samples = []
for file in os.listdir("path/to/sample_images"):
    if file.endswith(".jpg"):
        img = cv2.imread(os.path.join("path/to/sample_images", file))
        samples.append(img)

# 読み込んだ画像を解析し、人間が写り込んでいる部分について機械学習する
# (ここでは、画像をグレースケールに変換し、SVMによる分類器を訓練している)
gray_samples = [cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) for img in samples]
flat_samples = [img.flatten() for img in gray_samples]
clf = SVC()
clf.fit(flat_samples, [1]*len(samples))

# 機械学習の結果を活かし、読み込んだ画像に人間が映っているか判別する
test_img = cv2.imread("path/to/test_image.jpg")
gray_test_img = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)
flat_test_img = gray_test_img.flatten()
result = clf.predict([flat_test_img])

# 人間が映っている場合はその部分を強調表示する
if result[0] == 1:
    # 人間が映っている部分を検出する処理
    # (ここでは、OpenCVのHOG+SVMによる人検出を使用)
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    human, _ = hog.detectMultiScale(gray_test_img)
    # 人間が映っている部分を矩形で囲む
    for (x, y, w, h) in human:
        cv2.rectangle(test_img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow("Human Detection", test_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

