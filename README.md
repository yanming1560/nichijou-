# nichijou-calendar
想要做nichijou的台历，首先去堆糖把图片下载下来，然后设计台历模板，再把图片裁成合适大小，然后把万年历上的内容也下载下来，拼接成一页。最后找个便宜的淘宝店去印刷，如果太贵就做成电子版的。。。

down_image.py 去堆糖下图片（图片还要从动漫里截图，因为堆糖没有人物特写以及结局全家福）

get_date.py 获取万年历的内容

deal_image.py 处理图片，将所需要的图像按照尺寸截图出来，或者按照尺寸缩放

get_calendat.py 设计模板，放入图片和日历，保存。
