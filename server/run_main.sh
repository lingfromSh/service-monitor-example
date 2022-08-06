#!/bin/sh
###
 # @Author: shiyun.ling shiyun.ling@flexiv.com
 # @Date: 2022-08-05 17:21:32
 # @LastEditors: shiyun.ling
 # @LastEditTime: 2022-08-06 14:56:04
 # @Description: file content
### 

uvicorn --host 0.0.0.0 --port 8080 --access-log --log-level info main:app