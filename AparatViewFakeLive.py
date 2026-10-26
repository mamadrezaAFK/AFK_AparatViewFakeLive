import asyncio
from curl_cffi.requests import AsyncSession

proxies_list = [
    "http://185.143.232.10:8080",
    "http://91.107.160.45:3128",
]

# Eshgham Proxy hato inja Beza (Tarjihan Poli Bashe KHaily Khafan tar kar dar miad va ip hat block nmishan tavasote aparat) 

async def real_fake_viewer(proxy, stream_api_url):

    async with AsyncSession(impersonate="chrome110") as session:
        
        proxy_dict = {"http": proxy, "https": proxy}
        try:
          
            response = await session.get(stream_api_url, proxies=proxy_dict, timeout=10)

            if response.status_code == 200:
                print(f"[+] Connected via {proxy} | Status: {response.status_code}")
                
  
                while True:
                    await asyncio.sleep(10)
        
                    hb_response = await session.get(f"{stream_api_url}/ping", proxies=proxy_dict)

                    print(f"[*] Heartbeat sent via {proxy} - Status: {hb_response.status_code}")
                    
        except Exception as e:
            print(f"[-] Failed with {proxy}: {e}")

async def main():
# inja link streamet ro Bezar 
    stream_api_url = "https://www.aparat.com/mamadrezaAFK"
    
    tasks = [real_fake_viewer(proxy, stream_api_url) for proxy in proxies_list]

    await asyncio.gather(*tasks)

if __name__ == "__main__":

    asyncio.run(main())
