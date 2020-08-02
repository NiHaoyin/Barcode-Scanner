import commands.commands as commands


book = {
    "help": commands.call_help,  # 列出所有命令的用法
    "scan": commands.scan,  # 扫描单个图片，将扫描出的结果存入缓冲区
    "scanall": commands.scan_all,  # 扫描整个文件夹下的所有图片，将扫描出的结果存入缓冲区
    "print": commands.show_buffer,  # 在终端打印缓冲区
    "saveto": commands.save,  # 将缓冲区中的扫描结果存入excel文件
    "exit": commands.exit_program,  # 退出程序
}

# 新建缓冲区
res_buffer = list()
file_buffer = list()
# 新建命令
command = input("->")
while command != "exit":
    c = command.split(" ")
    if c[0] not in book:
        print("wrong command!")
        continue
    # 得到图片路径
    path = c[1]
    # 得到执行函数
    func = book[c[0]]
    # 更新buffer
    func(path, res_buffer, file_buffer)
    print(res_buffer, file_buffer)





