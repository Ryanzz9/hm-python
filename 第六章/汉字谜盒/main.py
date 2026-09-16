from fastapi import FastAPI
from starlette.responses import FileResponse
from fastapi.staticfiles import StaticFiles

# 创建FastAPI应用
app = FastAPI(title="汉字谜盒")

# 挂载静态文件目录
app.mount("/static", StaticFiles(directory="static"), name="static")



# 定义根路径操作
@app.get("/")
def root():
    print("访问项目首页")
    return FileResponse("static/index.html")




# 运行应用
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)
