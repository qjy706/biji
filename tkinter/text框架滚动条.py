import tkinter as tk
from tkinter import messagebox
#想写一个界面　要先有一个窗口　
#创建窗口　
win = tk.Tk()
#设置标题
win.title('qjy')
#设置大小和位置
win.geometry('600x600+200+20')

'''文本框架　用于显示多行文本
高度是显示四行 这时候需要带滚动条'''
#创建滚动条
s = tk.Scrollbar()

text = tk.Text(win,width=30,height=5)
#滚动条固定到窗体的右侧 Y轴填充满
s.pack(side = tk.RIGHT,fill=tk.Y)
text.pack(side = tk.RIGHT,fill=tk.Y)
#滚动条与文本框架关联 滚动条动文本动
s.config(command = text.yview)
#文本动滚动条动
text.config(yscrollcommand=s.set)
sta = '''
Accusation of meddling 'ridiculous'
By MO JINGXI/ZHAO HUANXIN/DONG LESHUO  (China Daily)    09:05, October 06, 2018

Beijing responds to remarks by Pence, says China adheres to noninterference 

The Foreign Ministry said on Friday that it was "ridiculous" for Washington to characterize China's regular exchanges with the US as interference, after US Vice-President Mike Pence accused Beijing of meddling in American politics.

"It is very ridiculous for the US side to stigmatize its normal exchanges and cooperation with China as China interfering in its internal affairs and elections," Foreign Ministry spokeswoman Hua Chunying said in a statement.

"China always follows the principle of noninterference in others' internal affairs, and we have no interest in meddling in US internal affairs and elections," Hua said.

"The international community has already known fully well who wantonly infringes upon others' sovereignty, interferes in others' internal affairs and undermines others' interests. Any malicious slander on China is futile," the statement said.

Pence's speech "made unwarranted accusations against China's domestic and foreign policies and slandered China by claiming that China meddles in US internal affairs and elections", Hua said.

"This is nothing but speaking on hearsay evidence, confusing right and wrong and creating something out of thin air. The Chinese side is firmly opposed to it," she said.

In Washington on Thursday, Pence said in a speech at the Hudson Institute, a Washington-based think tank, that China was using "wedge issues" such as tariffs to advance its political influence in the US and globally. He accused China of seeking to sway the US midterm elections on Nov 6, in retaliation for US trade policies against Beijing.

Hua said China's policy toward the US is "consistent and clear-cut".

"We are committed to joining hands with the US to work for nonconflict, nonconfrontation, mutual respect and win-win cooperation," she said.

"We urge the US to correct its wrongdoing, stop groundlessly accusing and slandering China and harming China's interests and China-US ties, and take concrete actions to maintain the sound and steady development of China-US relations," she added.

Pence also credited the US for China's rapid development, noting that China has become the world's second-largest economy.

"Much of this success was driven by American investment in China," he said.

Hua said China's development is mainly due to the Chinese people's hard work and its mutually beneficial cooperation with countries around the world.

Cui Tiankai, China's ambassador to the US, said China wants to end the trade conflict, but the US position keeps changing, "so we don't know exactly what the US would want as priorities".

"We are ready to make a deal. We are ready to make some compromise, but it needs the goodwill from both sides," Cui said in an interview with National Public Radio on Wednesday.

Cui said he does not see sufficient goodwill from the US.

"We offered to reduce the trade deficit of the United States, for instance. And we also presented a very good proposal to the US side about the further reform and opening-up in China, some of the so-called structural issues," he said.

"Then I think more than once we had some tentative agreement between the two working teams. Then just overnight the tentative agreement was rejected, and the demand from the US changed. So this is very confusing, and this is making things very difficult," he said.

Cui also spoke about the South China Sea.

"We have sovereignty over many of the islands in the South China Sea. And this has been a long-standing position of China," he said.

Cui said that at the end of World War II, the then-Chinese government, with the help of US naval ships, took back the islands from Japan.

"It was American naval ships that sent Chinese troops to take back these islands from Japan. So we have a long-standing sovereignty over these islands, but we are also aware there are some territorial disputes," Cui said.

"And now we're ready to work with other countries to have negotiations to have a final solution to such disputes," he said. "We understand this will take a long time, but in the meantime it is our intention to maintain stability there. That's why we are working on a code of conduct with the ASEAN countries.

"Before we are able to solve the territorial disputes, we should work together to maintain stability, to try to engage in some joint development of resources there, to keep a good order in the region," Cui said. "So I just hope that the United States will join our efforts, will be helpful, not try to disrupt the process toward peaceful negotiations."

People's Daily, in an opinion article published on Friday on its website, said US leaders' recent unwarranted accusations regarding China's internal and foreign policies are outdated and full of mistakes.

The US accusations distort facts and confuse right and wrong, and are full of factual and logical errors that don't conform to the times, it said, describing the US positions as "numerous absurd arguments".'''
#插入字符串
text.insert(tk.INSERT,sta)





win.mainloop()