import requests
import json
import re
import pandas as pd
from datetime import datetime


URL = "https://first-am.ru/individuals/fund/opif-obligatsiy-fond-ros-obligatsiy"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

OUTPUT = "fund214.csv"


def main():

    print("Загрузка данных First AM...")

    response = requests.get(
        URL,
        headers=HEADERS,
        timeout=30
    )

    response.raise_for_status()

    html = response.text


    match = re.search(
        r"chart-fund-data='(.*?)'",
        html,
        re.DOTALL
    )


    if not match:
        raise Exception(
            "Не найден chart-fund-data. Возможно, сайт изменил код."
        )


    data = json.loads(match.group(1))


    history = data["chartData"]


    df = pd.DataFrame(history)


    df = df[
        [
            "dateFormat",
            "originalPrice",
            "net_assets"
        ]
    ]


    df.columns = [
        "Date",
        "Price",
        "NAV"
    ]


    df.to_csv(
        OUTPUT,
        index=False,
        encoding="utf-8-sig"
    )


    print()
    print("Готово!")
    print("Файл:", OUTPUT)
    print("Время обновления:",
          datetime.now().strftime("%d.%m.%Y %H:%M"))

    print()
    print(df.tail())


if __name__ == "__main__":
    main()