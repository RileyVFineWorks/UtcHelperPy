from datetime import datetime
import pytz

def convert_timestamp_to_pst(timestamp):
    dt = datetime.fromisoformat(timestamp)

    dt_utc = dt.replace(tzinfo=pytz.UTC)

    pst_tz = pytz.timezone('US/Pacific')
    dt_pst = dt_utc.astimezone(pst_tz)

    readable_time = dt_pst.strftime("%B %d, %Y at %I:%M:%S %p %Z")
    return readable_time

def main():
    user_timestamp = input("enter utc (format: YYYY-MM-DDTHH:MM:SS.ssssss+00:00): ")

    try:
        pst_time = convert_timestamp_to_pst(user_timestamp)
        print(f"Converted time: {pst_time}")
    except ValueError:
        print("Invalid UTC")

if __name__ == "__main__":
    main()
