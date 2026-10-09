#!/usr/bin/env python3
"""
update_readme.py
Fetch daily dynamic Hysteria 2 test nodes from ihavean.app API
and update multi-language READMEs (README.md, README_EN.md, README_CN.md)
"""

import sys
import re
import json
import urllib.request
from datetime import datetime, timezone, timedelta

MSK_TZ = timezone(timedelta(hours=3))
API_URL = "https://ihavean.app/sub/today-info"

def fetch_node_info():
    req = urllib.request.Request(API_URL, headers={"User-Agent": "GitHub-Actions-Update-Bot"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        if resp.status != 200:
            raise RuntimeError(f"API returned status {resp.status}")
        data = json.loads(resp.read().decode("utf-8"))
        return data

def build_replacement_block(info, lang="ru"):
    server = info.get("server", "ru.ihavean.app")
    port = info.get("port", 63779)
    user = info.get("user", "trial_100g")
    password = info.get("password", "")
    token = info.get("daily_token", "")
    hopping = info.get("port_hopping", "37000-38000")
    speed = info.get("speed_mbps", 12)
    node_name = info.get("node_name", "ihavean.app/ru")
    sub_url = info.get("sub_url", f"https://ihavean.app/sub/trial100g?key={token}")

    hy2_link = f"hy2://{user}:{password}@{server}:{port}/?insecure=1&sni=hellousa.com&mport={hopping}#{node_name}"
    now_msk = datetime.now(MSK_TZ).strftime("%Y-%m-%d %H:%M MSK")

    if lang == "en":
        block = f"""<!-- DYNAMIC_NODE_START -->
> 🕒 **Last Updated**: `{now_msk}` | 🎁 **Daily Quota**: `100 GB/day` | ⚡ **Speed**: `{speed} Mbps (4K 60fps)`  
> 🔄 **Daily Key Reset**: Every day at 00:00 MSK (UTC+3)

### 📌 Active Node Today (1-Click Copy):

```text
{hy2_link}
```

### 🔗 Universal Subscription URL:

```text
{sub_url}
```
*(Supports v2rayN, Nekoray, NekoBox, Sing-box, Clash Meta, Shadowrocket, Surge)*
<!-- DYNAMIC_NODE_END -->"""
    elif lang == "cn":
        block = f"""<!-- DYNAMIC_NODE_START -->
> 🕒 **最近更新时间**: `{now_msk}` | 🎁 **每日免费配额**: `100 GB/天` | ⚡ **连接速率**: `{speed} Mbps (4K 60fps 秒开)`  
> 🔄 **凭证轮换时钟**: 每天 00:00 莫斯科时间（北京时间 05:00）全自动重置

### 📌 今日最新节点（点击代码块一键复制）:

```text
{hy2_link}
```

### 🔗 万能自动订阅链接（客户端直接导入）:

```text
{sub_url}
```
*(支持 v2rayN、Nekoray、NekoBox、Sing-box、Clash Meta、Shadowrocket、Surge 等全平台客户端)*
<!-- DYNAMIC_NODE_END -->"""
    else:  # Russian (default)
        block = f"""<!-- DYNAMIC_NODE_START -->
> 🕒 **Последнее обновление**: `{now_msk}` | 🎁 **Лимит**: `100 ГБ/день` | ⚡ **Скорость**: `{speed} Мбит/с (4K 60fps)`  
> 🔄 **Сброс ключа**: ежедневно в 00:00 МСК (UTC+3)

### 📌 Актуальный узел на сегодня (1-Click Copy):

```text
{hy2_link}
```

### 🔗 Универсальная ссылка на авто-подписку (Subscription URL):

```text
{sub_url}
```
*(Подходит для v2rayN, Nekoray, NekoBox, Sing-box, Clash Meta, Shadowrocket, Surge)*
<!-- DYNAMIC_NODE_END -->"""

    return block

def update_file(file_path, new_block):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        pattern = r"<!-- DYNAMIC_NODE_START -->.*?<!-- DYNAMIC_NODE_END -->"
        if not re.search(pattern, content, flags=re.DOTALL):
            print(f"⚠️ Placeholder tags not found in {file_path}, skipping.")
            return

        new_content = re.sub(pattern, new_block, content, flags=re.DOTALL)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)

        print(f"✅ {file_path} updated successfully!")
    except Exception as e:
        print(f"❌ Failed to update {file_path}: {e}")

def main():
    print(f"Fetching fresh credentials from {API_URL}...")
    info = fetch_node_info()
    print(f"Fetched token: {info.get('daily_token')}, password: {info.get('password')}")

    targets = [
        ("README.md", "ru"),
        ("README_EN.md", "en"),
        ("README_CN.md", "cn")
    ]

    for filename, lang in targets:
        block = build_replacement_block(info, lang=lang)
        update_file(filename, block)

if __name__ == "__main__":
    main()
