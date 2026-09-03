# -*- coding: utf-8 -*-
"""
D方向 产品6：简历模板合集（程序员风格）PDF
三款模板 + 填写指南
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, PageBreak)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT

pdfmetrics.registerFont(TTFont("SimHei", r"C:\Windows\Fonts\simhei.ttf"))

NAVY = HexColor("#17365D")
BLUE = HexColor("#5B9BD5")
LIGHT = HexColor("#DEEBF7")
TEAL = HexColor("#1E8E6E")
GRAY = HexColor("#6B7280")
BG = HexColor("#F8F9FB")
DARK = HexColor("#2C3E50")
ACCENT2 = HexColor("#E67E22")

OUT = r"C:\Users\31125\Doubao\chats\2026-09-01\new-chat-1\startup-projects\简历模板合集_程序员风格.pdf"

def st(name, **kw):
    base = dict(fontName="SimHei", leading=18, spaceAfter=6)
    base.update(kw)
    return ParagraphStyle(name, **base)

title_st = st("t", fontSize=26, leading=34, alignment=TA_CENTER, textColor=NAVY)
sub_st = st("s", fontSize=12, leading=18, alignment=TA_CENTER, textColor=GRAY)
h1_st = st("h1", fontSize=16, leading=22, textColor=NAVY, spaceBefore=12, spaceAfter=8)
h2_st = st("h2", fontSize=12, leading=18, textColor=BLUE, spaceBefore=8, spaceAfter=4)
body_st = st("b", fontSize=10.5, leading=17, textColor=HexColor("#333333"))
small_st = st("sm", fontSize=9, leading=14, textColor=GRAY)
hint_st = st("hint", fontSize=9, leading=14, textColor=GRAY, backColor=BG, borderPadding=6,
             borderColor=HexColor("#E4E3DD"), borderWidth=0.5)

def section_bar(text, color):
    t = Table([[Paragraph(text, st("sb", fontSize=12, leading=16, textColor=HexColor("#FFFFFF"))) ]],
              colWidths=[170*mm])
    t.setStyle(TableStyle([("BACKGROUND", (0,0), (-1,-1), color),
                           ("TOPPADDING",(0,0),(-1,-1),5),("BOTTOMPADDING",(0,0),(-1,-1),5),
                           ("LEFTPADDING",(0,0),(-1,-1),10)]))
    return t

doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=20*mm, rightMargin=20*mm,
                        topMargin=20*mm, bottomMargin=20*mm)
story = []

# ===== 封面 =====
story.append(Table([[""]], colWidths=[170*mm], rowHeights=[8*mm], style=TableStyle([
    ("BACKGROUND",(0,0),(-1,-1),NAVY),("TOPPADDING",(0,0),(-1,-1),0),("BOTTOMPADDING",(0,0),(-1,-1),0)])))
story.append(Spacer(1, 40*mm))
story.append(Paragraph("简历模板合集", title_st))
story.append(Paragraph("程序员风格 · 三款任选 · 附填写指南", sub_st))
story.append(Spacer(1, 12*mm))
story.append(Paragraph("简洁极简款 / 技术感深色款 / 应届生清爽款", st("c", fontSize=13, alignment=TA_CENTER, textColor=TEAL)))
story.append(Spacer(1, 30*mm))
story.append(Paragraph("脆脆鲸 · 数字产品", st("f", fontSize=10, alignment=TA_CENTER, textColor=GRAY)))
story.append(PageBreak())

# ===== 使用说明 =====
story.append(section_bar("📖 使用说明", NAVY))
story.append(Spacer(1, 5*mm))
for line in [
    "本合集含 3 款程序员简历版式，每款标注了「版式结构 + 填写提示 + 适用场景」。",
    "推荐用工具复刻版式：Word / WPS / Canva / 简历生成器，填充你的真实信息。",
    "程序员简历核心原则：一页纸 + 技术栈关键词 + 项目量化成果 + 无错别字。",
    "模板为版式参考，文字为示意，请替换为真实经历。",
]:
    story.append(Paragraph("· " + line, body_st))
story.append(PageBreak())

# ===== 模板一 =====
story.append(section_bar("模板一 · 简洁极简款（投递最稳）", BLUE))
story.append(Spacer(1, 5*mm))
story.append(Paragraph("适用：技术岗通用投递，HR 一眼扫完一页纸。", small_st))
story.append(Spacer(1, 4*mm))
t1 = [
    ["张三", "Java后端开发 · 应届生"],
    ["电话: 138****8888 | 邮箱: zhangsan@email.com | GitHub: github.com/zhangsan | 深圳"],
    ["教育背景", "XX大学 计算机科学与技术 本科（2022-2026）GPA 3.5/4.0"],
    ["技术栈", "Java / Spring Boot / MySQL / Redis / 数据结构与算法"],
    ["项目经历", "① 校园二手交易平台（2025）：Spring Boot + MySQL，实现登录/商品/订单模块，优化SQL后接口响应提升30%"],
    ["", "② 个人博客系统（2024）：Vue + Spring Boot，支持Markdown发布、评论、分类"],
    ["实习经历", "XX科技 Java开发实习生（2025.06-2025.09）：参与后台接口开发，完成XX模块，修复XX个bug"],
    ["奖项证书", "蓝桥杯省二等奖 / 英语四级 / 软考中级"],
]
t1t = Table([[Paragraph(v, st("c", fontSize=10, leading=15)) if i>0 or j==0 else Paragraph(v, st("n", fontSize=14, leading=18, textColor=NAVY)) 
              for j,v in enumerate(row)] for i,row in enumerate(t1)], colWidths=[28*mm, 142*mm])
t1t.setStyle(TableStyle([
    ("FONTNAME",(0,0),(-1,-1),"SimHei"),("VALIGN",(0,0),(-1,-1),"TOP"),
    ("ROWBACKGROUNDS",(0,0),(-1,-1),[HexColor("#FFFFFF"), HexColor("#FFFFFF")]),
    ("SPAN",(0,0),(1,0)),("TOPPADDING",(0,0),(-1,-1),5),("BOTTOMPADDING",(0,0),(-1,-1),5),
    ("BACKGROUND",(0,2),(-1,2),LIGHT),("BACKGROUND",(0,4),(-1,4),LIGHT),
    ("BACKGROUND",(0,6),(-1,6),LIGHT),("BACKGROUND",(0,7),(-1,7),LIGHT),
]))
story.append(t1t)
story.append(Spacer(1, 5*mm))
story.append(Paragraph("💡 填写提示：一页纸，项目写「技术+动作+量化结果」，技术栈放显眼位置，对齐岗位JD关键词。", hint_st))
story.append(PageBreak())

# ===== 模板二 =====
story.append(section_bar("模板二 · 技术感深色款（投递互联网大厂）", DARK))
story.append(Spacer(1, 5*mm))
story.append(Paragraph("适用：互联网/大厂技术岗，风格更显专业与个性。", small_st))
story.append(Spacer(1, 4*mm))
t2 = [
    ["LI SI", "Backend Engineer · 2026 Fresh Graduate"],
    ["+86 138****8888 | li.si@email.com | github.com/lisi | Shenzhen"],
    ["SKILLS", "Java · Spring Boot · MySQL · Redis · RabbitMQ · Linux · Git"],
    ["EXPERIENCE", "2025.06-2025.09  XX科技 后端开发实习生"],
    ["", "· 负责用户中心与订单模块接口开发，QPS 从 200 提升至 800"],
    ["PROJECTS", "高并发秒杀系统（2025）: 使用 Redis 预扣库存 + MQ 削峰，压测 TPS 达 5000+"],
    ["EDUCATION", "XX University, Computer Science, Bachelor (2022-2026)"],
    ["HONORS", "蓝桥杯省一 / 国家励志奖学金"],
]
t2t = Table([[Paragraph(v, st("c2", fontSize=10, leading=15, textColor=HexColor("#FFFFFF")) if False else st("c2", fontSize=10, leading=15))
              for v in row] for row in t2], colWidths=[30*mm, 140*mm])
t2t.setStyle(TableStyle([
    ("FONTNAME",(0,0),(-1,-1),"SimHei"),("VALIGN",(0,0),(-1,-1),"TOP"),
    ("SPAN",(0,0),(1,0)),
    ("BACKGROUND",(0,0),(-1,0),DARK),("TEXTCOLOR",(0,0),(1,0),HexColor("#FFFFFF")),
    ("BACKGROUND",(0,1),(-1,1),DARK),("TEXTCOLOR",(0,1),(1,1),HexColor("#FFFFFF")),
    ("BACKGROUND",(0,2),(-1,2),HexColor("#2E4053")),
    ("BACKGROUND",(0,3),(-1,3),HexColor("#2E4053")),
    ("BACKGROUND",(0,4),(-1,4),HexColor("#2E4053")),
    ("BACKGROUND",(0,5),(-1,5),HexColor("#2E4053")),
    ("BACKGROUND",(0,6),(-1,6),HexColor("#2E4053")),
    ("TOPPADDING",(0,0),(-1,-1),5),("BOTTOMPADDING",(0,0),(-1,-1),5),
]))
story.append(t2t)
story.append(Spacer(1, 5*mm))
story.append(Paragraph("💡 填写提示：英文版式适合外企/大厂，技能用关键词堆叠，项目突出「技术难点+解决+量化收益」。", hint_st))
story.append(PageBreak())

# ===== 模板三 =====
story.append(section_bar("模板三 · 应届生清爽款（实习/校招通用）", TEAL))
story.append(Spacer(1, 5*mm))
story.append(Paragraph("适用：校招/实习投递，清新醒目，突出应届生潜力。", small_st))
story.append(Spacer(1, 4*mm))
t3 = [
    ["王五", "计算机应届生 · 求职意向：后端开发/数据分析"],
    ["联系方式", "138****8888 | wangwu@email.com | 深圳 | 随时到岗"],
    ["教育背景", "XX大学 计算机科学与技术 本科（2022-2026） · 主修：数据结构/OS/数据库/计网"],
    ["专业技能", "熟悉Java/Spring Boot；掌握MySQL、Redis；了解Linux、Git、Docker"],
    ["项目经历", "校园外卖点餐小程序（2025）：微信小程序+Spring Boot，实现点餐/支付模拟/订单管理"],
    ["自我评价", "学习能力强，6个月从零到完成两个项目；有团队协作经验；抗压、主动"],
    ["相关荣誉", "校三好学生 / 计算机设计大赛省赛三等奖"],
]
t3t = Table([[Paragraph(v, st("c3", fontSize=10, leading=15)) for v in row] for row in t3], colWidths=[26*mm, 144*mm])
t3t.setStyle(TableStyle([
    ("FONTNAME",(0,0),(-1,-1),"SimHei"),("VALIGN",(0,0),(-1,-1),"TOP"),
    ("SPAN",(0,0),(1,0)),
    ("BACKGROUND",(0,0),(-1,0),TEAL),("TEXTCOLOR",(0,0),(1,0),HexColor("#FFFFFF")),
    ("BACKGROUND",(0,1),(-1,-1),HexColor("#FFFFFF")),
    ("TOPPADDING",(0,0),(-1,-1),5),("BOTTOMPADDING",(0,0),(-1,-1),5),
    ("LINEBELOW",(0,0),(-1,-1),0.4,HexColor("#E4E3DD")),
]))
story.append(t3t)
story.append(Spacer(1, 5*mm))
story.append(Paragraph("💡 填写提示：无实习也可投——用「项目经历+自我评价」体现能力，求职意向写具体岗位。", hint_st))
story.append(PageBreak())

# ===== 结尾 =====
story.append(section_bar("🎯 简历避坑清单", NAVY))
story.append(Spacer(1, 5*mm))
for line in [
    "❌ 不要超过一页纸（应届生尤其如此）",
    "❌ 不要写「负责/参与」空话，要写「做了什么+结果如何」",
    "❌ 不要有错别字/格式混乱，会直接暴露不细心",
    "✅ 投递前针对岗位改技术栈关键词",
    "✅ 项目写「技术+动作+量化结果」（如：优化SQL，接口提速30%）",
    "✅ 附上 GitHub / 作品链接（有真实项目是加分项）",
]:
    story.append(Paragraph(line, body_st))
story.append(Spacer(1, 8*mm))
story.append(Paragraph("—— 脆脆鲸 · 数字产品出品 ——", st("end", fontSize=10, alignment=TA_CENTER, textColor=GRAY)))

doc.build(story)
print(f"✅ 已生成: {OUT}")
