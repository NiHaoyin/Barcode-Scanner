from cv2 import imread
import pyzbar.pyzbar as pyzbar


# 输入图像路径，返回该图片中所有二维码信息的list
def scan_barcode(img_path):
    img = imread(img_path)
    # gray = cvtColor(img, cv2.COLOR_RGB2GRAY)
    # print(img)
    texts = pyzbar.decode(img)
    res = list()
    # 输出结果
    for text in texts:
        tt = text.data.decode("utf-8")
        res.append(tt)
    # print(res)
    return res




