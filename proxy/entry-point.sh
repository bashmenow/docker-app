#!/bin/bash
set -e
sed -ie "s|{{NGINX_HOST}}|$NGINX_HOST|" /etc/nginx/conf.d/default.conf
sed -ie "s|{{NGINX_PROXY}}|$NGINX_PROXY|"  /etc/nginx/conf.d/default.conf
cat /etc/nginx/conf.d/default.conf
exec "$@"
