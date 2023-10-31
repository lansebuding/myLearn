"""
套接字
"""

import socket

"""
网络类型：1.ipv4---PC  2.ipv6----移动端
套接字类型：1.udp  2.tcp
"""


def mains():
    socketObject = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    socketObject.sendto(b'abc',('192.168.20.2',8080))
    # 释放端口
    socketObject.close()


if __name__ == "__main__":
    mains()