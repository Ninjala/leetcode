# leetcode

leetcode刷题笔记

## 知识归纳

### Python字符串函数

* *str.index()与str.find()*

> [**index()介绍**](http://www.runoob.com/python/att-string-index.html)

> [**find()介绍**](http://www.runoob.com/python/att-string-find.html)

* *str.strip()*

> [**strip()介绍**](http://www.runoob.com/python/att-string-strip.html)

### Python内置函数 

[**bin()介绍**](http://www.runoob.com/python/python-func-bin.html)

[**eval()介绍**](http://www.runoob.com/python/python-func-eval.html)

[**map()介绍**](http://www.runoob.com/python/python-func-map.html)

### 算法

#### BFS与DFS

 **广度优先搜索BFS(Breadth First Search)**

> 使用队列保存未被检测的结点。结点按照宽度优先的次序被访问和进出队列。

> *eg:* 你的眼镜掉地上，你总是先从离你最近的地方摸索，如果没有，再摸远一点的地方...

 **深度优先搜索DFS(Depth First Search)**

> 使用栈保存未被检测的结点，结点按照深度优先的次序被访问并依次被压入栈中，并以相反的次序出栈进行新的检测。

> *eg:* 走迷宫 -- 不撞南墙不回头...

* [**BFS与DFS介绍**](https://www.cnblogs.com/gczr/p/6476577.html)


## 注意事项

* **easy：21.Merge_Two_Sorted_Lists**

```python
	return a or b
```

首先我是第一次见到这种写法，查看了官方文档，引用如下：

> The expression x and y first evaluates x; if x is false, its value is returned; otherwise, y is evaluated and the resulting value is returned.

> The expression x or y first evaluates x; if x is true, its value is returned; otherwise, y is evaluated and the resulting value is returned.

也就是说，

> return x or y 先判断x，如果x为真返回其值；否则，判断y并返回结果值。

> return x and y 先判断x，如果x为假，则返回其值；否则，判断y并返回结果值。
