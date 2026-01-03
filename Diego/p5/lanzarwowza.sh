#!/bin/bash

# Detener contenedor anterior si existe
docker stop wowza 2>/dev/null || true
docker rm wowza 2>/dev/null || true

docker run -it --rm -d  --name wowza\
    -p 1935:1935 -p 8086:8086 -p 8087:8087 -p 8088:8088 \
    -p 5004-5008:5004-5008/udp \
    -e WSE_MGR_USER=wowza \
    -e WSE_MGR_PASS=clavesecreta \
    -v $(pwd)/Server.license:/usr/local/WowzaStreamingEngine/conf/Server.license \
    -v $(pwd)/wowza/applications:/usr/local/WowzaStreamingEngine/applications \
    -v $(pwd)/wowza/conf:/usr/local/WowzaStreamingEngine/conf \
    -v $(pwd)/wowza/content:/usr/local/WowzaStreamingEngine/content \
    --entrypoint /sbin/entrypoint.sh \
    wowzamedia/wowza-streaming-engine-linux:4.8.17