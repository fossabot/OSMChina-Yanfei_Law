# OSMChina-Validator

##　中文拷贝器

### 使用示例

把有name但没有name:zh标签的点，设置name:zh为name的值。


## 分支名称分割器

用于OSM数据处理的分支名称分割器。

### 功能

将银行（未来可能支持更多）分行的name标签中的分支名称（如“某某分行”）移动到branch标签中，同时去掉name标签中分支名称，以此规范化名称标记。

例如，中国银行北京市分行，假设其标签如下
```
name=中国银行北京市分行
```
其标签会被处理为
```
name=中国银行
name:zh=中国银行
full_name=中国银行北京市分行
branch=北京市分行
```

### 特性

+ 处理node、way、relation
+ 处理银行（`amenity=bank`）
+ 分支名称支持`分行`、`支行`
+ 自动设置`name:zh`为`name`相同的值
+ 自动设置`full_name`为包含“某某分行”的值
+ 括号会被忽略，并兼容全角、半角括号，兼容圆、方、花括号和各种奇怪的括号，即`中国银行北京市分行`、`中国银行(北京市分行）`都会被处理成一样。
+ 输出处理前后差异比对

### 依赖

[Keqing_Sword](https://github.com/OSMChina/Keqing_Sword)

### 使用

#### 面向一般用户

首先下载Keqing_Sword，将keqing_my_waifu目录复制到本工具相同目录。正常情况下，可以看到keqing_my_waifu文件夹和branch_name_splitter文件在同一个文件夹中。

默认源文件为`src.osm`，目标文件为`dst.osm`。将待处理的文件命名为`src.osm`放置到本工具相同目录，双击运行`branch_name_splitter`即可，处理结果为`dst.osm`。

#### 面向IT业用户

命令行，-h，自己看。

### 注意

仅适用于中国内地的简体中文地区。

仅处理中文。

修改后请逐个人工检查修改结果！
