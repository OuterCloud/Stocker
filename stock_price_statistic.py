"""Stock price statistic

pip install stock-open-api
pip install environs
pip install loguru
"""
from loguru import logger
from stock_open_api.api.eastmoney.hk_stock import get_list

TARGETS = [
    "03690",  # 美团-W
    "00700",  # 腾讯控股
    "01810",  # 小米集团-W
    "09618",  # 京东集团-SW
    "09888",  # 百度集团-SW
]


def get_stock_prices(targets):
    """获取指定股票的价格信息"""

    data = get_list(page=1, size=5000).to_dict()

    items = data["items"]
    total = data["total"]

    logger.debug(f"港股总数: {total}")
    assert len(items) == total

    return {item["名称"]: item["最新价"] for item in items if item["代码"] in targets}


if __name__ == "__main__":
    stock_prices = get_stock_prices(TARGETS)
    logger.debug(stock_prices)
