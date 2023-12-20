"""根据股数和股价计算 futu 交易费用"""
import argparse
import math
from typing import Union

from loguru import logger

# pylint:disable=C2401:non-ascii-name


class Futu:
    """富途封装类"""

    def __init__(self) -> None:
        pass

    @staticmethod
    def calc_trade_pay(stock_count: int, price: Union[int, float]) -> float:
        """计算交易费用

        Args:
            stock_count (int): 股数.
            price (Union[int, float]): 股价.

        Returns:
            float: 交易费用
        """
        佣金 = (
            price * stock_count * 0.03 * 0.01
            if price * stock_count * 0.03 * 0.01 >= 3
            else 3
        )
        平台使用费 = 15
        交收费 = (
            0.002 * 0.01 * stock_count * price
            if 0.002 * 0.01 * stock_count * price >= 2
            else 2
        )
        交收费 = 交收费 if 交收费 <= 100 else 100
        印花税 = math.ceil(0.13 * 0.01 * price * stock_count)
        交易费 = (
            0.00565 * 0.01 * price * stock_count
            if 0.00565 * 0.01 * price * stock_count >= 0.01
            else 0.01
        )
        证监会交易征费 = (
            0.0027 * 0.01 * price * stock_count
            if 0.0027 * 0.01 * price * stock_count >= 0.01
            else 0.01
        )
        财务汇报局交易征费 = 0.00015 * 0.01 * price * stock_count
        交易费用 = 佣金 + 平台使用费 + 交收费 + 印花税 + 交易费 + 证监会交易征费 + 财务汇报局交易征费
        交易费用 = math.ceil(交易费用 * 100) / 100
        logger.warning(f"共需缴纳: {交易费用} 港币")
        return 交易费用


# 测试数据
# python futu.py 100 332 —— 73.79
# python futu.py 400 330 —— 240.46
if __name__ == "__main__":
    # 创建参数解析器
    parser = argparse.ArgumentParser(description="根据股数和股价计算交易费用")

    # 添加参数
    parser.add_argument("stock_count", type=int, help="股数")
    parser.add_argument("price", type=float, help="股价")

    # 解析命令行参数
    args = parser.parse_args()

    # 计算交易费用
    Futu.calc_trade_pay(stock_count=args.stock_count, price=args.price)
