<!--
 * @Author: shiyun.ling shiyun.ling@flexiv.com
 * @Date: 2022-08-05 17:03:00
 * @LastEditors: shiyun.ling
 * @LastEditTime: 2022-08-06 16:25:17
 * @Description: file content
-->
# Service monitor example

## Pre-requisites

- tilt >= 0.30.5
- k3d >= v5.4.3

## Quick Start

1. Start a cluster 
```shell
k3d cluster create--port 80:80 --registry-create local-registry:0.0.0.0:5678
```

2. Run tilt
```shell
tilt up
```