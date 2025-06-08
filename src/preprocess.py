import os
import pandas as pd
from tlops_tools.tools.Preprocess import (
    preprocess_signal_data,
    preprocess_demand_data,
)


def main() -> None:
    """Merge raw CSV files and run basic preprocessing."""

    # 1) 입력 경로 설정
    RAW_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "raw")
    SIGNAL_CSV = os.path.join(RAW_DIR, "signals", "20220810", "merged_s.csv")
    OD_CSV = os.path.join(RAW_DIR, "90001220220810050000od.csv")

    # (선행) signals/*.csv 병합: 한번만 실행
    if not os.path.exists(SIGNAL_CSV):
        files = [
            os.path.join(RAW_DIR, "signals", "20220810", f)
            for f in os.listdir(os.path.join(RAW_DIR, "signals", "20220810"))
            if f.endswith(".csv")
        ]
        df_s = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)
        df_s.to_csv(SIGNAL_CSV, index=False)

    # 2) 전처리
    # analysis_start: od 파일명 기준시각(예: 2022-08-10 05:00:00)
    ANALYSIS_START = "2022-08-10 05:00:00"

    signal_df = preprocess_signal_data(SIGNAL_CSV)
    demand_df = preprocess_demand_data(OD_CSV, ANALYSIS_START)

    # 3) 결과 저장
    OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "processed")
    os.makedirs(OUT_DIR, exist_ok=True)

    signal_df.to_csv(os.path.join(OUT_DIR, "s_preprocessed.csv"), index=False)
    demand_df.to_csv(os.path.join(OUT_DIR, "od_preprocessed.csv"), index=False)

    print("✔ 전처리 완료!")
    print(f" • 신호 데이터 → {OUT_DIR}/s_preprocessed.csv")
    print(f" • 교통량 데이터 → {OUT_DIR}/od_preprocessed.csv")


if __name__ == "__main__":
    main()
