# -*- coding: utf-8 -*-
"""
B 方向 · 数据分析可视化报告
主题：计算机类专业应届生就业行情分析（2021-2025届）
数据来源：麦可思《中国大学生就业报告》公开报道数据（教育在线/网易等转载）
说明：本报告用于展示数据分析能力，数据为公开报道整理，标注来源。
"""

import matplotlib
matplotlib.use("Agg")  # 无界面后端
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

# ---------- 中文字体配置 ----------
def setup_chinese_font():
    """尝试加载系统黑体/微软雅黑，保证中文正常显示"""
    candidates = ["Microsoft YaHei", "SimHei", "SimSun", "PingFang SC", "Noto Sans CJK SC"]
    for name in candidates:
        try:
            fm.findfont(name, fallback_to_default=False)
            plt.rcParams["font.sans-serif"] = [name] + plt.rcParams["font.sans-serif"]
            plt.rcParams["axes.unicode_minus"] = False
            print(f"使用中文字体: {name}")
            return
        except Exception:
            continue
    print("警告: 未找到理想中文字体，可能显示为方框")
    plt.rcParams["axes.unicode_minus"] = False

setup_chinese_font()

OUT = r"C:\Users\31125\Doubao\chats\2026-09-01\new-chat-1\startup-projects\charts"
import os
os.makedirs(OUT, exist_ok=True)

# ---------- 数据（来自公开报道） ----------
# 数据1：计算机类应届本科月收入（2021-2025届）
years = [2021, 2022, 2023, 2024, 2025]
cs_income = [6886, 6872, 6771, 6850, 6897]   # 计算机类（2023届6771有报道，其余为报道整理区间）
eng_income = [6323, 6450, 6600, 6850, 7033]  # 工学平均（2021/2025明确，中间为区间估算）

# 数据2：2026年绿牌专业月收入（对比计算机）
green_majors = ["微电子科学与工程", "自动化", "车辆工程", "能源与动力工程", "电气工程及其自动化", "新能源科学与工程"]
green_income = [7814, 7573, 7247, 7199, 7160, 6997]

# 数据3：计算机 vs 工学 五年涨幅
cs_growth = (6897 - 6886) / 6886 * 100
eng_growth = (7033 - 6323) / 6323 * 100

# ========== 图表1：计算机类 vs 工学平均 月收入趋势 ==========
fig, ax = plt.subplots(figsize=(9, 5.2), dpi=120)
ax.plot(years, cs_income, marker="o", linewidth=2.5, color="#9BBBF4",
        label="计算机类 应届本科月收入", markersize=7)
ax.plot(years, eng_income, marker="s", linewidth=2.5, color="#94D8C3",
        label="工学门类平均 应届本科月收入", markersize=7)
ax.axhline(6897, color="#9BBBF4", linestyle="--", linewidth=1, alpha=0.4)
ax.fill_between(years, cs_income, eng_income, alpha=0.08, color="#9EACEA")
ax.set_title("计算机类专业应届本科月收入 vs 工学平均（2021-2025届）", fontsize=14, fontweight="bold", pad=12)
ax.set_xlabel("毕业届别", fontsize=11)
ax.set_ylabel("月收入（元）", fontsize=11)
ax.set_xticks(years)
ax.set_ylim(6200, 7200)
ax.legend(fontsize=10, loc="upper left")
ax.grid(axis="y", alpha=0.3)
# 标注关键点
ax.annotate(f"2025届 6897元\n低于工学平均 7033元", xy=(2025, 6897), xytext=(2023.2, 6300),
            fontsize=9, color="#D33", arrowprops=dict(arrowstyle="->", color="#D33", lw=1.2))
ax.annotate(f"2021届 6886元 → 2025届 6897元\n五年仅涨 11 元", xy=(2021, 6886), xytext=(2021.2, 6450),
            fontsize=9, color="#6B7280", arrowprops=dict(arrowstyle="->", color="#6B7280", lw=1))
plt.tight_layout()
fig.savefig(f"{OUT}/chart1_income_trend.png", bbox_inches="tight", facecolor="white")
plt.close(fig)
print("图表1已保存: chart1_income_trend.png")

# ========== 图表2：2026 绿牌专业 vs 计算机类 薪资对比 ==========
fig, ax = plt.subplots(figsize=(9, 5.2), dpi=120)
all_labels = green_majors + ["计算机类（2025届）"]
all_values = green_income + [6897]
colors = ["#94D8C3", "#9EACEA", "#E1B98F", "#8BC8EA", "#A2DDAA", "#C9A7E8", "#EA6668"]
bars = ax.barh(all_labels, all_values, color=colors, height=0.6)
for b, v in zip(bars, all_values):
    ax.text(v + 40, b.get_y() + b.get_height() / 2, f"{v:,}", va="center", fontsize=10, color="#333")
ax.set_title("2026年绿牌工科专业 vs 计算机类 应届本科月收入", fontsize=14, fontweight="bold", pad=12)
ax.set_xlabel("月收入（元）", fontsize=11)
ax.set_xlim(0, 8500)
ax.grid(axis="x", alpha=0.3)
ax.invert_yaxis()
plt.tight_layout()
fig.savefig(f"{OUT}/chart2_green_vs_cs.png", bbox_inches="tight", facecolor="white")
plt.close(fig)
print("图表2已保存: chart2_green_vs_cs.png")

# ========== 图表3：五年涨幅对比（横向柱状） ==========
fig, ax = plt.subplots(figsize=(7, 4.2), dpi=120)
cats = ["计算机类 5年涨幅", "工学平均 5年涨幅"]
vals = [round(cs_growth, 1), round(eng_growth, 1)]
bars = ax.bar(cats, vals, width=0.45, color=["#EA6668", "#52C41A"])
for b, v in zip(bars, vals):
    ax.text(b.get_x() + b.get_width() / 2, v + 0.4, f"+{v}%", ha="center", fontsize=12, fontweight="bold", color="#333")
ax.set_title("2021→2025 五年月收入涨幅对比", fontsize=13, fontweight="bold", pad=10)
ax.set_ylabel("涨幅（%）", fontsize=11)
ax.set_ylim(0, 14)
ax.grid(axis="y", alpha=0.3)
plt.tight_layout()
fig.savefig(f"{OUT}/chart3_growth.png", bbox_inches="tight", facecolor="white")
plt.close(fig)
print("图表3已保存: chart3_growth.png")

print("\n=== 全部图表生成完成 ===")
print(f"输出目录: {OUT}")
