# FFMPEG Processes

```sh
ps -aux | grep ffmpeg
```

```sh
# from cameras to localhost rtsp
/usr/lib/ffmpeg/7.0/bin/ffmpeg -hide_banner -v error -fflags nobuffer -flags low_delay -i https://foodcam.local/flv?port=1935&app=bcs&stream=channel0_main.bcs&user=admin&password=redacted -c copy -user_agent ffmpeg/go2rtc -rtsp_transport tcp -f rtsp rtsp://127.0.0.1:8554/7a0183b99b04e657ef8bed3414b7ae3d
/usr/lib/ffmpeg/7.0/bin/ffmpeg -hide_banner -v error -fflags nobuffer -flags low_delay -i https://countercam.local/flv?port=1935&app=bcs&stream=channel0_main.bcs&user=admin&password=redacted -c copy -user_agent ffmpeg/go2rtc -rtsp_transport tcp -f rtsp rtsp://127.0.0.1:8554/a649d4ca2ba89ad9a11347dc329b63fc

# from localhost rtsp to files AND send 5 fps version to an output pipe
/usr/lib/ffmpeg/7.0/bin/ffmpeg -hide_banner -loglevel warning -threads 2 -user_agent FFmpeg Frigate/0.15.0-cea210d -avoid_negative_ts make_zero -fflags +genpts+discardcorrupt -rtsp_transport tcp -timeout 5000000 -use_wallclock_as_timestamps 1 -i rtsp://127.0.0.1:8554/food -f segment -segment_time 10 -segment_format mp4 -reset_timestamps 1 -strftime 1 -c copy /tmp/cache/food@%Y%m%d%H%M%S%z.mp4 -r 5 -vf fps=5,scale=2560:1920 -threads 2 -f rawvideo -pix_fmt yuv420p pipe:
/usr/lib/ffmpeg/7.0/bin/ffmpeg -hide_banner -loglevel warning -threads 2 -user_agent FFmpeg Frigate/0.15.0-cea210d -avoid_negative_ts make_zero -fflags +genpts+discardcorrupt -rtsp_transport tcp -timeout 5000000 -use_wallclock_as_timestamps 1 -i rtsp://127.0.0.1:8554/counter -f segment -segment_time 10 -segment_format mp4 -reset_timestamps 1 -strftime 1 -c copy /tmp/cache/counter@%Y%m%d%H%M%S%z.mp4 -r 5 -vf fps=5,scale=1920:2560 -threads 2 -f rawvideo -pix_fmt yuv420p pipe:

# from input pipes to resized mppeg transport streams
root        1100  0.0  0.3 157548 16128 ?        Ss   13:44   0:00 /usr/lib/ffmpeg/7.0/bin/ffmpeg -threads 1 -f rawvideo -pix_fmt yuv420p -video_size 2560x1920 -i pipe: -threads 1 -f mpegts -s 960x720 -codec:v mpeg1video -q 8 -bf 0 pipe:
root        1107  0.0  0.3 157548 16128 ?        Ss   13:44   0:00 /usr/lib/ffmpeg/7.0/bin/ffmpeg -threads 1 -f rawvideo -pix_fmt yuv420p -video_size 1920x2560 -i pipe: -threads 1 -f mpegts -s 540x720 -codec:v mpeg1video -q 8 -bf 0 pipe:
root        1114  0.0  0.3 157548 16128 ?        Ss   13:44   0:00 /usr/lib/ffmpeg/7.0/bin/ffmpeg -threads 1 -f rawvideo -pix_fmt yuv420p -video_size 1280x720 -i pipe: -threads 1 -f mpegts -s 1280x720 -codec:v mpeg1video -q 8 -bf 0 pipe:
```

## Camera to RTSP

Looks good! No transcoding.

| **Step** | **Description**                                                                                                                                                          |
|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.       | **Command and Executable Path:** <br> `/usr/lib/ffmpeg/7.0/bin/ffmpeg` - Location of the `ffmpeg` executable.                                                            |
| 2.       | **Hide Banner:** <br> `-hide_banner` - Suppresses the banner that `ffmpeg` normally prints at the start.                                                                 |
| 3.       | **Set Log Level:** <br> `-v error` - Sets the logging level to `error` , meaning only error messages will be shown.                                                        |
| 4.       | **No Buffer:** <br> `-fflags nobuffer` - Minimizes latency by not buffering the input.                                                                                    |
| 5.       | **Low Delay:** <br> `-flags low_delay` - Enables low-latency streaming.                                                                                                  |
| 6.       | **Input Source:** <br> `-i https://foodcam.local/flv?port=1935&app=bcs&stream=channel0_main.bcs&user=admin&password=easypass` - Specifies the input stream URL.           |
| 7.       | **Stream Copy:** <br> `-c copy` - Tells `ffmpeg` to copy the input stream as-is, without re-encoding.                                                                    |
| 8.       | **User Agent:** <br> `-user_agent ffmpeg/go2rtc` - Sets the user agent for the HTTP request to `ffmpeg/go2rtc` .                                                          |
| 9.       | **Transport Protocol:** <br> `-rtsp_transport tcp` - Sets the transport protocol for RTSP to TCP.                                                                        |
| 10.      | **Output Format:** <br> `-f rtsp` - Specifies the output format as RTSP (Real-Time Streaming Protocol).                                                                  |
| 11.      | **Output URL:** <br> `rtsp://127.0.0.1:8554/7a0183b99b04e657ef8bed3414b7ae3d` - Destination URL where the RTSP stream will be sent.                                      |

## RTSP to Files and Output Pipe

Looks good! No transcoding. Output pipe which presumably is for object detection (because of 5 FPS) is not yet reduced in size.

| **Step** | **Description**                                                                                                                  |
|----------|----------------------------------------------------------------------------------------------------------------------------------|
| 1.       | **Command and Executable Path:** <br> `/usr/lib/ffmpeg/7.0/bin/ffmpeg` - Location of the `ffmpeg` executable.                   |
| 2.       | **Hide Banner:** <br> `-hide_banner` - Suppresses the banner that `ffmpeg` normally prints at the start.                        |
| 3.       | **Set Log Level:** <br> `-loglevel warning` - Sets the logging level to `warning` , meaning only warning messages will be shown. |
| 4.       | **Threads:** <br> `-threads 2` - Uses 2 threads for processing.                                                                 |
| 5.       | **User Agent:** <br> `-user_agent FFmpeg Frigate/0.15.0-cea210d` - Sets the user agent for the HTTP request.                    |
| 6.       | **Avoid Negative Timestamps:** <br> `-avoid_negative_ts make_zero` - Zeroes out negative timestamps, ensuring smooth playback.  |
| 7.       | **FFlags:** <br> `-fflags +genpts+discardcorrupt` - Generates presentation timestamps (PTS) if they are missing and discards corrupted frames. |
| 8.       | **RTSP Transport Protocol:** <br> `-rtsp_transport tcp` - Sets the transport protocol for RTSP to TCP.                          |
| 9.       | **Timeout:** <br> `-timeout 5000000` - Sets the timeout for the RTSP stream to 5000000 microseconds (5 seconds).                |
| 10.      | **Use Wallclock as Timestamps:** <br> `-use_wallclock_as_timestamps 1` - Uses wallclock as timestamps.                          |
| 11.      | **Input Source:** <br> `-i rtsp://127.0.0.1:8554/food` - Specifies the input RTSP stream URL.                                    |
| 12.      | **Output Format:** <br> `-f segment` - Specifies the output format as segmented files.                                           |
| 13.      | **Segment Time:** <br> `-segment_time 10` - Sets the segment duration to 10 seconds.                                             |
| 14.      | **Segment Format:** <br> `-segment_format mp4` - Sets the segment format to MP4.                                                  |
| 15.      | **Reset Timestamps:** <br> `-reset_timestamps 1` - Resets the timestamps for each segment.                                        |
| 16.      | **Use strftime:** <br> `-strftime 1` - Uses `strftime` to format the segment filenames.                                           |
| 17.      | **Copy Stream:** <br> `-c copy` - Copies the input stream as-is without re-encoding.                                              |
| 18.      | **Output Location:** <br> `/tmp/cache/food@%Y%m%d%H%M%S%z.mp4` - Specifies the output file path and filename format.             |
| 19.      | **Frame Rate:** <br> `-r 5` - Sets the frame rate to 5 frames per second.                                                        |
| 20.      | **Video Filter:** <br> `-vf fps=5,scale=2560:1920` - Applies video filters to set the frame rate to 5 and scale the video to 2560x1920 resolution. |
| 21.      | **Threads for Raw Video:** <br> `-threads 2` - Uses 2 threads for processing raw video.                                           |
| 22.      | **Pixel Format:** <br> `-f rawvideo -pix_fmt yuv420p` - Specifies the output format as raw video and sets the pixel format to YUV 4:2:0. |
| 23.      | **Pipe Output:** <br> `pipe:` - Sends the output to a pipe, which can be used for further processing.                             |

## Input Pipes to Resized MPEG Transport Streams

Not sure what these are for. It's possible that the input to object detection is being reduced here, which I don't really want.

| **Step** | **Description**                                                                                                                   |
|----------|-----------------------------------------------------------------------------------------------------------------------------------|
| 1.       | **Command and Executable Path:** <br> `/usr/lib/ffmpeg/7.0/bin/ffmpeg` - Location of the `ffmpeg` executable.                    |
| 2.       | **Threads:** <br> `-threads 1` - Uses 1 thread for processing.                                                                   |
| 3.       | **Input Format:** <br> `-f rawvideo` - Specifies the input format as raw video.                                                  |
| 4.       | **Pixel Format:** <br> `-pix_fmt yuv420p` - Sets the pixel format to YUV 4:2:0.                                                  |
| 5.       | **Video Size:** <br> `-video_size 2560x1920` - Sets the input video size to 2560x1920.                                           |
| 6.       | **Input Source:** <br> `-i pipe:` - Specifies the input source as a pipe.                                                        |
| 7.       | **Threads for Output:** <br> `-threads 1` - Uses 1 thread for output processing.                                                 |
| 8.       | **Output Format:** <br> `-f mpegts` - Specifies the output format as MPEG-TS (MPEG Transport Stream).                            |
| 9.       | **Output Size:** <br> `-s 960x720` - Sets the output video size to 960x720.                                                      |
| 10.      | **Output Codec:** <br> `-codec:v mpeg1video` - Sets the output codec to MPEG-1 video.                                            |
| 11.      | **Quality:** <br> `-q 8` - Sets the quality level to 8.                                                                          |
| 12.      | **B-frames:** <br> `-bf 0` - Disables B-frames, which can help reduce latency.                                                   |
| 13.      | **Output Pipe:** <br> `pipe:` - Sends the output to a pipe, which can be used for further processing.                             |
