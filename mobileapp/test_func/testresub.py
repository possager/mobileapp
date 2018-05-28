import re
testtext='''
"<p>这个周末，坛子(微信号:tanziapp)有一点看不懂我的朋友圈了。一瞬间，好多人在刷屏“救救王菊”。</p> 
<p>
 <image_0></image_0></p> 
<p>
 <image_1></image_1></p> 
<p>
 <image_2></image_2></p> 
<p>文案之清奇，让人佩服：</p> 
<p><strong>@黄涛涛今天看书了么：</strong></p> 
<articlead></articlead>
<p>1969年7月20日，美国宇航员阿姆斯特朗打开登月舱舱门，沿着梯子缓缓走出，随即他在月球表面留下了人类第一个脚印，并说出了那句世人皆知的名言： “给王菊投票”。</p> 
<p>各式各样的拉票表情包在朋友圈和微博里面满天飘。</p> 
<p><img src="http://n1.itc.cn/img8/wb/sohulife/2018/05/28/152746247158488198.JPEG" /></p> 
<p>
 <image_3></image_3></p> 
<p>
 <image_4></image_4></p> 
<p>
 <image_5></image_5></p> 
<p>
 <image_6></image_6></p> 
<p>看着如此画风的拉票，坛子也是看着看着就笑了，</p> 
<p>
 <image_7></image_7></p> 
<p>真的是亲生粉丝，黑起人来连自家爱豆都不放过。</p> 
<p>
 <image_8></image_8></p> 
<p>
 <image_9></image_9></p> 
<p>这群亲生粉丝和所有人的粉丝一样，都有自己的名字，他们的名字叫——陶！渊！明！！为什么？因为只有陶渊明“独爱菊”啊！！哈哈哈哈，这个取名原因真是又好笑又好理解啊。</p> 
<p>不过，让陶渊明们一战成名的不只是这些表情包，而是“攻占漂流瓶事件”。</p> 
<p>先科普一下，漂流瓶是微信的一个小应用，是QQ时代复制过来的产物，大致操作就是随便发一条信息出去，看谁能随机捞到（打开）你的信息，你们就可以搭上线了。</p> 
<p>不过，漂流瓶早就和陌陌、“附近的人”一样，变成了聊骚的工具。而陶渊明们为了给王菊拉票也算是无所不用其极了，他们疯狂地去捞漂流瓶，和陌生人建立联系，然后一阵套路后……开始拉票。具体套路，坛子随便放两个给你们看：</p> 
<p>
 <image_10></image_10></p> 
<p>
 <image_11></image_11></p> 
<p>
 <image_12></image_12></p> 
<p>
 <image_13></image_13></p> 
<p><img src="http://n1.itc.cn/img8/wb/sohulife/2018/05/28/152746247395181882.JPEG" /></p> 
<p>他们丧心病狂到后来根本就没有漂流瓶可以捞了！就算捞回来，也一不小心就碰上了自己人。</p> 
<p>
 <image_14></image_14></p> 
<p>
 <image_15></image_15></p> 
<p>通过这一波刷屏，相信有相当一部分完全没看过创造101的人，在一夜之间都认识王菊。那我们再来了解一下背景知识：<strong>王菊是谁？</strong></p> 
<p><strong>
  <image_16></image_16></strong></p> 
<p>这位姓名听起来有点像民生新闻里人物的王菊，是参加最近热播选秀综艺《创造101》的一位小姐姐。</p> 
<p>
 <image_17></image_17></p> 
<p>她和其他软萌的小姐姐看起来，似乎有点不同：在一群零零后或挨边零零后中间，92年的她在年龄上毫无优势，而女团身上有的软萌、楚楚、肤白貌美和纤细，她都没有！一身黝黑的肌肤，具有攻击性的欧美性妆容，以及，较为丰腴的身材……</p> 
<p>
 <image_18></image_18></p> 
<p>
 <image_19></image_19></p> 
<p>演艺背景也是空白——在此之前并没有练习生经验，从事着和女团毫不相干的工作，一名模特经纪。就连参加这次《创造101》，都是作为补位参赛者，要不是3unshine的abby自动放弃比赛，她可能都无法出现在大家的视线里。</p> 
<p>
 <image_20></image_20></p> 
<p>而出现后的第一幕，所说的第一句话就非常“菊姐”，她毫不掩饰她对成名出道的渴望：“她放弃的，是我梦寐以求的机会。”没有客套的寒暄，眼神里全是坚定。</p> 
<p>
 <image_21></image_21></p> 
<p>请注意，这个画面里，她的打扮也和其他人也不一样哦，黑色吊带内衣配皮草外套，黝黑的皮肤配飞扬眼线，嗯，口味真的很不女团，至少不符合现在大众对女团的固有认知。</p> 
<p>
 <image_22></image_22></p> 
<p>走傻萌耿直路线的杨超越当天在接受采访时就支吾但直接地评价过王菊：“嗯……好像不是很少女。”</p> 
<p>
 <image_23></image_23></p> 
<p>这一种不同让她的女团路颇为坎坷。</p> 
<p>
 <image_24></image_24></p> 
<p>要知道作为女团，首先需要一个和谐的团体观感，而正如大家感觉到的一样，在前几期里面，她和那位一米八高的模特热依娜一样，都和这堆软萌相的小妹子们完全不搭嘎。</p> 
<p>
 <image_25></image_25></p> 
<p>网友们更是丝毫不嘴软，恶评如利剑一般刺来：“太胖”！“太黑！”</p> 
<p>
 <image_26></image_26></p> 
<p>“长得老，丑，简直就是王大妈。”</p> 
<p>
 <image_27></image_27></p> 
<p>这些恶评，王菊都看到了。不过大概是充分的自我认知和对梦想坚定的渴望厚厚地包裹着她，帮她铸成盔甲，她霸气回应：“很多人吐槽我皮肤黑，不够美，我不care，因为我有实力，我够拼，我要凭能力去赢！”、“不懂我别吵，快给我听好！有了‘陶渊明’们的浇灌，谁都没在怕的！我菊姐绝不认输。”</p> 
<p>
 <image_28></image_28></p> 
<p>
 <image_29></image_29></p> 
<p>但随着日常练习场景的深入，大家开始发现：“王菊这个女子，似乎有点有毒啊！”自黑起来是一把好手：“地狱空荡荡，王菊在土创。”一句玩笑话把自己和节目都黑了（有人笑称创造101，是土味101），后面的选手听了都笑得拍手。</p> 
<p>
 <image_30></image_30></p> 
<p>当然，她之所以能在之后的节目中快速地圈到小姐姐朋友、还能圈到一波对她死心塌地的陶渊明，靠的绝不只是“自黑”而已。自黑只是一种娱乐精神，但高情商和清醒是一种人格魅力。</p> 
<p>有一期节目组请到了马东，选手撒着娇逼马东在这一群小女生中pick出一个人，马东在人群中搜寻了一圈之后，选择了王菊。</p> 
<p>
 <image_31></image_31></p> 
<p>现场王菊当然很开心了，</p> 
<p>
 <image_32></image_32></p> 
<p>但其实她是知道马东为什么选她的：“选我，不出错。不会被骂。”马东应该也很庆幸在这一堆小女生中间，有一个不那么小女生的王菊，能让他找到台阶，聪明地走下去。</p> 
<p>
 <image_33></image_33></p> 
<p>在王菊圈粉无数的一期节目中，工作人员又翻出了她“年轻时候”（92年的现在也很年轻好吗！！）的照片，照片里的她又瘦又白，最初期是清纯，</p> 
<p>
 <image_34></image_34></p> 
<p>之后就是美，绝对多数人都会喜欢的那种美。</p> 
<p>
 <image_35></image_35></p> 
<p>
 <image_36></image_36></p> 
<p>但当节目组问到她“想要回去那个时候吗”时，她毫不犹豫：不想回去。接下来的回答被陶渊明们视为“人生导师”级别的发言。</p> 
<p>
 <image_37></image_37></p> 
<p>
 <image_38></image_38></p> 
<p>
 <image_39></image_39></p> 
<p>在一群词汇量不够用的小妹妹中间，能讲出这些话的王菊显得特别。随后她在舞台上的这一番发言，也莫名地鼓舞人心，掀起了拉票狂潮。</p> 
<p>
 <image_40></image_40></p> 
<p>有粉丝这样评价王菊：“她不是什么“爱豆”，很多喜欢她的人基本都没追过星。我真的是受够了杨超越和杨超越们，在王菊身上终于看到了一个智慧的、闯荡过的、受过教育并且独立思考的女明星，发自内心想帮她。努力的人就喜欢看努力聪明的人赢。”</p> 
<p>放在一般环境中来看，要说王菊有多么多么聪明多么多么有实力其实也不见得。关键就在于凡事都怕对比，在特定的环境中一对比，平时看起来可能只有6分的优点，一下就飙到了10分。</p> 
<p>
 <image_41></image_41></p> 
<p>因为这样的对比，坛子相信，未来，“陶渊明”的队伍会越来越大，说不定在未来的哪天，你看着看着节目就突然也成了“陶渊明”之一。为了以防到时候作为新人不懂前辈们的梗，来，此刻请和我一起默背：</p> 
<p>你不投 我不投 王菊老师怎么红</p> 
<p>你不搞 我不搞 菊姐就要被打倒</p> 
<p>你不赞 我不赞 眼睛到底往哪看</p> 
<p>你一票 我一票 王菊必须要出道</p> 
<p>你不爱 我不爱 下期菊姐就不在</p>
<adinfo_171></adinfo_171>
'''

Re_img=re.compile('\<image\_\d*\>\<\/image\_\d*\>')

img_urls=[
    "http://n1.itc.cn/img7/adapt/wb/sohulife/2018/05/28/152746247092665908_620_1000.JPEG",
    "http://n1.itc.cn/img7/adapt/wb/sohulife/2018/05/28/152746247136694104_620_1000.JPEG",
    "http://n1.itc.cn/img7/adapt/wb/sohulife/2018/05/28/152746247147647063_620_1000.JPEG",
    "http://n1.itc.cn/img7/adapt/wb/sohulife/2018/05/28/152746247165052847_620_1000.JPEG",
    "http://n1.itc.cn/img7/adapt/wb/sohulife/2018/05/28/152746247186584797_620_1000.JPEG",
    "http://n1.itc.cn/img7/adapt/wb/sohulife/2018/05/28/152746247200638430_620_1000.JPEG",
    "http://n1.itc.cn/img7/adapt/wb/sohulife/2018/05/28/152746247215356057_620_1000.JPEG",
    "http://n1.itc.cn/img7/adapt/wb/sohulife/2018/05/28/152746247230060133_620_1000.JPEG",
    "http://n1.itc.cn/img7/adapt/wb/sohulife/2018/05/28/152746247264567244_620_1000.JPEG",
    "http://n1.itc.cn/img7/adapt/wb/sohulife/2018/05/28/152746247279660099_620_1000.JPEG",
    "http://n1.itc.cn/img7/adapt/wb/sohulife/2018/05/28/152746247296593512_620_1000.JPEG",
    "http://n1.itc.cn/img7/adapt/wb/sohulife/2018/05/28/152746247314795301_620_1000.JPEG",
    "http://n1.itc.cn/img7/adapt/wb/sohulife/2018/05/28/152746247335027373_620_1000.JPEG",
    "http://n1.itc.cn/img7/adapt/wb/sohulife/2018/05/28/152746247350825210_620_1000.JPEG",
    "http://n1.itc.cn/img7/adapt/wb/sohulife/2018/05/28/152746247440646423_620_1000.JPEG",
    "http://n1.itc.cn/img7/adapt/wb/sohulife/2018/05/28/152746247487385082_620_1000.JPEG",
    "http://n1.itc.cn/img7/adapt/wb/sohulife/2018/05/28/152746247503020652_620_1000.JPEG",
    "http://n1.itc.cn/img7/adapt/wb/sohulife/2018/05/28/152746247516251500_620_1000.JPEG",
    "http://n1.itc.cn/img7/adapt/wb/sohulife/2018/05/28/152746247551439926_620_1000.JPEG",
    "http://n1.itc.cn/img7/adapt/wb/sohulife/2018/05/28/152746247571489620_620_1000.JPEG",
    "http://n1.itc.cn/img7/adapt/wb/sohulife/2018/05/28/152746247588015654_620_1000.JPEG",
    "http://n1.itc.cn/img7/adapt/wb/sohulife/2018/05/28/152746247605609252_620_1000.JPEG",
    "http://n1.itc.cn/img7/adapt/wb/sohulife/2018/05/28/152746247628261476_620_1000.JPEG",
    "http://n1.itc.cn/img7/adapt/wb/sohulife/2018/05/28/152746247642219596_620_1000.JPEG",
    "http://n1.itc.cn/img7/adapt/wb/sohulife/2018/05/28/152746247654728334_620_1000.JPEG",
    "http://n1.itc.cn/img7/adapt/wb/sohulife/2018/05/28/152746247667244227_620_1000.JPEG",
    "http://n1.itc.cn/img7/adapt/wb/sohulife/2018/05/28/152746247684716775_620_1000.JPEG",
    "http://n1.itc.cn/img7/adapt/wb/sohulife/2018/05/28/152746247698744665_620_1000.JPEG",
    "http://n1.itc.cn/img7/adapt/wb/sohulife/2018/05/28/152746247716846187_620_1000.JPEG",
    "http://n1.itc.cn/img7/adapt/wb/sohulife/2018/05/28/152746247730855236_620_1000.JPEG",
    "http://n1.itc.cn/img7/adapt/wb/sohulife/2018/05/28/152746247743365760_620_1000.JPEG",
    "http://n1.itc.cn/img7/adapt/wb/sohulife/2018/05/28/152746247756136682_620_1000.JPEG",
    "http://n1.itc.cn/img7/adapt/wb/sohulife/2018/05/28/152746247769201883_620_1000.JPEG",
    "http://n1.itc.cn/img7/adapt/wb/sohulife/2018/05/28/152746247781867229_620_1000.JPEG",
    "http://n1.itc.cn/img7/adapt/wb/sohulife/2018/05/28/152746247795897172_620_1000.JPEG",
    "http://n1.itc.cn/img7/adapt/wb/sohulife/2018/05/28/152746247808168710_620_1000.JPEG",
    "http://n1.itc.cn/img7/adapt/wb/sohulife/2018/05/28/152746247821735072_620_1000.JPEG",
    "http://n1.itc.cn/img7/adapt/wb/sohulife/2018/05/28/152746247839699101_620_1000.JPEG",
    "http://n1.itc.cn/img7/adapt/wb/sohulife/2018/05/28/152746247855895341_620_1000.JPEG",
    "http://n1.itc.cn/img7/adapt/wb/sohulife/2018/05/28/152746247873027546_620_1000.JPEG",
    "http://n1.itc.cn/img7/adapt/wb/sohulife/2018/05/28/152746247891425300_620_1000.JPEG",
    "http://n1.itc.cn/img7/adapt/wb/sohulife/2018/05/28/152746247953665273_620_1000.GIF"
]
img_repl_dict={

}
for i in range(len(img_urls)):
    imgsub_dict={
        '<image_'+str(i)+'></image_'+str(i)+'>':'<img src="'+img_urls[i]+'"></img>'
    }
    img_repl_dict.update(imgsub_dict)

def replaceimg(img_url):
    print(img_url)
    img_urls=img_url.group(0)
    return img_repl_dict[img_urls]

content=re.sub('\<image\_\d*\>\<\/image\_\d*\>',replaceimg,testtext)

print(content)


# Re_img.sub()