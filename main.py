from fastapi import FastAPI
from typing import Optional

app = FastAPI(
    title="FundGPT API",
    version="1.1.0",
    description="FundGPT Real-Time Fund Query API"
)

@app.get("/")
def root():
    return {
        "name": "FundGPT API",
        "version": "1.1.0",
        "status": "running"
    }


@app.get("/fund/{code}")
def fund(code: str):
    """
    查询基金（目前为测试版）
    """

    return {
        "success": True,
        "fund_code": code,
        "fund_name": "待接入基金数据库",
        "fund_type": "Unknown",
        "latest_nav": None,
        "estimated_nav": None,
        "estimated_change": None,
        "update_time": None
    }


@app.get("/search")
def search(keyword: str):
    """
    按基金名称搜索（下一步接数据库）
    """

    return {
        "keyword": keyword,
        "result": [],
        "message": "Search API Ready"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }
