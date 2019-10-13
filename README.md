## PYTHON控制台单词实时翻译工具

CZQ 20191013 10:52

需要先安装翻译工具 sudo npm install terminal-translate -g
实时监听复制操作，满足条件的英文单词就进行翻译，这样电脑上就不需要安装翻译工具了

注意：ubuntu系统如果要支持剪贴板监听，需要安装依赖1个就可以 sudo apt-get install xsel
https://pyperclip.readthedocs.io/en/latest/introduction.html#not-implemented-error


## 系统
ubuntu 16.04

## 依赖
sudo pip3 install pyperclip
sudo npm install terminal-translate -g
sudo apt-get install xsel

## 运行
python3 clip_tl.py
