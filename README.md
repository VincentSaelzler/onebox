## Raspberry Pi

Configure the base image with the Raspberry Pi Imager program.

1. OTHER Raspberry Pi OS
1. Lite 64 Bit
1. hostname: backdoor.local
1. un/pw vince/[from lastpass]
1. set time zone and keyboard layout
1. enable ssh with public key only [key from lastpass]

Inject secret vault password and set up aliases to use that plus the inventory file.

```sh
sudo apt update
sudo apt full-upgrade
sudo apt autoremove
sudo apt install ansible git
git clone https://github.com/VincentSaelzler/onebox/
cd onebox/ansible
ansible-playbook 0-ansible-bootstrap.yml --ask-vault-pass
source ~/.bashrc
```

# run playbooks

cd ansible
ans [playbook.yml]

```

### Useful Commands

```sh
# view git log in graph format
glog

# wipe out a container
pct destroy 103 --force true --destroy-unreferenced-disks true --purge true
```

### Proxmox Virtualization Host

Wipe NVMe SSDs

```sh
# the adata one looks messed up.
# it shows different results after the same command is run multiple times
hexdump -C -n 1048576 /dev/nvme0n1 | tail

# first run
000ffe00  c6 dd d7 e2 a0 97 4b 88  19 a7 c2 89 72 75 85 d5  |......K.....ru..|
000ffe10  2e 58 10 ad 1d a0 e4 1b  c7 e3 8b 0c e6 23 6e 69  |.X...........#ni|
000ffe20  23 38 d5 33 d2 91 13 9a  21 58 61 75 41 7e 29 24  |#8.3....!XauA~)$|
[non-zero data continues all the way to....]
00100000

# second run
000ffe00  dd e0 66 66 02 00 00 c2  55 55 02 56 03 00 80 c1  |..ff....UU.V....|
000ffe10  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
*
00100000

# perhaps (long shot) since the drive was formatted, but no data yet written,
# it returns arbitrary stuff until data is written?
badblocks -wsv /dev/nvme0n1
```

### Networking

Manually create the vlan bridge, or copy the interfaces file.

```sh
scp ./ansible/files/interfaces root@pve.local:/etc/network/interfaces
```

### Reolink Camera

#### Initialization via Reolink App (NOT Web UI)

* Set PW
* Camera Name: Food

Display

* OSD > Hide Everything

Stream

* Clear
  + Max Bitrate (kbps): 8192 (max allowed option)
  + I-frame Interval: 1x
* Bitrate Mode: Constant Bitrate

Sounds

* Record Audio: On

Network

* Advanced > Server Settings
  + RTSP: On / 554

## Sound Not Working

Try changing back to RTSP

```sh
v3.0.0.2033_23041302 # works
v3.0.0.3215_2401262240 # bad
v3.0.0.3215_2401272069 # mine
v3.0.0.3215_2401272069 # latest
v3.0.0.4110_2410111120 # works poe
DB_566128M5MP_W_W
DB_566128M5MP_W_W
DB_566128M5MP_W_W

```

```yml
detect:
  width: 640
  height: 480
  fps: 5

ffmpeg:
  hwaccel_args: -hwaccel_output_format qsv -c:v h264_qsv
  output_args: # record audio
    record: -f segment -segment_time 10 -segment_format mp4 -reset_timestamps 1 -strftime 1 -c copy # -an

cameras:
  Balcony:
    ffmpeg:
      inputs:
        - path: rtsp://{FRIGATE_USER}:{FRIGATE_PASSWORD}@192.168.1.76:554//h264Preview_01_sub
          roles:
            - detect
        - path: rtsp://{FRIGATE_USER}:{FRIGATE_PASSWORD}@192.168.1.76:554
          roles:
            - record
```

```sh
ffprobe rtsp://admin:qS7kef9TzrBoQl4h@foodcam.local
ffprobe version n5.1-2-g915ef932a3-20220731 Copyright (c) 2007-2022 the FFmpeg developers
  built with gcc 12.1.0 (crosstool-NG 1.25.0.55_3defb7b)
  configuration: --prefix=/ffbuild/prefix --pkg-config-flags=--static --pkg-config=pkg-config --cross-prefix=x86_64-ffbuild-linux-gnu- --arch=x86_64 --target-os=linux --enable-gpl --enable-version3 --disable-debug --enable-iconv --enable-libxml2 --enable-zlib --enable-libfreetype --enable-libfribidi --enable-gmp --enable-lzma --enable-fontconfig --enable-libvorbis --enable-opencl --enable-libpulse --enable-libvmaf --enable-libxcb --enable-xlib --enable-amf --enable-libaom --enable-libaribb24 --enable-avisynth --enable-libdav1d --enable-libdavs2 --disable-libfdk-aac --enable-ffnvcodec --enable-cuda-llvm --enable-frei0r --enable-libgme --enable-libass --enable-libbluray --enable-libjxl --enable-libmp3lame --enable-libopus --enable-mbedtls --enable-librist --enable-libtheora --enable-libvpx --enable-libwebp --enable-lv2 --enable-libmfx --enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libopenh264 --enable-libopenjpeg --enable-libopenmpt --enable-librav1e --enable-librubberband --disable-schannel --enable-sdl2 --enable-libsoxr --enable-libsrt --enable-libsvtav1 --enable-libtwolame --enable-libuavs3d --enable-libdrm --enable-vaapi --enable-libvidstab --enable-vulkan --enable-libshaderc --enable-libplacebo --enable-libx264 --enable-libx265 --enable-libxavs2 --enable-libxvid --enable-libzimg --enable-libzvbi --extra-cflags=-DLIBTWOLAME_STATIC --extra-cxxflags= --extra-ldflags=-pthread --extra-ldexeflags=-pie --extra-libs='-ldl -lgomp' --extra-version=20220731
  libavutil      57. 28.100 / 57. 28.100
  libavcodec     59. 37.100 / 59. 37.100
  libavformat    59. 27.100 / 59. 27.100
  libavdevice    59.  7.100 / 59.  7.100
  libavfilter     8. 44.100 /  8. 44.100
  libswscale      6.  7.100 /  6.  7.100
  libswresample   4.  7.100 /  4.  7.100
  libpostproc    56.  6.100 / 56.  6.100
Input #0, rtsp, from 'rtsp://admin:qS7kef9TzrBoQl4h@foodcam.local':
  Metadata:
    title           : Session streamed by "preview"
  Duration: N/A, start: 0.000063, bitrate: N/A
  Stream #0:0: Video: h264 (High), yuv420p(progressive), 2560x1920, 30 fps, 30 tbr, 90k tbn
  Stream #0:1: Audio: aac (LC), 16000 Hz, mono, fltp
```

```sh
# A
      - ffmpeg:https://foodcam.local/flv?port=1935&app=bcs&stream=channel0_main.bcs&user=admin&password=qS7kef9TzrBoQl4h#video=copy#audio=copy#audio=opus
      - ffmpeg:food#audio=aac
# B
# sound still works lin live web preview
      - ffmpeg:https://foodcam.local/flv?port=1935&app=bcs&stream=channel0_main.bcs&user=admin&password=qS7kef9TzrBoQl4h#video=copy#audio=copy
# C
# sound still works in live web preview
# stream properties are basically identical to B
# sound not in recorded clips (not sure if it was there before or not)
      - ffmpeg:https://foodcam.local/flv?port=1935&app=bcs&stream=channel0_main.bcs&user=admin&password=qS7kef9TzrBoQl4h
# D
# same still no sound in the recordings
      - ffmpeg:https://foodcam.local/flv?port=1935&app=bcs&stream=channel0_main.bcs&user=admin&password=qS7kef9TzrBoQl4h#video=copy#audio=aac
# E
# recorded clips freeze
      - ffmpeg:https://foodcam.local/flv?port=1935&app=bcs&stream=channel0_main.bcs&user=admin&password=qS7kef9TzrBoQl4h
ffmpeg:
  output_args:
    record: preset-record-generic-audio-copy
# F
      - ffmpeg:https://foodcam.local/flv?port=1935&app=bcs&stream=channel0_main.bcs&user=admin&password=qS7kef9TzrBoQl4h
ffmpeg:
  output_args:
    record: preset-record-generic-audio-aac
```

#### PCIe Passthrough

<https://raw.githubusercontent.com/VincentSaelzler/hyper-homelab/main/docs/pcie-passthrough.md>

#### BIOS Configuration

* Update BIOS (from v1804 to v3205 to v3607)
* Reset All to Defaults
* Q-Fan Auto-Optimize
* Use 3200 MHz RAM Profile

## DNS API Credentials

Use porkbun.
