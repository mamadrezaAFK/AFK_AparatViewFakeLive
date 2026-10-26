<div align="center">

  <h1>🚀 Aparat Async ViewBot & Stream Pinger</h1>
  <p><strong>High-Performance Asynchronous Layer-7 Stream Viewer & Heartbeat Engine for Aparat Live</strong></p>

  [![Website](https://img.shields.io/badge/Official_Website-mamadrezaafk.top-blue?style=for-the-badge&logo=googlechrome&logoColor=white)](https://mamadrezaafk.top)
  [![Discord](https://img.shields.io/badge/Discord-Join_Community-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/GY5mSJFg77)
  [![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
  [![Asyncio](https://img.shields.io/badge/Architecture-Asyncio%20%2F%20Aiohttp-orange.svg?style=for-the-badge)]()
  [![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)

  <p align="center">
    An ultra-lightweight, high-concurrency standalone Python security & traffic engine engineered to simulate and manage <strong>Layer-7 Stream Viewers</strong> and maintain persistent WebSocket/Heartbeat sessions with zero memory bloat.
  </p>

</div>

---

## ⚡ Overview

Traditional view-botting scripts rely on heavy, resource-draining headless browsers (like Selenium) that immediately exhaust server RAM and trigger IP rate-limits. **Aparat Async ViewBot** operates directly on **Layer 7 (Application Layer)** using asynchronous coroutines and advanced TLS fingerprint emulation.

Designed for performance and scalability, this engine handles hundreds of concurrent persistent connections while maintaining minimal system footprint and clean proxy rotation.

---

## ✨ Features

- **🚀 Maximum Performance (Zero RAM Bloat):** Pure Python `asyncio` and `curl_cffi` implementation replacing resource-heavy browser instances with asynchronous coroutines.
- **🎯 Advanced TLS Fingerprint Emulation:** Bypasses Cloudflare and modern anti-bot protections by impersonating real browser TLS profiles (Chrome 110+).
- **🛡️ Dynamic Proxy Rotation & Pool:**
  - Full support for HTTP/SOCKS5 Residential & Datacenter Proxies.
  - Per-coroutine isolated session routing to prevent IP blacklisting.
- **📊 Persistent Heartbeat Pipeline:** Automated background loops maintaining stable session states and heartbeat packets to ensure accurate stream connection metrics.
- **🌐 100% Standalone & Modular:** Easy to configure, integrate, and deploy on high-speed Linux/Windows VPS environments.

---

## 🏗️ Project Structure
```text
Aparat-Async-ViewBot/
├── main.py               # Core Asynchronous Execution & Event Loop
├── config.json           # Stream Target URL & Proxy Configuration
├── requirements.txt      # Python Dependencies (curl_cffi, asyncio)
└── README.md             # Documentation & Usage Guide
