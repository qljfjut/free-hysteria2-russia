<div align="center">

# ⚡ Free Hysteria 2 Russia • 高速抗封锁抗 QoS 代理节点

### 🌐 [ 🇨🇳 简体中文 ](README_CN.md) &nbsp;•&nbsp; [ 🇬🇧 English ](README_EN.md) &nbsp;•&nbsp; [ 🇷🇺 Русский ](README.md)

[![Daily Node Update](https://github.com/qljfjut/free-hysteria2-russia/actions/workflows/daily-update.yml/badge.svg)](https://github.com/qljfjut/free-hysteria2-russia/actions/workflows/daily-update.yml)
[![Protocol](https://img.shields.io/badge/Protocol-Hysteria%202%20(QUIC)-blue.svg)](https://v2.hysteria.network/)
[![Speed](https://img.shields.io/badge/Speed-12%20Mbps%20(4K%2060fps)-brightgreen.svg)](https://ihavean.app/ru/)
[![Traffic](https://img.shields.io/badge/Daily%20Quota-100%20GB%2Fday-orange.svg)](https://ihavean.app/ru/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

</div>

> 🚀 **基于 Hysteria 2 协议与动态端口跳跃（Port Hopping 37000-38000）** 的高速抗审查与抗 QoS 限速节点。专治晚高峰 UDP 断流、运营商 QoS 降速及强 DPI 审查封锁（支持 YouTube 4K、Telegram、Discord、Instagram 及全球网页自由访问）。  
> 🔄 **节点每天莫斯科时间 00:00（北京时间 05:00）全自动更新轮换**。

---

## 🎁 今日活跃免费测试节点（每日更新）

<!-- DYNAMIC_NODE_START -->
> 🕒 **最近更新时间**: `2026-10-09 06:28 MSK` | 🎁 **每日免费配额**: `100 GB/天` | ⚡ **连接速率**: `12 Mbps (4K 60fps 秒开)`  
> 🔄 **凭证轮换时钟**: 每天 00:00 莫斯科时间（北京时间 05:00）全自动重置

### 📌 今日最新节点（点击代码块一键复制）:

```text
hy2://trial_100g:hy2_trial_8m4k_20261009@ru.ihavean.app:63779/?insecure=1&sni=hellousa.com&mport=37000-38000#ihavean.app/ru
```

### 🔗 万能自动订阅链接（客户端直接导入）:

```text
https://ihavean.app/sub/trial100g?key=a3473e69
```
*(支持 v2rayN、Nekoray、NekoBox、Sing-box、Clash Meta、Shadowrocket、Surge 等全平台客户端)*
<!-- DYNAMIC_NODE_END -->

---

## 🌐 官方大本营与社群矩阵

* 🌍 **官方落地页与状态监控**: [https://ihavean.app/ru/](https://ihavean.app/ru/)
* 📢 **Telegram 官方频道（每日零点自动推送）**: [@ihaveanapp_ru](https://t.me/ihaveanapp_ru)
* 🤖 **Telegram 客服与指引机器人**: [@IHaveAnAppRU_Bot](https://t.me/IHaveAnAppRU_Bot)

---

## 🛠️ 全平台客户端极速配置指南（1 分钟上手）

### 1. Windows / macOS / Linux
* **推荐客户端**：**Nekoray** / **v2rayN** / **Sing-box**
1. 复制上方 `hy2://...` 节点单行代码；
2. 在客户端界面选择 **从剪贴板导入**（Import from Clipboard）；
3. 选中 `ihavean.app/ru` 节点并开启 系统代理 / TUN 虚拟网卡模式；
4. 打开 YouTube 测试 4K 60fps 视频播放，秒开无缓冲。

### 2. Android（安卓手机）
* **推荐客户端**：**NekoBox**（GitHub / F-Droid 下载）或 **Sing-box** / **Clash Meta for Android**
1. 复制 `hy2://...` 字符串或万能订阅链接；
2. 点击右上角 `+` 号 ➔ 选择 `从剪切板导入`；
3. 点击右下角运行按钮开启代理。

### 3. iOS（iPhone / iPad）
* **推荐客户端**：**Shadowrocket (小火箭)** / **Surge** / **Sing-box** / **Streisand**
1. 复制万能订阅链接 `https://ihavean.app/sub/trial100g?key=...`；
2. 打开 Shadowrocket，点击右上角 `+`，类型选择 `Subscribe`，粘贴链接并完成更新；
3. 或直接复制 `hy2://...` 打开小火箭，小火箭会自动弹出是否添加节点提示，点击保存即可。

---

## ⚡ 为什么 Hysteria 2 能暴力穿透强审查与 QoS 限速？

| 核心特性 | 传统 VPN (WireGuard / OpenVPN) | Shadowsocks | Hysteria 2 (本项目方案) |
| :--- | :---: | :---: | :---: |
| **YouTube 4K 播放能力** | ❌ 被运营商 QoS 限速至 128 Kbps | ⚠️ 高峰期频繁转圈缓冲 | ✅ **12 Mbps 稳定独享跑满 4K** |
| **抗 DPI 深度特征嗅探** | ❌ 握手特征明显，易被直接阻断 | ⚠️ 统计学与主动探测易识别 | ✅ **标准 QUIC 协议伪装为 HTTPS** |
| **抗单端口 UDP QoS 降速** | ❌ 运营商单端口限速直接瘫痪 | ❌ 遭遇大面积 UDP 丢包 | ✅ **Linux 内核级动态端口跳跃 (37000-38000)** |
| **高丢包恶劣链路表现** | 吞吐量骤降 70%+ | 延迟飙升至 2000ms+ | ✅ **定制版激进 BBR 拥塞控制算法** |

---

## ⚖️ 安全与使用合规守则
* 服务端配置了严格的出站安全沙箱 ACL（阻断内网回环与宿主机 IP、封死邮件 SMTP 25/465/587 端口防滥发）；
* 本节点专供学术研究、跨国远程办公、流媒体娱乐与反审查测试；
* 访问凭据每 24 小时动态轮换。建议将本仓库加星（**⭐ Star**）收藏，或订阅 [@ihaveanapp_ru](https://t.me/ihaveanapp_ru) 获取持续连接。

---

## 📄 开源许可
本项目遵循开放的 [MIT License](LICENSE) 协议。
