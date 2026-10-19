#!/bin/bash
CONFIG_FILE="/www/server/panel/vhost/nginx/ansapra.com.conf"

echo "正在修复Nginx配置..."

# 备份原配置
cp "$CONFIG_FILE" "${CONFIG_FILE}.backup.$(date +%Y%m%d%H%M%S)"

# 添加client header配置
if ! grep -q "client_header_buffer_size" "$CONFIG_FILE"; then
  sed -i '/server {/a\    client_header_buffer_size 64k;\n    large_client_header_buffers 4 64k;' "$CONFIG_FILE"
fi

# 添加proxy buffer配置
if grep -q "location /" "$CONFIG_FILE"; then
  sed -i '/location \/ {/a\        proxy_buffer_size 128k;\n        proxy_buffers 4 256k;\n        proxy_busy_buffers_size 256k;' "$CONFIG_FILE"
fi

echo "配置已更新，测试Nginx配置..."
nginx -t

if [ $? -eq 0 ]; then
  echo "重载Nginx..."
  nginx -s reload
  echo "修复完成！"
else
  echo "Nginx配置测试失败，恢复备份..."
  cp "${CONFIG_FILE}.backup" "$CONFIG_FILE"
  nginx -t
fi