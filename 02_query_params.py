from fastapi import FastAPI
from typing import Optional

app = FastAPI()

# 查询参数：URL中?key=value的部分
@app.get("/items/")  # 装饰器
async def list_items(skip: int = 0, limit: int = 10):
    # 模拟数据
    # fake_items_db = []为列表推导式，生成100个模拟数据
    fake_items_db = [{"item_name": f"Item{i}"} for i in range(100)]
    # 列表切片：从skip开始，取limit个元素
    return fake_items_db[skip: skip + limit]

# 可选查询参数
@app.get("/users/{user_id}")
# 定义异步函数，user_id是路径参数，q是可选查询参数，默认值为None
async def get_user(user_id: int, q: Optional[str] = None):
    if q:
        return {"user_id": user_id, "query": q}
    return {"user_id": user_id}