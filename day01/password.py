#标准输入的时候采用密文的方式输入密码
#首先倒入标准库getpass，在pycharm中无法交互，需要到命令行中执行

import getpass

name = input('name:')
password = getpass.getpass('pass')