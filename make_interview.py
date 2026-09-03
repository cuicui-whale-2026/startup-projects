# -*- coding: utf-8 -*-
"""
D方向 产品7：求职面试题库（计算机岗）PDF
Java 后端高频面试题 + 参考答案
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, PageBreak)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER

pdfmetrics.registerFont(TTFont("SimHei", r"C:\Windows\Fonts\simhei.ttf"))

NAVY = HexColor("#17365D")
BLUE = HexColor("#5B9BD5")
RED = HexColor("#C0392B")
ORANGE = HexColor("#E67E22")
GREEN = HexColor("#1E8E6E")
GRAY = HexColor("#6B7280")
BG = HexColor("#F8F9FB")

OUT = r"C:\Users\31125\Doubao\chats\2026-09-01\new-chat-1\startup-projects\求职面试题库_计算机岗.pdf"

def st(name, **kw):
    base = dict(fontName="SimHei", leading=18, spaceAfter=6)
    base.update(kw)
    return ParagraphStyle(name, **base)

title_st = st("t", fontSize=26, leading=34, alignment=TA_CENTER, textColor=NAVY)
sub_st = st("s", fontSize=12, leading=18, alignment=TA_CENTER, textColor=GRAY)
body_st = st("b", fontSize=10.5, leading=17, textColor=HexColor("#333333"))
q_st = st("q", fontSize=11, leading=17, textColor=NAVY, spaceBefore=10, spaceAfter=2)
a_st = st("a", fontSize=10, leading=16, textColor=HexColor("#444444"), leftIndent=14)
tag_st = st("tag", fontSize=8.5, leading=12, textColor=HexColor("#FFFFFF"))

def section_bar(text, color):
    t = Table([[Paragraph(text, st("sb", fontSize=13, leading=16, textColor=HexColor("#FFFFFF"))) ]],
              colWidths=[170*mm])
    t.setStyle(TableStyle([("BACKGROUND", (0,0), (-1,-1), color),
                           ("TOPPADDING",(0,0),(-1,-1),6),("BOTTOMPADDING",(0,0),(-1,-1),6),
                           ("LEFTPADDING",(0,0),(-1,-1),10)]))
    return t

def qa(q, a, tag="必背", tagcolor=ORANGE):
    out = []
    t = Table([[Paragraph(f"<b>{tag}</b>", tag_st)]], colWidths=[22*mm])
    t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),tagcolor),
                           ("TOPPADDING",(0,0),(-1,-1),2),("BOTTOMPADDING",(0,0),(-1,-1),2),
                           ("ALIGN",(0,0),(-1,-1),"CENTER")]))
    h = Table([[t, Paragraph(q, q_st)]], colWidths=[26*mm, 144*mm])
    h.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"MIDDLE"),
                           ("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),0),
                           ("BOTTOMPADDING",(0,0),(-1,-1),2)]))
    out.append(h)
    out.append(Paragraph(a, a_st))
    out.append(Spacer(1, 4*mm))
    return out

doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=20*mm, rightMargin=20*mm,
                        topMargin=20*mm, bottomMargin=20*mm)
story = []

# ===== 封面 =====
story.append(Table([[""]], colWidths=[170*mm], rowHeights=[8*mm], style=TableStyle([
    ("BACKGROUND",(0,0),(-1,-1),NAVY),("TOPPADDING",(0,0),(-1,-1),0),("BOTTOMPADDING",(0,0),(-1,-1),0)])))
story.append(Spacer(1, 40*mm))
story.append(Paragraph("求职面试题库", title_st))
story.append(Paragraph("计算机岗位 · Java 后端高频 50 题 + 参考答案", sub_st))
story.append(Spacer(1, 12*mm))
story.append(Paragraph("八股文 + 手写 + 场景 + HR 面，一次吃透", st("c", fontSize=13, alignment=TA_CENTER, textColor=GREEN)))
story.append(Spacer(1, 30*mm))
story.append(Paragraph("脆脆鲸 · 数字产品", st("f", fontSize=10, alignment=TA_CENTER, textColor=GRAY)))
story.append(PageBreak())

# ===== Java =====
story.append(section_bar("一、Java 基础（高频必背）", RED))
story.append(Spacer(1, 4*mm))
story += qa("1. == 和 equals() 的区别？", "== 比较引用地址（基本类型比数值）；equals() 是方法，默认比较地址，但 String/Integer 等重写后比较内容。重写 equals() 必须重写 hashCode()，保证相同对象哈希一致。")
story += qa("2. String、StringBuilder、StringBuffer 区别？", "String 不可变，每次拼接生成新对象；StringBuffer 线程安全（方法加 synchronized），效率低；StringBuilder 非线程安全，效率最高。单线程场景用 StringBuilder。")
story += qa("3. HashMap 底层原理？", "数组+链表+红黑树（JDK8+）。put：计算 hash → 定位桶 → 冲突链式 → 链表>8 转红黑树；扩容：默认 0.75 负载因子，2 倍扩容。线程不安全（用 ConcurrentHashMap）。")
story += qa("4. ArrayList 和 LinkedList 区别？", "ArrayList 基于动态数组，随机访问 O(1)，增删慢（需移动）；LinkedList 基于双向链表，增删快，随机访问 O(n)。底层都是 fail-fast 迭代器。")
story += qa("5. 线程池核心参数？", "核心线程数 corePoolSize、最大线程数 maximumPoolSize、空闲存活 keepAliveTime、工作队列 workQueue、线程工厂 threadFactory、拒绝策略 handler。拒绝策略：AbortPolicy（抛异常）/CallerRunsPolicy（调用者执行）/DiscardPolicy（丢弃）。")
story.append(PageBreak())

# ===== 并发 =====
story.append(section_bar("二、并发与 JVM", RED))
story.append(Spacer(1, 4*mm))
story += qa("6. synchronized 和 ReentrantLock 区别？", "synchronized 是 JVM 关键字，自动释放；ReentrantLock 是 JUC 类，可手动 lock/unlock，支持公平锁、可中断、可超时、多条件。性能相差不大，功能上 ReentrantLock 更丰富。")
story += qa("7. volatile 作用？", "保证可见性（写后立即刷主内存）和禁止指令重排；不保证原子性。适合状态标志位，不适合 i++ 这类复合操作。")
story += qa("8. 说下 JVM 内存区域？", "线程共享：堆（对象）、方法区（类信息/常量）；线程私有：虚拟机栈、本地方法栈、程序计数器。堆又分新生代（Eden+2个Survivor）和老年代。")
story += qa("9. GC 如何判断对象可回收？", "可达性分析：从 GC Roots 出发不可达的对象可回收。常见收集器：CMS（并发标记清除，低停顿）、G1（分区+可预测停顿，默认）、ZGC（超低延迟）。")
story += qa("10. 说下类加载过程？", "加载 → 验证 → 准备 → 解析 → 初始化。双亲委派：子类加载器先委托父类，父类找不到才自己加载，保证核心类不被篡改。")
story.append(PageBreak())

# ===== Spring =====
story.append(section_bar("三、Spring 全家桶", BLUE))
story.append(Spacer(1, 4*mm))
story += qa("11. Spring 的 IOC 和 AOP 是什么？", "IOC 控制反转：对象创建和管理交给容器（BeanFactory/ApplicationContext），解耦。AOP 面向切面：把日志/事务/权限等横切逻辑抽出来，动态代理实现（JDK 动态代理/CGLIB）。")
story += qa("12. Spring Bean 生命周期？", "实例化 → 属性填充 → Aware 回调 → BeanPostProcessor 前置 → init-method → BeanPostProcessor 后置 → 使用 → destroy。")
story += qa("13. SpringBoot 自动配置原理？", "@SpringBootApplication 包含 @EnableAutoConfiguration，通过 spring.factories 加载自动配置类，配合 @Conditional 条件注解按需装配。")
story += qa("14. Spring 事务失效场景？", "同类方法内部调用、方法非 public、异常被 catch 吞掉、rollbackFor 没指定、数据库引擎不支持事务（MyISAM）、代理没生效。")
story += qa("15. MyBatis 和 JPA 区别？", "MyBatis 半自动，手写 SQL，灵活可控，适合复杂查询；JPA/Hibernate 全自动 ORM，开发快，复杂 SQL 难优化。国内公司 MyBatis-Plus 最常用。")
story.append(PageBreak())

# ===== MySQL/Redis =====
story.append(section_bar("四、MySQL 与 Redis", ORANGE))
story.append(Spacer(1, 4*mm))
story += qa("16. 索引为什么用 B+ 树？", "B+ 树矮胖（层数少，IO 少）、叶子节点有序链表（范围查询快）、非叶子只存 key（页能装更多）。对比：Hash 不支持范围查询；B 树非叶子也存数据，占用大。")
story += qa("17. 事务隔离级别有哪些？", "读未提交（脏读）、读已提交（不可重复读）、可重复读（MySQL 默认，靠 MVCC 解决，仍可能幻读）、串行化（最高，性能差）。")
story += qa("18. 什么时候索引失效？", "左模糊 %xx、对列做运算或函数、隐式类型转换、OR 连接非索引列、联合索引不满足最左前缀、数据量小优化器放弃索引。")
story += qa("19. Redis 为什么快？", "纯内存 + 单线程（避免上下文切换/锁竞争）+ IO 多路复用（epoll）+ 高效数据结构（跳表等）。")
story += qa("20. Redis 缓存穿透/击穿/雪崩？", "穿透：查不存在的数据 → 布隆过滤器/缓存空值；击穿：热点 key 过期 → 互斥锁/逻辑过期；雪崩：大量 key 同时过期 → 过期时间加随机值/多级缓存。")
story.append(PageBreak())

# ===== 网络/OS/算法 =====
story.append(section_bar("五、计网 + OS + 算法", GREEN))
story.append(Spacer(1, 4*mm))
story += qa("21. TCP 三次握手四次挥手？", "握手：SYN → SYN+ACK → ACK，确认双方收发能力。挥手：FIN → ACK → FIN → ACK，因为 TCP 全双工，需两边分别关闭。", "必背")
story += qa("22. HTTP 和 HTTPS 区别？", "HTTPS = HTTP + TLS，加密传输（对称加密+非对称交换密钥），默认 443 端口，防止中间人攻击。", "必背")
story += qa("23. 进程和线程区别？", "进程是资源分配最小单位，线程是 CPU 调度最小单位；进程间隔离（独立地址空间），线程共享进程资源；进程切换开销大。", "必背")
story += qa("24. 死锁的四个必要条件？", "互斥、占有且等待、不可剥夺、循环等待。破坏任一即可避免死锁（如资源有序分配）。", "必背")
story += qa("25. 手写快排/二分/单例？", "快排：选 pivot 分区递归；二分：有序数组折半；单例：双重检查锁 DCL（volatile + synchronized）。算法题建议每道都手写一遍。", "必背")
story.append(PageBreak())

# ===== 场景 + HR =====
story.append(section_bar("六、场景题 + HR 面", NAVY))
story.append(Spacer(1, 4*mm))
story += qa("26. 设计一个秒杀系统？", "前端限流（按钮置灰）+ 接口层限流（令牌桶）+ Redis 预扣库存 + MQ 削峰异步下单 + 数据库库存扣减。重点：防超卖（Redis Lua 原子扣减）。", "场景")
story += qa("27. 设计短链接服务？", "发号器（雪花/自增）生成短码 → 存 Redis（key=短码, value=长链接）→ 302 跳转。要点：发号器 ID 转 62 进制压缩。", "场景")
story += qa("28. 如何排查线上 OOM？", "看监控报警 → 导出 dump 文件 → 用 MAT/JProfiler 分析 → 定位大对象/内存泄漏 → 优化代码或加大内存。")
story += qa("29. 自我介绍怎么说？", "1分钟版：姓名学历 + 技术栈 + 1个亮点项目（讲清难点和成果）+ 求职意向。别背简历，讲你做了什么、结果如何。", "HR")
story += qa("30. 你最大的缺点？", "说真实但可改进的缺点+改进动作。如：'我过去容易钻牛角尖，后来学会先定优先级再深入'。别说'我太完美'这类。", "HR")
story.append(Spacer(1, 6*mm))

story.append(section_bar("🎯 面试通关心法", NAVY))
story.append(Spacer(1, 4*mm))
for line in [
    "1. 八股文要「理解后用自己的话讲」，背稿会被追问击穿",
    "2. 项目一定要讲「技术难点 + 解决方案 + 量化结果」",
    "3. 手写题提前练：快排/二分/链表反转/单例/生产者消费者",
    "4. 反问环节问「团队技术栈/业务方向」，体现主动性",
    "5. 面完复盘：记录被问倒的题，查漏补缺下一面补上",
]:
    story.append(Paragraph(line, body_st))
story.append(Spacer(1, 8*mm))
story.append(Paragraph("—— 脆脆鲸 · 数字产品出品 ——", st("end", fontSize=10, alignment=TA_CENTER, textColor=GRAY)))

doc.build(story)
print(f"✅ 已生成: {OUT}")
