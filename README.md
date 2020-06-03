# web_robot
自动化网页操作

## 详细说明
请见博客
[使用教程](http://ganjiacheng.cn/article/article_18_chrome%E6%8F%92%E4%BB%B6-%E7%BD%91%E9%A1%B5%E8%87%AA%E5%8A%A8%E5%8C%96/)

## 已有功能
1. 管理多个事务，每个事务有多个过程，每个过程对应一种操作   
2. 新增操作中方便的页面元素筛选器，css/id筛选器
3. 测试运行一个过程，运行一个事务，运行转为background后台   
4. 支持事务的导入导出
5. 支持源码事务
6. 支持本地鼠标键盘受控执行事务

## 使用方法
1. 浏览器设置（三个点）--> 更多工具 --> 扩展程序 ↓  
2. 打开右上角开发者模式 --> 加载已解压的扩展程序 --> 选择clone下来的该项目根目录 ↓  
3. 弄完可关掉开发者模式 --> 右键项目图标 --> 检查可读取和更改网站数据 --> 在所有网站上

### 受控运行，开启本地web服务

4. 首先准备一个python3虚拟环境或本地python3运行环境
5. pip下载 py/requirements.txt 里的包
6. 启动web服务 **python py/web.py**

## 版本迭代

v1.0 
1. 管理多个事务，每个事务有多个过程，每个过程对应一种操作   
2. 新增操作中方便的页面元素筛选器，css/id筛选器
3. 测试运行一个过程，运行一个事务，运行转为background后台   
4. 支持事务的导入导出

v1.1
1. 支持源码事务

v1.2
1. 新增事务受控运行模式，运行于background中
2. 新增本地web服务，用于鼠标键盘模拟流程的受控执行

v1.2.1
1. 删除事务新增校验
2. 实现流程中事件的复制，移动，编辑

## 感谢轮子
1. [materializecss](http://www.materializecss.cn/about.html)
3. [官方轮子](https://developer.chrome.com/extensions)
4. [插件教程](https://www.cnblogs.com/liuxianan/p/chrome-plugin-develop.html)
