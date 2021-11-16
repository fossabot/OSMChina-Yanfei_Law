# OSMChina-Validator

规则中如果有node，way，relation共存同样内容的，可以用nwr表示

rule的mode如果是rule，就按照rule执行，否则作为单独的validator程序

### 依赖

[Keqing_Sword](https://github.com/OSMChina/OSMChina-Keqing_Sword)

### 使用

#### 面向一般用户

需要安装前置依赖库，需要在本项目的根目录下运行：

```python
pip install -r requirements.txt
```

首先下载Keqing_Sword，将keqing_my_waifu目录复制到本工具相同目录。正常情况下，可以看到keqing_my_waifu文件夹和branch_name_splitter文件在同一个文件夹中。

默认源文件为`src.osm`，目标文件为`dst.osm`。将待处理的文件命名为`src.osm`放置到本工具相同目录，双击运行`branch_name_splitter`即可，处理结果为`dst.osm`。

#### 面向IT业用户

命令行，-h，自己看。

### 注意

仅适用于中国内地的简体中文地区。

仅处理中文。

修改后请逐个人工检查修改结果！
