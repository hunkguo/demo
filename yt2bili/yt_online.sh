#!/bin/bash

#streamlink <油管链接> \
#best \ 								#输出画质最好
#--player-external-http \ 			#以HTTP流的形式对外输出，而不是调用播放器
#--player-external-http-port 8080 \  #输出端口8080，与上面nginx的反代地址一样
#--retry-open 30 \ 					#链接失败时，重复请求30次
#--hls-segment-timeout 600 \ 		#HLS每个切片的最大超时（单位：秒）
#--hls-timeout 900 \				 	#HLS最大超时（单位：秒）
#--http-stream-timeout 900 \ 		#HTTP流最大超时（单位：秒）
#--ringbuffer-size 4M \ 				#缓存大小，默认是16m，在低配置小内存机器下建议调小

# SATURDAY MUSIC HAWAIIAN: Surf Vibes Afternoon - Beach Background Music for Chill, Leisure and Unwind
#yt_url="https://www.youtube.com/watch?v=1szv6XIi_cw"
# Elegant Saturday JAZZ - Delicate JAZZ and Sweet Bossa Nova For Relax, Reading,Dreaming
#yt_url="https://www.youtube.com/watch?v=Scg96Acc31I"
# WEEKEND JAZZ HIPHOP: Chill Out Jazz Hip Hop Beat Music - Have a Nice Weekend!
#yt_url="https://www.youtube.com/watch?v=Tnosxi2omrE"
# COFFEE JAZZ RELAXING: Soft and Sweet Jazz & Bossa Nova for The Best Morning, Good Mood
#yt_url="https://www.youtube.com/watch?v=mMb8h803ePY"
# Relaxing Jazz Piano Radio - Slow Jazz Music - 24/7 Live Stream - Music For Work & Study
#yt_url="https://www.youtube.com/watch?v=Dx5qFachd3A"
# Rainy Jazz: Relaxing Jazz & Bossa Nova Music Radio - 24/7 Chill Out Piano & Guitar Music
yt_url="https://www.youtube.com/watch?v=DSGyEsJ17cI"

streamlink $yt_url best --player-external-http --player-external-http-port 9126 --retry-open 30 --hls-segment-timeout 600 --hls-timeout 900 --http-stream-timeout 900 --ringbuffer-size 4M


