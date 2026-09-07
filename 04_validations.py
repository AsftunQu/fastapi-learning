from fastapi import FastAPI, Query, Path  # Query查询参数， Path路径参数
from typing import Optional

app = FastAPI()

# 1.查询参数校验
@app.get("/items/")
async def read_items(
    # None表示可选参数，min_length最小长度，max_length最大长度，regex正则表达式
    q: Optional[str] = Query(None, min_length=3, max_length=50, regex="^fixedquery$"),
    # ge表示大于等于，le表示小于等于
    skip: int = Query(0, ge=0, le=100),
    limit: int = Query(10, ge=1, le=100)
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# 2.路径参数校验
@app.get("/items/{item_id}")
async def read_item(
    # 用Path函数包裹参数，...表示必填（因为路径参数必须是必填的）
    # 路径参数必须要用Path()而不是Query()，因为路径参数从URL中获取，查询参数从？后面获取
    item_id: int = Path(..., title="The ID of the item to get", ge=1, le=1000),
    q: Optional[str] = None
):
    return {"item_id": item_id, "q": q}

# 3.查询参数+路径参数混合校验
@app.get("/products/{product_id}")
async def read_product(
    # 路径参数
    product_id: int = Path(..., ge=1, description="Product ID must be >= 1"),
    # 查询参数，默认“asc”，必须是asc或desc
    sort: str = Query("asc", regex="^(asc|desc)$", description="Sort order:asc or desc"),
    # 查询参数
    page: int = Query(1, ge=1, le=100)
):
    return{
        "product_id": product_id,
        "sort": sort,
        "page": page
    }