from fastapi import FastAPI  # 导入FastAPI

app = FastAPI()  # 创建应用实例

# 基础路径参数
@app.get("/items/{item_id}")  # 装饰器，当用户访问/items/xxx时，执行下面函数
async def read_item(item_id: int):  # 定义异步函数，FastAPI会把URL中捕获的值转换成整数，不是数字则报错
    return {"item_id":item_id, "name":f"Item{item_id}"}  # 返回字典

# 带枚举的路径参数
from enum import Enum  # 导入枚举类

class ModelName(str,Enum):  # 定义枚举类，继承自str和Enum
    alexnet = "alexnet"  # 枚举成员与值，用户访问不是其三之一则会返回422错误
    resnet = "resnet"
    lenet = "lenet"

# 带枚举的路径参数接口
@app.get("/models/{model_name}")  # 装饰器，访问/models/xxx时，执行下面函数
async def get_model(model_name:ModelName):  # 定义异步函数
    if model_name is ModelName.alexnet:  # 判断枚举成员并给出对应回答
        return {"model_name":model_name, "message":"Deep Learning FTW!"}
    if model_name.value == "lenet":
        return {"model_name":model_name, "message":"LeCNN all the images"}
    return {"model_name":model_name, "message":"Have some residuals"}

# 路径参数和查询参数混合
@app.get("/files/{file_path:path}")  # :path是特殊语法，告诉FastAPI这个参数可以匹配包含斜杠的路径
async def read_file(file_path:str):  # 类型是字符串，接收完整的文件路径
    return {"file_path":file_path}  # 返回捕获到的路径