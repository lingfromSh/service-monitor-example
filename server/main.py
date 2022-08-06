'''
Author: shiyun.ling shiyun.ling@flexiv.com
Date: 2022-08-05 17:08:55
LastEditors: shiyun.ling
LastEditTime: 2022-08-05 17:20:40
Description: file content
'''
from fastapi import FastAPI
from fastapi.responses import Response

app = FastAPI()


@app.get("/200")
async def return200():
    return Response(content="OK")


@app.post("/400")
async def return400():
    return Response(content="Bad Request", status_code=400)


@app.get("/404")
async def return404():
    return Response(content="Not Found", status_code=404)


@app.get("/500")
async def return500():
    return Response(content="Internal Server Error", status_code=500)
