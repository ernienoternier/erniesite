$(document).ready(function(){//判断文档是否准备完成
alert("hello");
   $(window).on("load",function(){//加载文档
        ImageLocation();//此方法是为了确定图片位置
       //模拟数据源, 自定义json字符串, 设置无限滚动加载
       var dataImg = {"data":[{"src":"8.jpg"},{"src":"5.jpg"},{"src":"3.jpg"},{"src":"9.jpg"},{"src":"8.jpg"},{"src":"6.jpg"},{"src":"5.jpg"},{"src":"4.jpg"},{"src":"3.jpg"}]}
       //下面这个方法是在滚动鼠标或者滑动滚动条时间执行的, 目的在于判断何时开始加载图片, 我定义的是最后一张图片的一半的时候开始加载数据
       window.onscroll=function(){
            if(scollToSide()){
                $.each(dataImg.data,function(index,value){
                    var box = $("<div>").addClass("box").appendTo("#container");//创建div标签追加在主容器之后, 用来承载图片盒子
                    var contend = $("<div>").addClass("contend").appendTo(box);//创建内容容器, 装饰图片样式
                    $("<img>").attr("src","./img/"+$(value).attr("src")).appendTo(contend);//加载图片
                });
            }
           ImageLocation();//重新调用确定图片位置方法, 以确保图片位置摆放和之前一样
       }
   }) ;
});

//此方法是为了判断何时加载, 当最后一张图片的高度小于屏幕窗口高度和滚动条滚动距离的时候开始加载, 否则不加载
function scollToSide(){
    var box = $(".box");
    var lastHeight = box.last().get(0).offsetTop+Math.floor(box.last().height()/2);//Math方法目的在于将小数化为整数
    var screenHeight = $(document).width();
    var scrollHeight = $(window).scrollTop();
    return lastHeight < (screenHeight + scrollHeight) ? true:false;
}

//确定图片摆放位置
function ImageLocation(){
    var screenWidth = $(window).width();//获取当前屏幕宽度
    var box = $(".box");//获取所有的box容器
    var ImgWidth = box.eq(0).width();//获取图片宽度
    var num = Math.floor(screenWidth / ImgWidth);//判断一个屏幕宽度内最多可以容纳多少张图片
    var ary = [];//声明数组
    box.each(function(index, value){
        if(index<num){
            ary[index]=box.eq(index).height();//承载第一行图片的高度
        } else {
            var minHeight = Math.min.apply(null,ary);//取到第一行高度的最小值
            var minIndex = $.inArray(minHeight,ary);//计算出最小高度的位置
            $(value).css({//添加样式
                top:minHeight,
                left:box.eq(minIndex).position().left,
                position:"absolute"

            });
            ary[minIndex]+=box.eq(index).height();//进行高度叠加, 方便后面图片位置的确定
        }
    });
}
