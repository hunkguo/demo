#!/bin/bash

#ffmpeg \
#-rw_timeout 30000000 \                            #超时值：30s
#-i http://127.0.0.1:9126/ \       #流输入
#-c copy \                                         #直接复制流
#-f flv \                                          #重新封装为flv
#-bsf:a aac_adtstoasc\                             #对于flv格式中的AAC，需要用到这个filter
#rtmp://live-push.bilivideo.com/live-bvc/?streamname=live_37742441_61916176&key=fd0e27eb6d779279d273024b50ca12af&schedule=rtmp                                #流输出


#有些直播源不能用
#ffmpeg -rw_timeout 30000000 -i "http://localhost:9126/" -c copy -f flv -bsf:a aac_adtstoasc "rtmp://qn.live-send.acg.tv/live-qn/?streamname=live_37742441_61916176&key=fd0e27eb6d779279d273024b50ca12af&schedule=rtmp"
#                                                                                                                                 ?streamname=live_37742441_61916176&key=fd0e27eb6d779279d273024b50ca12af&schedule=rtmp

#似乎兼容性好

#ffmpeg -re -i "http://localhost:9126/" -vcodec copy -acodec aac -b:a 192k -f flv "rtmp://qn.live-send.acg.tv/live-qn/?streamname=live_37742441_61916176&key=fd0e27eb6d779279d273024b50ca12af&schedule=rtmp"


play_video_name="./media/Hawaiian Cafe - Beach Relaxing Guitar Music for Resting, Taking a Nap, Chill-_Pso4chWMSg.mkv"

push_video="rtmp://qn.live-send.acg.tv/live-qn/?streamname=live_37742441_61916176&key=fd0e27eb6d779279d273024b50ca12af&schedule=rtmp"

ffmpeg -re -stream_loop -1 -i "$play_video_name" \
-vcodec copy -acodec aac -b:a 192k -f flv "$push_video"
