import scanner.scanner as scanner
from os import listdir
import numpy as np


def call_help():
    print("Commands include:")
    print("scan <图片路径> : 扫描条形码并将扫描结果加入buffer中")
    print("scan <文件夹路径> : 扫描文件夹下所有条形码并将扫描结果加入buffer中")
    print("print buffer : 打印当前buffer中的扫描结果")
    print("saveto <新建文件名> : 将结果保存在.csv文件中")


scan_failure = "Unable to scan the code"


# 输入图片路径，返回填入扫描结果的buffer
def scan(img_path, res_buffer, file_buffer):
    decoded_barcode = scanner.scan_barcode(img_path)
    origin_len = len(res_buffer)
    res_buffer.append(decoded_barcode)
    file_buffer.append(img_path)
    current_len = len(res_buffer)
    print("Finish scanning. Add %d decoded message." % (current_len - origin_len))


# 输入文件夹路径和buffer，返回填入扫描结果的buffer
def scan_all(dir_path, res_buffer, file_buffer):
    files = listdir(dir_path)  # 得到文件夹下所有文件的名称
    origin_len = len(res_buffer)
    for file in files:
        file = dir_path + '/' + file
        decoded_barcode = scanner.scan_barcode(file)
        # 如果扫描结果为空，则不将扫描结果填入buffer
        # if decoded_barcode is []:
        #     decoded_barcode.append("Null")
        res_buffer.append(decoded_barcode)
        file_buffer.append(file)
    current_len = len(res_buffer)
    print("Finish scanning. Add %d decoded message." % (current_len-origin_len))


def save(path, res_buffer, file_buffer):
    path = path + '.csv'
    np.savetxt(path, np.column_stack((file_buffer, res_buffer)), delimiter=',',
               fmt='%s', header='File name,Decoded message', comments='')
    print('File saved')


def show_buffer(path, res_buffer, file_buffer):
    for i in range(0, len(res_buffer)):
        print("The image:", file_buffer[i])
        print("The decoded message:", res_buffer[i])


def exit_program():
    print("Goodbye")

