FROM nginx:1.17.9

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY entry-point.sh /entry-point.sh
ENTRYPOINT ["/entry-point.sh"]
CMD ["nginx", "-g", "daemon off;"]