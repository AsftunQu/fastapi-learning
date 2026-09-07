from fastapi import FastAPI
from pydantic import BaseModel  # 导入Pydantic的基类，用于定义数据模型
from typing import Optional

app = FastAPI()

# 用Pydantic定义数据模型（相当于定于数据结构）
class Item(BaseModel):  # 定义一个数据模型，继承BaseModel
    name: str  # 必填字段，类型必须是字符串
    description: Optional[str] = None  # 可选字段，类型是字符串，默认值为None
    price: float  # 必填字段，类型必须是浮点数
    tax: Optional[float] = None  # 可选字段，类型是浮点数，默认值为None

# 请求体：接收JSON数据，自动校验并转换成item对象
@app.post("/items/")  # POST请求，用于创建数据（不是GET）
async def create_item(item: Item):  # 参数类型是Item模型，FastAPI自动解析
    # item现在是一个Item对象，可以直接使用
    item_dict = item.dict() # Pydantic方法，将模型对象转为PYthon字典
    if item.tax:  # 如果有tax字段
        price_with_tax = item.price + item.tax  # 计算原价+税
        item_dict.update({"price_with_tax": price_with_tax}) # 更新字典
    return item_dict  # 返回字典，自动转成JSON

# 路径参数 + 请求体混合使用
@app.put("/items/{item_id}")  # PUT请求，用于更新数据
async def update_item(item_id: int, item: Item):
    return {"item_id":item_id, **item.dict()}  # Python解包语法，把字典拆成键值对

# 多个请求体参数
class User(BaseModel):  # 定义User数据模型
    username: str
    full_name: Optional[str] = None

@app.post("/create-order/")
async def create_order(item: Item, user: User):
    return {
        "item": item.dict(),
        "user": user.dict(),
        "message": f"Order created for {user.username}"
    }