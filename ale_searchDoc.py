#coding=utf-8
import os #os.path模块是Python中OS模块的子模块，用于通用路径名操作。
import time
import shutil #对文件的复制与删除操作更是比较支持好
import subprocess

def findfile(path):
    try:
        items = os.listdir(path) #返回指定的文件夹包含的文件或文件夹的名字的列表
        for item in items:
            file = os.path.join(path, item)#os.path.join(路径，目标路径，文件) 这里item集合了 目标路径和文件
            if not os.path.isdir(file): #os.path.isdir(file 文件；if判断的是不是文件夹，如果不是文件夹，就拷贝
                for ext in ['.doc', '.docx']:
                    if file.endswith(ext):#endswith() 方法用于判断字符串是否以指定后缀结尾，如果以指定后缀结尾返回True，否则返回False
                        print('Found file: %s' % file)
                        dest_file = os.path.join(doc_bak_path, item)
                        shutil.copyfile(file, dest_file)
            else:
                findfile(file)#是文件夹，就继续遍历
    except PermissionError as error:
        pass
    except:
        pass


if __name__ == '__main__':
    drives = str(subprocess.check_output("fsutil fsinfo drives").strip(), encoding='gbk').split()[1:]
    while True:
        drives_new = str(subprocess.check_output("fsutil fsinfo drives").strip(), encoding='gbk').split()[1:]
        udisk = list(set(drives_new).difference(set(drives)))
        if udisk:
            udisk_path = udisk[0]
            print('检测到U盘，开始拷贝文件')

            doc_bak_path = os.path.join(udisk_path, 'doc_files')

            if os.path.exists(doc_bak_path):
                shutil.rmtree(doc_bak_path)
                os.mkdir(doc_bak_path)
            else:
                os.mkdir(doc_bak_path)

            print('备份文件路径：%s' % doc_bak_path)

            for drive in drives:
                findfile(drive)
            time.sleep(5)
            print('拷贝完成')
            break
        else:
            print('未检测到U盘，请插入U盘')
            time.sleep(3)
"""
import shutil
# 将文件内容拷贝到另一个文件中
shutil.copyfileobj(open('old.txt', 'r'), open('new.txt', 'w'))

# 拷贝文件
shutil.copyfile('old.txt', 'old1.txt')

# 仅拷贝权限。内容、组、用户均不变
shutil.copymode('old.txt', 'old1.txt')
# 复制权限、最后访问时间、最后修改时间
shutil.copystat('old.txt', 'old1.txt')
# 复制一个文件到一个文件或一个目录
shutil.copy('old.txt', 'old2.txt')
# 在copy上的基础上再复制文件最后访问时间与修改时间也复制过来了
shutil.copy2('old.txt', 'old2.txt')
# 把olddir拷贝一份newdir，如果第3个参数是True，则复制目录时将保持文件夹下的符号连接，如果第3个参数是False，则将在复制的目录下生成物理副本来替代符号连接
shutil.copytree('C:/Users/xiaoxinsoso/Desktop/aaa', 'C:/Users/xiaoxinsoso/Desktop/bbb')
# 移动目录或文件
shutil.move('C:/Users/xiaoxinsoso/Desktop/aaa', 'C:/Users/xiaoxinsoso/Desktop/bbb') # 把aaa目录移动到bbb目录下
# 删除一个目录
shutil.rmtree('C:/Users/xiaoxinsoso/Desktop/bbb') # 删除bbb目录
"""

"""
 def getUdisk():
        # 运行时盘符列表
        fullDisks = psutil.disk_partitions()
        print(fullDisks)
        newDisks = psutil.disk_partitions()
        # 比较磁盘的不同，求集差
        newDisks = list(set(newDisks).difference(set(fullDisks)))
        while newDisks:
            if fullDisks != newDisks:
                print("未检测到U盘")
                time.sleep(3)
            else:
                print("检测到U盘，开始拷贝文件")
                global doc_bak_path
                doc_bak_path = os.path.join(newDisks, 'doc_files')
                if os.path.exists(doc_bak_path):
                    shutil.rmtree(doc_bak_path)
                    os.mkdir(doc_bak_path)
                else:
                    os.mkdir(doc_bak_path)
                    print('备份文件路径：%s' % doc_bak_path)
                    for disk in newDisks:
                        findfile(disk)
                        time.sleep(5)
                        print('拷贝完成')
                        break
"""