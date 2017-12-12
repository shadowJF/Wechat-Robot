# 微信机器人

基于[itchat](https://github.com/littlecodersh/ItChat)的python微信机器人

后台机器人服务需要自己提供

## 启动

python start.py

启动后，用手机微信扫描二维码登录即可

这个项目其实和我们自己的机器人服务有比较深度的结合了

所以，只是给你们一个思路，如何做一个微信机器人 ┑(￣Д ￣)┍

## 环境搭建

**安装python3**

安装python依赖环境

yum install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc make

./configure --prefix=/usr/local/python3

make && make install

ln -s /usr/local/python3/bin/python3 /usr/bin/python3
ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3
ln -s /usr/local/python3/bin/easy_install-3.6 /usr/bin/easy_install-3.6

**安装itchat**

pip3 install itchat

**安装Flask**

pip3 install Flask

**安装pydub**

pip3 install pydub

**安装ffmpeg**

下载ffmpeg-git-64bit-static.tar.xz，直接解压

在/etc/profile最后加上

export PATH=/data/ffmpeg-git-20171124-64bit-static:$PATH