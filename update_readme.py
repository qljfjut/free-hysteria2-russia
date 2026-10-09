#!/usr/bin/env python3
"""
update_readme.py
Fetch daily dynamic Hysteria 2 test nodes from ihavean.app API and update README.md
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

def build_replacement_block(info):
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
*(Подходит для v2rayN, Nekoray, NekoBox, Sing-box, Clash Meta, Shadowrocket)*
<!-- DYNAMIC_NODE_END -->"""
    return block

def update_readme(readme_path="README.md"):
    print(f"Fetching fresh credentials from {API_URL}...")
    info = fetch_node_info()
    print(f"Fetched token: {info.get('daily_token')}, password: {info.get('password')}")

    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    pattern = r"<!-- DYNAMIC_NODE_START -->.*?<!-- DYNAMIC_NODE_END -->"
    new_block = build_replacement_block(info)

    if not re.search(pattern, content, flags=re.DOTALL):
        raise ValueError("Placeholder tags <!-- DYNAMIC_NODE_START --> not found in README.md")

    new_content = re.sub(pattern, new_block, content, flags=re.DOTALL)

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    print("README.md updated successfully!")

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "README.md"
    update_readme(path)
