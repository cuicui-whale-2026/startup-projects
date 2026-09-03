# -*- coding: utf-8 -*-
"""
D方向 数字模板产品 PDF 生成脚本
生成三个可售产品：
1. AI_提示词包_求职备考.pdf
2. 行测公式速记卡.pdf
3. 408考点清单.pdf
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, PageBreak, ListFlowable, ListItem,
                                KeepTogether)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT

# ---------- 字体 ----------
pdfmetrics.registerFont(TTFont("SimHei", r"C:\Windows\Fonts\simhei.ttf"))

# ---------- 品牌配色 ----------
NAVY = HexColor("#17365D")
BLUE = HexColor("#5B9BD5")
LIGHT = HexColor("#DEEBF7")
ORANGE = HexColor("#C96A2B")
GREEN = HexColor("#1E8E6E")
PURPLE = HexColor("#7B3FBF")
GRAY = HexColor("#6B7280")
BG = HexColor("#F8F9FB")

# ---------- 样式 ----------
def st(name, **kw):
    base = dict(fontName="SimHei", leading=18, spaceAfter=6)
    base.update(kw)
    return ParagraphStyle(name, **base)

title_st = st("title", fontSize=26, leading=34, alignment=TA_CENTER, textColor=NAVY, spaceAfter=4)
sub_st = st("sub", fontSize=12, leading=18, alignment=TA_CENTER, textColor=GRAY, spaceAfter=12)
h1_st = st("h1", fontSize=16, leading=22, textColor=NAVY, spaceBefore=14, spaceAfter=8)
h2_st = st("h2", fontSize=13, leading=19, textColor=BLUE, spaceBefore=10, spaceAfter=6)
body_st = st("body", fontSize=11, leading=18, textColor=HexColor("#333333"))
small_st = st("small", fontSize=9, leading=14, textColor=GRAY)
code_st = st("code", fontSize=9.5, leading=15, textColor=HexColor("#333333"),
             backColor=BG, borderPadding=8, borderColor=HexColor("#E4E3DD"), borderWidth=0.5)

# ---------- 封面函数 ----------
def cover(doc, title, subtitle, tagline, color):
    """生成一页品牌封面"""
    w, h = A4
    story = []
    # 顶部色带
    t = Table([[""]], colWidths=[w-40*mm], rowHeights=[8*mm])
    t.setStyle(TableStyle([("BACKGROUND", (0,0), (-1,-1), color),
                           ("TOPPADDING",(0,0),(-1,-1),0),("BOTTOMPADDING",(0,0),(-1,-1),0)]))
    story.append(t)
    story.append(Spacer(1, 40*mm))
    story.append(Paragraph(title, title_st))
    story.append(Paragraph(subtitle, sub_st))
    story.append(Spacer(1, 10*mm))
    # 分隔线
    line = Table([[""]], colWidths=[60*mm], rowHeights=[0.5])
    line.setStyle(TableStyle([("LINEBELOW",(0,0),(-1,-1),1,color),
                              ("TOPPADDING",(0,0),(-1,-1),0),("BOTTOMPADDING",(0,0),(-1,-1),0)]))
    story.append(line)
    story.append(Spacer(1, 10*mm))
    story.append(Paragraph(tagline, st("tg", fontSize=11, leading=18, alignment=TA_CENTER, textColor=HexColor("#555555"))))
    story.append(Spacer(1, 30*mm))
    # 底部信息
    story.append(Paragraph("脆脆鲸 · 数字产品", st("ft", fontSize=10, alignment=TA_CENTER, textColor=GRAY)))
    story.append(Paragraph("一次购买 · 永久使用 · 备考人/求职人专属", st("ft2", fontSize=9, alignment=TA_CENTER, textColor=GRAY)))
    story.append(PageBreak())
    return story

def section_header(text, color):
    t = Table([[Paragraph(text, st("sec", fontSize=13, leading=18, textColor=HexColor("#FFFFFF")))],
               ], colWidths=[170*mm])
    t.setStyle(TableStyle([("BACKGROUND", (0,0), (-1,-1), color),
                           ("TOPPADDING",(0,0),(-1,-1),6),("BOTTOMPADDING",(0,0),(-1,-1),6),
                           ("LEFTPADDING",(0,0),(-1,-1),10)]))
    return t

def usage_box(text):
    t = Table([[Paragraph(text, body_st)]], colWidths=[170*mm])
    t.setStyle(TableStyle([("BACKGROUND", (0,0), (-1,-1), HexColor("#FFF8E1")),
                           ("BOX", (0,0), (-1,-1), 0.5, HexColor("#FAAD14")),
                           ("TOPPADDING",(0,0),(-1,-1),8),("BOTTOMPADDING",(0,0),(-1,-1),8),
                           ("LEFTPADDING",(0,0),(-1,-1),10),("RIGHTPADDING",(0,0),(-1,-1),10)]))
    return t

OUT_DIR = r"C:\Users\31125\Doubao\chats\2026-09-01\new-chat-1\startup-projects"

# =========================================================
# 产品 1：AI 提示词包
# =========================================================
def make_prompt_pack():
    doc = SimpleDocTemplate(f"{OUT_DIR}\\AI_提示词包_求职备考.pdf", pagesize=A4,
                            leftMargin=20*mm, rightMargin=20*mm, topMargin=20*mm, bottomMargin=20*mm)
    story = []
    story += cover(doc,
                   "AI 提示词包",
                   "应届生求职 + 考公申论 + 408考研 三合一",
                   "把 AI 变成你的私人助教：简历优化 / 申论批改 / 考研规划，复制即用",
                   PURPLE)
    # 使用说明
    story.append(section_header("📖 使用说明", PURPLE))
    story.append(Spacer(1, 6*mm))
    story.append(usage_box("本提示词包包含 3 个场景的 AI 提示词。使用方法：打开任意 AI 工具（豆包 / ChatGPT / Claude 等），"
                           "复制对应提示词，把【】中的内容替换成你的真实信息，发送即可。"))
    story.append(Spacer(1, 4*mm))
    for line in ["① 提示词中的「角色设定」让 AI 扮演专业角色，输出质量更高",
                 "② 填空处（【】）一定要替换，否则结果不精准",
                 "③ 不满意可追加「再优化一版，更口语化/更专业」，AI 会继续改"]:
        story.append(Paragraph("· " + line, body_st))
    story.append(PageBreak())

    # 产品A
    story.append(section_header("产品 A · 应届生简历优化提示词", PURPLE))
    story.append(Spacer(1, 5*mm))
    story.append(Paragraph("场景：把平淡的经历改写成有亮点、能过筛的简历描述。", small_st))
    story.append(Spacer(1, 3*mm))
    prompt_a = """【角色】你是资深 HR 兼求职导师，有 10 年筛简历经验。
【任务】帮我优化下面的简历经历描述，让它有重点、有量化成果、符合 ATS 关键词筛选。

原经历：【把你的原经历粘贴到这里】

要求：
1. 用 STAR 法则重写（情境-任务-行动-结果）
2. 每条加 1 个可量化的数字（如"提升 30%"）
3. 去掉空话（"负责""参与"等），换成动作开头
4. 控制在 3 条以内，每条不超过 60 字
5. 输出格式：原句 → 改后 → 为什么这样改"""
    story.append(Paragraph(prompt_a, code_st))
    story.append(Spacer(1, 4*mm))
    story.append(Paragraph("使用提示：如果投递的是特定岗位，把岗位描述（JD）也粘进去，让 AI 对齐关键词。", small_st))
    story.append(PageBreak())

    # 产品B
    story.append(section_header("产品 B · 考公申论大作文提示词", PURPLE))
    story.append(Spacer(1, 5*mm))
    story.append(Paragraph("场景：申论大作文写完没人批改？让 AI 当阅卷老师。", small_st))
    story.append(Spacer(1, 3*mm))
    prompt_b = """【角色】你是申论阅卷老师，熟悉国考/省考评分标准。
【任务】帮我审一篇申论大作文，从立意、结构、论据、语言四方面打分并给出修改建议。
作文主题：【写主题】
我的正文：【粘贴正文】

要求：
1. 按评分维度给 0-10 分
2. 指出立意是否切题、是否跑偏
3. 给出 2 个可替换的高分论据
4. 修改一段我写得最差的段落"""
    story.append(Paragraph(prompt_b, code_st))
    story.append(Spacer(1, 4*mm))
    story.append(Paragraph("使用提示：可以追加「再按一类文标准给我示范一段」，看高分写法差距。", small_st))
    story.append(PageBreak())

    # 产品C
    story.append(section_header("产品 C · 408 复习规划提示词", PURPLE))
    story.append(Spacer(1, 5*mm))
    story.append(Paragraph("场景：408 四科不知从何下手？让 AI 帮你定制复习计划。", small_st))
    story.append(Spacer(1, 3*mm))
    prompt_c = """【角色】你是计算机考研 408 高分学长（专业课 130+）。
【任务】根据我的情况制定 408 四科复习计划。
当前进度：数据结构【】 / 操作系统【】 / 计算机组成【】 / 计算机网络【】
每天可用时间：【】小时
目标分数：【】

要求：
1. 按"基础→强化→真题→冲刺"四阶段排计划
2. 每科给推荐教材和刷题量
3. 指出每科最常考的 5 个考点
4. 每周一个可检查的里程碑"""
    story.append(Paragraph(prompt_c, code_st))
    story.append(Spacer(1, 4*mm))
    story.append(Paragraph("使用提示：每周反馈进度，让 AI 动态调整计划，别一次排完就不管了。", small_st))
    story.append(PageBreak())

    # 结尾
    story.append(section_header("🎁 附赠：AI 使用 3 个心法", PURPLE))
    story.append(Spacer(1, 5*mm))
    for title, desc in [
        ("1. 角色代入法", "永远先给 AI 一个身份（HR / 阅卷老师 / 学长），专业身份决定输出水平"),
        ("2. 迭代追问法", "第一次输出不满意很正常，追加「更具体」「举例子」「换个角度」继续调"),
        ("3. 交叉验证法", "重要结论（如岗位要求、考试政策）让 AI 给两版说法，再核对官方信息"),
    ]:
        story.append(Paragraph(f"<b>{title}</b>", h2_st))
        story.append(Paragraph(desc, body_st))
    story.append(Spacer(1, 6*mm))
    story.append(Paragraph("—— 脆脆鲸 · 数字产品出品 ——", st("end", fontSize=10, alignment=TA_CENTER, textColor=GRAY)))
    doc.build(story)
    print("✅ AI_提示词包_求职备考.pdf 已生成")

# =========================================================
# 产品 2：行测公式速记卡
# =========================================================
def make_xingce():
    doc = SimpleDocTemplate(f"{OUT_DIR}\\行测公式速记卡.pdf", pagesize=A4,
                            leftMargin=20*mm, rightMargin=20*mm, topMargin=20*mm, bottomMargin=20*mm)
    story = []
    story += cover(doc,
                   "行测公式速记卡",
                   "资料分析 / 数量关系 / 判断推理 核心公式",
                   "考前冲刺必备 · 一页一模块 · 随看随记",
                   ORANGE)

    # 模块1：资料分析
    story.append(section_header("模块一 · 资料分析（拿分大户）", ORANGE))
    story.append(Spacer(1, 5*mm))
    data = [
        ["公式", "表达", "速记要点"],
        ["增长率", "(现期-基期)/基期", "问增长百分之几"],
        ["增长量", "现期-基期", "绝对增长值"],
        ["基期量", "现期/(1+增长率)", "已知现期求过去"],
        ["现期量", "基期×(1+增长率)", "已知过去求现在"],
        ["比重", "部分/整体", "占多少"],
        ["平均数", "总量/个数", "平均每个"],
        ["倍数", "A/B", "A是B的几倍"],
        ["隔年增长率", "r1+r2+r1×r2", "两年复合增长"],
        ["年均增长率", "(现期/基期)^(1/n)-1", "多年平均"],
    ]
    t = Table(data, colWidths=[38*mm, 60*mm, 72*mm])
    t.setStyle(TableStyle([
        ("FONTNAME", (0,0), (-1,-1), "SimHei"),
        ("FONTSIZE", (0,0), (-1,-1), 9.5),
        ("BACKGROUND", (0,0), (-1,0), ORANGE),
        ("TEXTCOLOR", (0,0), (-1,0), HexColor("#FFFFFF")),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [HexColor("#FFFFFF"), BG]),
        ("GRID", (0,0), (-1,-1), 0.4, HexColor("#E4E3DD")),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("TOPPADDING", (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
    ]))
    story.append(t)
    story.append(Spacer(1, 4*mm))
    story.append(Paragraph("💡 资料分析 60% 分数来自「增长率/比重/平均数」三件套，优先掌握。", small_st))
    story.append(PageBreak())

    # 模块2：数量关系
    story.append(section_header("模块二 · 数量关系（秒杀技巧）", ORANGE))
    story.append(Spacer(1, 5*mm))
    data2 = [
        ["题型", "核心公式/技巧", "秒杀点"],
        ["行程问题", "路程=速度×时间", "相对速度/相遇追及"],
        ["工程问题", "总量=效率×时间", "设总量为1或公倍数"],
        ["利润问题", "利润=售价-成本", "利润率=利润/成本"],
        ["浓度问题", "溶质=溶液×浓度", "十字交叉法"],
        ["容斥问题", "A∪B=A+B-A∩B", "两集合/三集合公式"],
        ["排列组合", "C(n,m)、A(n,m)", "分清排列还是组合"],
        ["概率", "P=满足/总数", "古典概型"],
        ["数列", "等差/等比通项", "求和公式"],
        ["最值问题", "和定求极值", "极端思想"],
    ]
    t = Table(data2, colWidths=[38*mm, 60*mm, 72*mm])
    t.setStyle(TableStyle([
        ("FONTNAME", (0,0), (-1,-1), "SimHei"),
        ("FONTSIZE", (0,0), (-1,-1), 9.5),
        ("BACKGROUND", (0,0), (-1,0), ORANGE),
        ("TEXTCOLOR", (0,0), (-1,0), HexColor("#FFFFFF")),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [HexColor("#FFFFFF"), BG]),
        ("GRID", (0,0), (-1,-1), 0.4, HexColor("#E4E3DD")),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("TOPPADDING", (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
    ]))
    story.append(t)
    story.append(Spacer(1, 4*mm))
    story.append(Paragraph("💡 数量关系别恋战，先做会做的，不会的直接蒙，保住时间给资料分析。", small_st))
    story.append(PageBreak())

    # 模块3：判断推理 + 常识速记
    story.append(section_header("模块三 · 判断推理 + 言语要点", ORANGE))
    story.append(Spacer(1, 5*mm))
    data3 = [
        ["模块", "核心方法", "一句话技巧"],
        ["图形推理", "先看对称/笔画/元素", "数量-位置-样式-属性"],
        ["定义判断", "抓关键词对照", "主体+对象+方式+结果"],
        ["类比推理", "看逻辑关系", "种属/组成/并列/反义"],
        ["逻辑判断", "翻译推理+加强削弱", "先形式化再分析"],
        ["言语理解", "找主旨句", "转折之后是重点"],
        ["逻辑填空", "结合语境+搭配", "看感情色彩"],
    ]
    t = Table(data3, colWidths=[38*mm, 60*mm, 72*mm])
    t.setStyle(TableStyle([
        ("FONTNAME", (0,0), (-1,-1), "SimHei"),
        ("FONTSIZE", (0,0), (-1,-1), 9.5),
        ("BACKGROUND", (0,0), (-1,0), ORANGE),
        ("TEXTCOLOR", (0,0), (-1,0), HexColor("#FFFFFF")),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [HexColor("#FFFFFF"), BG]),
        ("GRID", (0,0), (-1,-1), 0.4, HexColor("#E4E3DD")),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("TOPPADDING", (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
    ]))
    story.append(t)
    story.append(Spacer(1, 6*mm))
    story.append(section_header("模块四 · 申论黄金结构", ORANGE))
    story.append(Spacer(1, 4*mm))
    for line in [
        "总-分-总结构：开头点题（3-4行）→ 主体三段（每段：观点+论据+分析）→ 结尾升华",
        "开头万能式：背景引入 + 中心论点，首句亮观点",
        "论证方法：举例论证 + 道理论证 + 对比论证，至少两种",
        "结尾：回扣主题 + 展望/呼吁，别拖泥带水",
    ]:
        story.append(Paragraph("· " + line, body_st))
    story.append(Spacer(1, 6*mm))
    story.append(Paragraph("—— 脆脆鲸 · 数字产品出品 ——", st("end", fontSize=10, alignment=TA_CENTER, textColor=GRAY)))
    doc.build(story)
    print("✅ 行测公式速记卡.pdf 已生成")

# =========================================================
# 产品 3：408 考点清单
# =========================================================
def make_408():
    doc = SimpleDocTemplate(f"{OUT_DIR}\\408考点清单.pdf", pagesize=A4,
                            leftMargin=20*mm, rightMargin=20*mm, topMargin=20*mm, bottomMargin=20*mm)
    story = []
    story += cover(doc,
                   "408 考点清单",
                   "数据结构 / 操作系统 / 计算机组成 / 计算机网络",
                   "计算机考研核心考点梳理 · 冲刺自查表",
                   GREEN)

    # 数据结构
    story.append(section_header("第一科 · 数据结构（45分）", GREEN))
    story.append(Spacer(1, 5*mm))
    ds = [
        ["章节", "必考考点", "优先级"],
        ["线性表", "顺序表/链表操作、插入删除复杂度", "⭐⭐⭐"],
        ["栈和队列", "进出栈序列、循环队列、应用（括号匹配）", "⭐⭐⭐"],
        ["树与二叉树", "遍历（前中后/层次）、线索二叉树、哈夫曼树", "⭐⭐⭐"],
        ["图", "邻接表/矩阵、DFS/BFS、最小生成树、最短路", "⭐⭐⭐"],
        ["查找", "二分查找、BST、平衡树、哈希表、B树", "⭐⭐⭐"],
        ["排序", "快排/归并/堆排序、稳定性、复杂度", "⭐⭐⭐"],
    ]
    t = Table(ds, colWidths=[42*mm, 88*mm, 40*mm])
    t.setStyle(TableStyle([
        ("FONTNAME", (0,0), (-1,-1), "SimHei"),("FONTSIZE", (0,0), (-1,-1), 9.5),
        ("BACKGROUND", (0,0), (-1,0), GREEN),("TEXTCOLOR", (0,0), (-1,0), HexColor("#FFFFFF")),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [HexColor("#FFFFFF"), BG]),
        ("GRID", (0,0), (-1,-1), 0.4, HexColor("#E4E3DD")),("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("TOPPADDING", (0,0), (-1,-1), 6),("BOTTOMPADDING", (0,0), (-1,-1), 6),
    ]))
    story.append(t)
    story.append(PageBreak())

    # 操作系统
    story.append(section_header("第二科 · 操作系统（35分）", GREEN))
    story.append(Spacer(1, 5*mm))
    os = [
        ["章节", "必考考点", "优先级"],
        ["进程管理", "PCB、进程状态转换、进程/线程区别", "⭐⭐⭐"],
        ["调度", "先来先服务/短作业/时间片轮转/优先级", "⭐⭐⭐"],
        ["同步互斥", "信号量、PV操作、经典问题（生产者消费者）", "⭐⭐⭐"],
        ["死锁", "必要条件、银行家算法、死锁检测", "⭐⭐⭐"],
        ["内存管理", "分页/分段、虚拟内存、页面置换（LRU）", "⭐⭐⭐"],
        ["文件与I/O", "文件系统、磁盘调度（FCFS/SSTF/SCAN）", "⭐⭐"],
    ]
    t = Table(os, colWidths=[42*mm, 88*mm, 40*mm])
    t.setStyle(TableStyle([
        ("FONTNAME", (0,0), (-1,-1), "SimHei"),("FONTSIZE", (0,0), (-1,-1), 9.5),
        ("BACKGROUND", (0,0), (-1,0), GREEN),("TEXTCOLOR", (0,0), (-1,0), HexColor("#FFFFFF")),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [HexColor("#FFFFFF"), BG]),
        ("GRID", (0,0), (-1,-1), 0.4, HexColor("#E4E3DD")),("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("TOPPADDING", (0,0), (-1,-1), 6),("BOTTOMPADDING", (0,0), (-1,-1), 6),
    ]))
    story.append(t)
    story.append(PageBreak())

    # 计算机组成原理
    story.append(section_header("第三科 · 计算机组成原理（45分）", GREEN))
    story.append(Spacer(1, 5*mm))
    cz = [
        ["章节", "必考考点", "优先级"],
        ["数据表示", "原码/反码/补码、IEEE754浮点、溢出判断", "⭐⭐⭐"],
        ["存储系统", "Cache映射（直接/全相联/组相联）、主存扩展", "⭐⭐⭐"],
        ["指令系统", "指令格式、寻址方式、CISC/RISC", "⭐⭐⭐"],
        ["CPU", "数据通路、指令流水线、冒险与处理", "⭐⭐⭐"],
        ["总线", "总线仲裁、同步/异步、总线带宽计算", "⭐⭐"],
        ["I/O方式", "程序查询/中断/DMA", "⭐⭐"],
    ]
    t = Table(cz, colWidths=[42*mm, 88*mm, 40*mm])
    t.setStyle(TableStyle([
        ("FONTNAME", (0,0), (-1,-1), "SimHei"),("FONTSIZE", (0,0), (-1,-1), 9.5),
        ("BACKGROUND", (0,0), (-1,0), GREEN),("TEXTCOLOR", (0,0), (-1,0), HexColor("#FFFFFF")),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [HexColor("#FFFFFF"), BG]),
        ("GRID", (0,0), (-1,-1), 0.4, HexColor("#E4E3DD")),("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("TOPPADDING", (0,0), (-1,-1), 6),("BOTTOMPADDING", (0,0), (-1,-1), 6),
    ]))
    story.append(t)
    story.append(PageBreak())

    # 计算机网络
    story.append(section_header("第四科 · 计算机网络（25分）", GREEN))
    story.append(Spacer(1, 5*mm))
    net = [
        ["章节", "必考考点", "优先级"],
        ["体系结构", "OSI七层/TCP-IP四层、各层功能", "⭐⭐⭐"],
        ["物理层", "编码、传输介质、信道容量（奈奎斯特/香农）", "⭐⭐"],
        ["数据链路层", "封装成帧、差错控制、CSMA/CD、MAC地址", "⭐⭐⭐"],
        ["网络层", "IP编址、子网划分、路由协议（RIP/OSPF/BGP）", "⭐⭐⭐"],
        ["传输层", "TCP/UDP、三次握手四次挥手、流量/拥塞控制", "⭐⭐⭐"],
        ["应用层", "DNS/HTTP/FTP/SMTP、HTTP各版本", "⭐⭐⭐"],
    ]
    t = Table(net, colWidths=[42*mm, 88*mm, 40*mm])
    t.setStyle(TableStyle([
        ("FONTNAME", (0,0), (-1,-1), "SimHei"),("FONTSIZE", (0,0), (-1,-1), 9.5),
        ("BACKGROUND", (0,0), (-1,0), GREEN),("TEXTCOLOR", (0,0), (-1,0), HexColor("#FFFFFF")),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [HexColor("#FFFFFF"), BG]),
        ("GRID", (0,0), (-1,-1), 0.4, HexColor("#E4E3DD")),("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("TOPPADDING", (0,0), (-1,-1), 6),("BOTTOMPADDING", (0,0), (-1,-1), 6),
    ]))
    story.append(t)
    story.append(Spacer(1, 6*mm))
    story.append(Paragraph("📌 408 复习节奏建议：基础期通读教材→强化期刷王道→真题期限时模考→冲刺期背错题。", small_st))
    story.append(Spacer(1, 5*mm))
    story.append(Paragraph("—— 脆脆鲸 · 数字产品出品 ——", st("end", fontSize=10, alignment=TA_CENTER, textColor=GRAY)))
    doc.build(story)
    print("✅ 408考点清单.pdf 已生成")

if __name__ == "__main__":
    make_prompt_pack()
    make_xingce()
    make_408()
    print("全部完成")
