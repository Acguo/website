import re

ss = """<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0" name="viewport" /> 
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>金蝉脱壳2：冥府</title>
<script src="/js/jquery.min.js" type="text/javascript"></script>
<link href="/js/style.css" rel="stylesheet">
</head>
<body>
<div id="a1" class="player"><iframe id="player" width="100%" height="100%" allowfullscreen="true"  scrolling="no" frameborder="0"  border="0" marginwidth="0" marginheight="0"  src="//jx.618g.com/m3u8.php?url=https://youku.cdn-163.com/20180615/7524_12e995e8/index.m3u8"></iframe></div>
<div style="display:none"><script src="https://s13.cnzz.com/z_stat.php?id=1273559864&web_id=1273559864" language="JavaScript"></script><!--okzy--></div>
<div style="display:none"><script></script></div><div style="display:none"><script src="https://s13.cnzz.com/z_stat.php?id=1273075720&web_id=1273075720" language="JavaScript"></script></div></body>
</html>"""
result = re.findall("<div id=\"a1\" class=\"player\">(.*?)</div>",ss)
print(result)