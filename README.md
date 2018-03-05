# leetcode

leetcode刷题笔记

## 注意事项

* easy中的21.Merge_Two_Sorted_Lists

```python
	return a or b
```

首先我是第一次见到这种写法，查看了官方文档，引用如下：
> The expression x and y first evaluates x; if x is false, its value is returned; otherwise, y is evaluated and the resulting value is returned.
> The expression x or y first evaluates x; if x is true, its value is returned; otherwise, y is evaluated and the resulting value is returned.
也就是说，
> return x or y 先评估x，如果x为真返回其值；否则，评估y并返回结果值。
> return x and y 先评估x，如果x为假，则返回其值；否则，评估y并返回结果值。
