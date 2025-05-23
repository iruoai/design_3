import requests
import time
import json

url = "https://jwxt.cqut.edu.cn/jwglxt/design/funcData_cxFuncDataList.html?xqmeKlxm=0BubqMAlqWmnEv9DBiuudI.FFzHi53WJK_PTxi4dNOR38cEOzSbXVahC7x.O6p7.rYyBkuESbfbrRIB7hI3lw56YL3ZGnxwKCfa0abHd.ukp7wtC5gXgCcikcUD3NyMjlxBk_Vx9fN5OsLqLGmHkjHIbuzysYt5FEUgIgngqm1MvQm42hgKyvPGFrcrZhi8JObohPhWf33U0"
headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    "Referer": "https://jwxt.cqut.edu.cn/jwglxt/design/viewFunc_cxDesignFuncPageIndex.html?gnmkdm=N219904&layout=default",
    "Cookie":   "JSESSIONID=1EECA05B46BA3E3C21260289EB519043; route=33ef780ed4561e995513ab3b8e56c88a; ZXniXLfxkjSbO=60Cjy_cFIhsNnGAX2Yq7NtoLScFT.Z_Fi4hzRNs7hPXHL4KmJpWbSiOdbPAnO38BitYNmGrCb4lURjR8wW03uFYq; ZXniXLfxkjSbP=08YB14g0Dej4URyRmAwYUjpVjN3inlAr4AOmAgGMmtZkSjkCoYqqOGxDJyqwzooutI_ml_FAM5cSgzHdKid7bYqb8OoVc._2jiTgoGKWkZIn5kZpb1fmUsGugGF6r6cteZVxdTBDHv7cdKT2bV9uq8FlI2CwLoc3RVzZdYdlohjK6Z1zpHyYTQJdU68i4f0empmIDKxBMYPHYx3yrAsLHmQcltqXz5_5nQb4uKsv6qppvlgQN1pYBCr9OeDePJ6SKueYw92oI.WuCABucEhz0y_e9fpjrz5aA7ss4vj8_nn3_.ifT5Rpi6M6cCqc5FNX4Myq0Oz7WkH97Bz3gsysxg6lG6sZnO3hdKl8cm.IKXcAwq0JSxmqoFdP6.DjCin4bW6rQwBkNe.nxXBIXrGEmUzyDd4ovl8UJvdBKjsybOVw0Vcfiwi20KzvI9WQknYmQ_fZpLOI_BYrNeSVoeDY..a",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
}

form_data = {
    "xnm": "2024",
    "xqm": "12",
    "nd": str(int(time.time() * 1000)),
    "queryModel.showCount": "500",
    "queryModel.currentPage": "1",
    "queryModel.sortOrder": "asc"
}

try:
    # 发送请求
    response = requests.post(url, headers=headers, data=form_data, timeout=10)
    response.raise_for_status()

    # 解析JSON数据
    result = response.json()

    # 提取Items数组
    items_data = result.get('items', [])

    if not items_data:
        print("警告：响应中未找到Items数据")
    else:
        # 保存Items数据到文件
        with open("items_data.json", "w", encoding="utf-8") as f:
            json.dump(items_data, f, ensure_ascii=False, indent=2)

        print(f"成功提取并保存{len(items_data)}条数据到items_data.json")

except requests.exceptions.RequestException as e:
    print(f"网络请求失败: {str(e)}")