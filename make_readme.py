import os
import re

# === 設定 ===
folder = "split_markdown"   # 分割済みファイルのフォルダ
output_file = "README.md"      # 出力先

# === 見出し抽出パターン ===
h1_pattern = re.compile(r"^# (?!#)(.+)")
h2_pattern = re.compile(r"^## (?!#)(.+)")

# === アンカー生成関数 ===
def make_anchor(text):
    """GitHub風アンカー名を生成"""
    anchor = text.lower()
    anchor = re.sub(r"[^\w一-龥ぁ-んァ-ンー]+", "-", anchor)
    anchor = anchor.strip("-")
    return anchor

# === ファイル一覧 ===
files = sorted([f for f in os.listdir(folder) if f.endswith(".md")])

# === 目次生成 ===
lines = []
lines.append("# 🧱 HTML/CSS 学習ノート\n")
lines.append("## 📖 目次\n")

for f in files:
    path = os.path.join(folder, f).replace("\\", "/")
    with open(os.path.join(folder, f), "r", encoding="utf-8") as md:
        content = md.readlines()

    title_h1 = None
    sub_headings = []

    for line in content:
        m1 = h1_pattern.match(line)
        m2 = h2_pattern.match(line)
        if m1 and not title_h1:
            title_h1 = m1.group(1).strip()
        elif m2:
            sub_headings.append(m2.group(1).strip())

    if not title_h1:
        title_h1 = f.replace(".md", "")

    lines.append(f"- [{title_h1}]({path})")

    for sub in sub_headings:
        anchor = make_anchor(sub)
        lines.append(f"  - [{sub}]({path}#{anchor})")

# === ファイル出力 ===
with open(output_file, "w", encoding="utf-8") as out:
    out.write("\n".join(lines))

print(f"✅ {output_file} を生成しました！")
