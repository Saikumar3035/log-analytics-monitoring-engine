import time
from backend.config.dask_config import start_dask
from backend.pipeline.processing import build_pipeline
from backend.anomaly.detection import detect_anamoly
from backend.config.email_alert import send_anomaly_email

def main():
    client = start_dask()
    print(client)
    print(f"Dashboard link: {client.dashboard_link}")
    print("\n" + "=" * 50)
    start = time.time()
    # Build log processing pipeline
    log_df = build_pipeline(r"D:\log-analytics-monitoring-engine\backend\sample_log\data_log.log")
    print("Parsed Log Data (Table Format):")
    print(log_df.compute())
    # Correct way to count rows
    total_logs = log_df.shape[0].compute()
    end = time.time()
    print("Total logs parsed:", total_logs)
    print("Time taken:", round(end - start, 2), "seconds")
    print("\nRunning anomaly detection...")
    # Detect anomalies
    anomalies = detect_anamoly(log_df)
    # If still a Dask dataframe convert to pandas
    if hasattr(anomalies, "compute"):
        anomalies = anomalies.compute()
    if anomalies.empty:
        print("No anomalies detected")
    else:
        print(f"🚨 {len(anomalies)} anomalies detected!")
        
        for minute, row in anomalies.iterrows():
            anomaly_data = {
                "timestamp": minute,
    "error_count": row.get("error_count", 0),
    "z_score": row.get("z_score", 0)
            }
            send_anomaly_email(
sender_email="saipatelmudam@gmail.com",
password="lgxu zsds fgdq pgzx",
 to_email="jangilisrividya@gmail.com",
anomaly=anomaly_data
    )

            print(
                f"Alert | Time: {minute} | "
                f"Errors: {row.get('error_count')}"
            )

    input("\nPress Enter to exit...")


if __name__ == "__main__":
    main()