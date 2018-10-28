import os 

尺寸　overflow:auto;
边框　border : border-width border-style(solid dashed dotted double) color
    border-radius 
    border-top
    border-bottom
    border-left
    border-right
    网页三角标　
            空的块元素　宽高为0 等宽边框　三个设置为透明
轮廓线　　outline : none
圆角边框 : border-radius

div : 没有border marigin的值

1．  外边距
    １．外边距
        1.垂直方向上的外边距，会发生合并，取较大的值
        2.水平方向上的外边距，会发生叠加，元素之间的较大
        3.为子元素添加距上的外边距，但是会作用于父元素上（子元素上边框与父元素重叠）因为上下边框取大值　这时候需要给父元素设置一个上边框，或者给父元素设置一个内上边框
            解决办法　：　
                １．为父元素设置上边框（可以使用透明色）border-top:0.1px solid transparent;
                ２．为父元素添加顶部的内边距padding-top:0.1px;

2.  内边距
    １．元素内容与元素边框之间的距离　，称为内边距
    ２．属性：　padding 
        取值：　像素或者百分比　
            １．padding:10px;
                设置上下左右四个方向的内边距
            ２．padding:10px 20px;
                设置上下内边距为10，左右内边距为20 

            3. padding:10px 20px 30px;
                设置上下内边距分别为10 30  左右内边距为20
1342 上下左右原则
            4. padding:10px 20px 30px 40px;
                设置上右下左四个方向内边距

    3. 单方向内边距的设置
        １．属性　：
            padding-top:距上的内边距
            padding-bottom:
            padding-left:
            padding-right:
        2.  取值为像素值　

    4.默认带有内边距的元素    
        ol ul input td　

    5.清除浏览器的默认内外边距
        body,h1,h2,h3,h4,h5,h6,p,ul,ol,input{
        marigin:0;
        padding:0;
        }

3.  设置盒模型的计算方式
    et:
        div{
        width:200px;
        height:200px;
        border:10px solid red;
        marigin:10px;
        padding:10px;
        }
        div 在文档中实际占据的尺寸为　260*260
    有空白间隙的时候　把元素共行书写　因为换行也是一个空白符号　

    1 .　属性　: box-sizing
        作用 : 指定盒模型的计算方式
        取值 : 
            1.content-box : 默认值　
                元素的width height属性只用来规定内容的尺寸，如果元素设置内外边距和边框
                最终在文档中占据的尺寸由各种值相加得到

            2.border-box 
                元素的width height属性，规定的是包含边框，内边距和内容在内的尺寸
            border　以内的

            解决行内元素水平缝隙问题：
               　１ 父元素中设置字体大小为0 解决子元素水平方向上的间隙 (空格也有像素值　直接设置0就没有了)
                    注意子元素需要重新设置字体大小  font-size:0;
                ２．子元素并行书写(空格也是一个字体)   也可以使用浮动float

4.  元素的显示设置　
    １．设置元素的可见性
        属性　:  visibility
        取值　: 
            1. visible  默认值，元素可见
            2. hidden   设置元素隐藏，元素在文档中仍然占位

    ２．转换元素类型　
        属性　：　display
        取值　：　　　
            1.  block : 转换为块元素
            2.  inline : 转换为行内元素　
            3.  inline-block : 转换为行内块元素　
先设置子元素是隐藏元素
父元素是伪类，子元素设置成块元素就可以实现简单的菜单

        特殊取值 
            4.   none 实现元素隐藏　元素在文档中不占位，其他元素相应移动

        实现元素的隐藏与显示:    
                display : none; 隐藏
                display : block; 显示  变成块元素 不工行显示
                作业　：
                    实现下拉菜单
                    １．使用列表或其他结构完成下拉菜单
                        et:
                            北京　
                        菜单　：　深圳　．．
                    ２．　当鼠标悬停在文本上时候　比如北京上时候，　显示下拉菜单　
                        鼠标移除时，隐藏下拉菜单　
5,  背景相关的属性　
    １．backgroud-color
        设置背景颜色，取颜色值
        注意：
            １．所有元素默认的背景颜色都是透明色，新建窗口的白色不是body的背景色
                是浏览器渲染的结构
            ２．背景颜色是从元素的边框位置开始绘制的，如果颜色添加内边距，
                都会被渲染成相应的背景颜色

    2.  背景图片

        １．设置背景图片
            属性　：　background-image
            取值　：　url()  如果路径中出现中文　最好加引号　
            注意　：　
                    １．背景图片的尺寸如果大于元素尺寸，图片仍然按照原始尺寸显示，
                        超出的元素部分不可见
                    ２．背景图片的尺寸小于元素尺寸，浏览器会自动对背景图片重复平铺，知道铺满元素

                    3.  背景图片与背景颜色一样，不影响元素正常内容显示　　　

        ２．设置背景图片的重复方式
            图片尺寸不够时候，浏览器会自动沿水平和垂直两个方向对图片进行重复平铺，
            直到铺满为止

            属性　：　background-repeat
            取值　：　　
                １．repeat : 默认值　，沿水平和垂直方向平铺
                ２．repeat-x : 沿水平方向平铺
                ３．repeat-y : 沿垂直方向平铺
                ４．no-repeat : 设置背景图片不重复平铺
            　　　　　　　　　　　　　
        3.  设置背景图片的位置　
            1.属性　：　background-position
            2.取值　：　x y
                1. 取像素值　：　
                    x : 表示背景图片水平方向的偏移距离　
                            正值表示图片向右偏移
                            负值表示图片向左偏移

                    y : 背景图片垂直方向的偏移距离
                            正值表示图片向下偏移
                            负值表示图片向上偏移

                    结合'精灵图'实现元素背景图片调整

                2.  百分比
                        参照元素尺寸计算水平和垂直偏移距离
                        1.0% 0% 
                            背景图片显示在元素左上角　
                        2.50% 50% 
                            背景图片显示在元素中间　
                        3.100% 100% 
                            背景图片显示在右下角　
                3.  方位值确定背景图片的位置　
                    x : left / center / right 
                    y : top / center / right
323 155
        4.  设置背景图片大小　
                １．属性　：　background-size 
                ２．取值　：　x y 
                    x y 分别表示背景图片的宽和高　
                    １　像素值　
                    ２　百分比　：　参照元素宽高尺寸计算背景图片大小　
                    ３　cover : 表示将图片等比放大至完全铺盖元素
                    ４ contain : 表示将图片等比拉伸至刚好被元素容纳
                                不能超出元素尺寸　

        5. 背景属性简写　
                １，属性　：　background 
                ２．取值　：　color url() repeat position 
                注意　：　
                    １．背景属性按照一定顺序设置　
                    ２．background-size 单独设置　
                    ３．可以省略属性值　，单独设置颜色，或者背景图片　

6.  文本相关的属性　
    １．字体相关的属性
        １．字体大小
            属性　：　font-size
            取值　：　像素值或em 1em = 16px 

        ２．字体粗细程度
            属性　：　font-weight
            取值　：　
                １．关键字　light / normal(正常) / bold(加粗)
                ２．整百数值　100-900,数值越大，字体越粗
                    100(lighter) - 400(normal) - 700(bold) -900(bolder)
        ３．字体名称：
            １．属性：font-family
            ２．取值：

            注意　：　
                １．如果字体名称是中文或者由多个英文单词组成，需要使用引号引起来
                    et:
                      font-family : '微软雅黑'
                      font-family : 'Microsoft YaHei'
                      font-family : Arial;
                      font-family : serif;

                ２．同时指定多个字体名称，之间使用英文逗号间隔
                    当浏览器不支持第一种字体时，会按照顺序依次以后面指定字体名称显示
                    et:
                        font-family : '黑体','微软雅黑','宋体'

        4.  字体样式（是否采用斜体）
            １．属性　：　font-style
            ２．取值　：　
                    １．normal 正常显示
                    ２．italic 斜体显示　
                    ３．oblique 倾斜显示　
                    注意　：　oblique 可以将字体倾斜一定角度，默认倾斜效果与
                            italic斜体没有差别　

        5.字体属性简写　
            １．属性　：　font
            ２．取值　：　style weight size family;
                注意　：　
                    １．同时设置四个属性值时，参照给定顺序书写　
                    ２． font-family是必填项，不能省略　　
                    ３．　font-size 和　font-family 是必填项，不能省略　
149,191,112
    ２．　文本相关的属性　
        １．文本颜色
            １．属性　：　color 
            ２．取值　：　颜色值

        ２．文本装饰线
            １．属性　：　text-decoration 
            ２．取值　：　
                １．underline : 下划线
                ２．overline : 上划线　
                ３．line-through : 删除线
                ４．none : 取消文本装饰线　

        ３　文本水平对齐方式
            １．属性　：　text-align
            ２．取值　：
                １．left(默认值) / center /right
                ２.　justify 两端对齐　

        ４．设置行高　
            行高只一行文本所占的高度
            １．属性　：　line-height  
            ２．取值　：　像素值或em

            用法：
                １．设置行高与元素高度相同，实现一行文本的垂直居中　
                ２．line-height > height ,文本会下移
                ３．line-height < height , 文本会上移　

            注意　：　
                文本内容在当前行中始终是垂直居中的　　
                行高不能比字体大小小　负责会重叠在一起　

            特殊取值　：
                取无单位的数值，表示当前字体大小的倍数，由此计算行高
                et:
                    p{
                    font-size:20px;
                    line-height:2;(当前行高为字体大小的2倍，40px)
                    }

7.  表格相关的属性
    １．基础样式是通用的
    ２．独有的CSS:
        1.边框合并
            属性　：　border-collapse 
            取值　：

            　
                1.Seperate : 默认值，单元格边框与表格边框　
                2.collapese : 设置表格边框与单元格边框合并

            注意　：
                1.td 不支持margin 
                2.border-collapse只能在table中使用　，其他元素不能使用

        ２．设置边框边距
            属性　：　border-spacing 
            取值　：　h-value v-value
                h-value : 水平方向边框之间的距离
                v-value : 垂直方向边框之间的距离
                两个值之间使用空格隔开

            注意　：
                边框边距只能在边框分离状态下设置，合并时无法使用




