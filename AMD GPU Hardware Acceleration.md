# AMD GPU Hardware Acceleration

## ⚠️ Bottom Line ⚠️

```sh
# pass these through
/dev/dri/renderD128
/dev/kfd
```

```sh
# set this env var
HSA_OVERRIDE_GFX_VERSION=10.3.0 # i.e. gfx1030
```

## Sample Working Passthrough

See the `frigginpve` branch. That left frigate with a working config where the GPU handled both video decode and object detection.

However, power usage was high and performance was bad. It seems they are still ironing out the kinks as of 2025-02-25.

## References and Stuff About My Card

this set of links always seems hard to find.

* https://github.com/ollama/ollama/blob/main/docs/gpu.md#overrides-on-linux
* https://docs.frigate.video/configuration/object_detectors#docker-settings-for-overriding-the-gpu-chipset
* https://rocm.docs.amd.com/en/latest/reference/gpu-arch-specs.html
* https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html

```sh
lspci -v -s 0a:00.0
Sapphire Technology Limited Sapphire Radeon RX 6700
Navi 2x "Big Navi"
Video Core Next (VCN) 3.0
RDNA 2
Added Resizable BAR functionality
21Q2
VRAM 10 GiB

# "LLVM target name" of gfx1031
Radeon RX 6700
Radeon RX 6700 XT
Radeon RX 6750 XT

# "LLVM target" of gfx1030
Radeon RX 6800
Radeon RX 6800 XT
Radeon RX 6900 XT
Radeon RX 6950 XT

# "LLVM target" of gfx1030 and are officially supported ROCm
Radeon PRO W6800
Radeon PRO V620
```
