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

## 注意事项

* **easy中的21.Merge_Two_Sorted_Lists**

```python
	return a or b
```

首先我是第一次见到这种写法，查看了官方文档，引用如下：

> The expression x and y first evaluates x; if x is false, its value is returned; otherwise, y is evaluated and the resulting value is returned.<br>
> The expression x or y first evaluates x; if x is true, its value is returned; otherwise, y is evaluated and the resulting value is returned.

也就是说，

> return x or y 先判断x，如果x为真返回其值；否则，判断y并返回结果值。<br>
> return x and y 先判断x，如果x为假，则返回其值；否则，判断y并返回结果值。
