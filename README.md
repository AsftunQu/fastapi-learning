![Python Version](https://img.shields.io/badge/python-3.11%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

---

## 学习内容

| 章节 | 文件 | 核心知识点 |
|:---|:---|:---|
| 第1章 | `01_path_params.py` | 路径参数、枚举类型 |
| 第2章 | `02_query_params.py` | 查询参数、可选参数 |
| 第3章 | `03_request_body.py` | 请求体、Pydantic 模型 |
| 第4章 | `04_validations.py` | 查询参数和路径参数校验 |
| 第5章 | `05_request_body_validations.py` | 请求体校验、嵌套模型、混合参数 |

---

## 技术栈

- **框架**：FastAPI
- **服务器**：Uvicorn
- **数据校验**：Pydantic
- **数据库**：PostgreSQL（Docker）
- **版本控制**：Git & GitHub

---

## 上手须知

- 1.弄懂什么时候用POST、GET、PUT和DELETE
本质上就是增删改查，POST相当于增，GET相当于查，PUT相当于改

- 2.弄明白各个类如何使用，例如Path、Query、Body、Field和Optional
Path从URL路径中取值，来源于URL路径
Query从URL中的?后面取值，来源于URL参数
Body从HTTP请求体中取值，来源于JSON数据
Filed用于定义模型中的字段校验，来源于模型内部
Optional表示字段可以是None，来源于类型注解

##### 记忆口诀：路径用Path，问号用Query，JSON用Body，模型字段用Field

---

## 完整决策流程图

你要做什么？
    │
    ├─ 只查询数据，不修改 → GET
    │   ├─ 需要从 URL 中取 ID → Path
    │   ├─ 需要过滤/分页 → Query
    │   └─ 不需要请求体
    │
    ├─ 创建新数据 → POST
    │   ├─ 数据放哪里 → Body
    │   ├─ 字段校验 → Field
    │   ├─ 可选字段 → Optional
    │   └─ 路径参数 → 看情况（如 POST /users/{group_id}）
    │
    ├─ 更新已有数据 → PUT
    │   ├─ 从 URL 取 ID → Path（必填）
    │   ├─ 新数据放哪里 → Body
    │   ├─ 字段校验 → Field
    │   └─ 可选字段 → Optional
    │
    └─ 删除数据 → DELETE
        └─ 从 URL 取 ID → Path（必填）