from fastapi import FastAPI, Query, Path, Body  # FastAPI核心类，query查询参数，path路径参数，body控制请求体
from pydantic import BaseModel, Field  # 导入Pydantic用于定义数据模型，Field用于给请求体字段添加校验规则
from typing import Optional

app = FastAPI()  # 创建一个FastAPI应用实例

# ============================================
# 1. 请求体字段校验（用 Field）
# ============================================

# 定义Item模型
class Item(BaseModel):
    name: str = Field(..., title="Item name", min_length=2, max_length=50)
    description: Optional[str] = Field(None, max_length=300)
    price: float = Field(..., gt=0, description="Price must be greater than zero")
    tax: Optional[float] = Field(None, ge=0)

# POST创建商品
@app.post("/items/")
async def create_item(item: Item):
    return item

# ============================================
# 2. 请求体 + 路径参数 + 查询参数 混合
# ============================================

# PUT更新商品（混合参数）
@app.put("/items/{item_id}")
async def update_item(
    item_id: int = Path(..., ge=1, description="Item ID must be >= 1"),
    q: Optional[str] = Query(None, min_length=3, max_length=50),
    item: Item = Body(..., embed=True)
):
    return {"item_id": item_id, "q": q, "item": item}

# ============================================
# 3. 多个请求体参数 + 路径参数 + 查询参数
# ============================================

# 定义User模型
class User(BaseModel): 
    username: str = Field(..., min_length=3, max_length=20)
    full_name: Optional[str] = Field(None, max_length=50)
    age: int = Field(..., ge=18, le=120)

# 定义OrderItem模型
class OrderItem(BaseModel):
    product_name: str = Field(..., min_length=1, max_length=100)
    quantity: int = Field(..., ge=1, le=999)
    unit_price: float = Field(..., gt=0)

# 创建订单（多参数混合）
@app.post("/orders/{order_id}")
async def create_order(
    order_id: int = Path(..., ge=1, description="Order ID must be >= 1"),
    user: User = Body(...),
    items: list[OrderItem] = Body(...),
    discount: Optional[float] = Query(None, ge=0, le=1, description="Discount rate (0-1)")
):
    total = sum(item.quantity * item.unit_price for item in items)
    if discount:
        total = total * (1 - discount)
    
    return {
        "order_id": order_id,
        "user": user,
        "items": items,
        "discount": discount,
        "total": round(total, 2)
    }

# ============================================
# 4. 嵌套模型
# ============================================

class Address(BaseModel):
    street: str = Field(..., min_length=1, max_length=100)
    city: str = Field(..., min_length=1, max_length=50)
    zip_code: str = Field(..., pattern=r"^[0-9]{5,6}$")  # 改为 pattern，用原始字符串 r"..."

class Customer(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    email: str = Field(..., pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")  # 改为 pattern
    address: Address

@app.post("/customers/")
async def create_customer(customer: Customer):
    return customer