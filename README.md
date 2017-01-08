# translate
    python baidu api translator
    python 3.5 
    osx 10.11 
    use baidu translate api 
    it is a translator can translate multiple words or sentence into diff language 
# data wait to translate
you may format your data like this by using regular expressions or replace
--------
    hello
    your brother
    cool thing
    amazing
translate result is like this
-----
    'hello' : '你好'
    'your brother' : '你的哥哥'
    'cool thing' : '酷'
    'amazing' : '鹅妹z樱'
# How to Use
    git clone this project 
    git clone 
    http://api.fanyi.baidu.com/api/trans/product/index 注册 获取自己的 appid 和secretkey
    python path/to/this/script waitForTransFileName result fromLan toLang appid secretkey
    例如 你需要翻译的文件名为 waitForTrans.txt中文zh 翻译到 result.txt英文en 文件 
    那就是
    python c/Download/translateToDiffLang waitForTrans.txt result.txt zh en your_appid your_secretkey
<div>
<h3>language arguments</h3>
<table class="info-table">
<tbody><tr>
<th>语言简写</th>
<th>名称</th>
</tr>
<tr>
<td>auto</td>
<td>自动检测</td>
</tr>
<tr>
<td>zh</td>
<td>中文</td>
</tr>
<tr>
<td>en</td>
<td>英语</td>
</tr>
<tr>
<td>yue</td>
<td>粤语</td>
</tr>
<tr>
<td>wyw</td>
<td>文言文</td>
</tr>
<tr>
<td>jp</td>
<td>日语</td>
</tr>
<tr>
<td>kor</td>
<td>韩语</td>
</tr>
<tr>
<td>fra</td>
<td>法语</td>
</tr>
<tr>
<td>spa</td>
<td>西班牙语</td>
</tr>
<tr>
<td>th</td>
<td>泰语</td>
</tr>
<tr>
<td>ara</td>
<td>阿拉伯语</td>
</tr>
<tr>
<td>ru</td>
<td>俄语</td>
</tr>
<tr>
<td>pt</td>
<td>葡萄牙语</td>
</tr>
<tr>
<td>de</td>
<td>德语</td>
</tr>
<tr>
<td>it</td>
<td>意大利语</td>
</tr>
<tr>
<td>el</td>
<td>希腊语</td>
</tr>
<tr>
<td>nl</td>
<td>荷兰语</td>
</tr>
<tr>
<td>pl</td>
<td>波兰语</td>
</tr>
<tr>
<td>bul</td>
<td>保加利亚语</td>
</tr>
<tr>
<td>est</td>
<td>爱沙尼亚语</td>
</tr>
<tr>
<td>dan</td>
<td>丹麦语</td>
</tr>
<tr>
<td>fin</td>
<td>芬兰语</td>
</tr>
<tr>
<td>cs</td>
<td>捷克语</td>
</tr>
<tr>
<td>rom</td>
<td>罗马尼亚语</td>
</tr>
<tr>
<td>slo</td>
<td>斯洛文尼亚语</td>
</tr>
<tr>
<td>swe</td>
<td>瑞典语</td>
</tr>
<tr>
<td>hu</td>
<td>匈牙利语</td>
</tr>
<tr>
<td>cht</td>
<td>繁体中文</td>
</tr>
</tbody></table>

</div>
