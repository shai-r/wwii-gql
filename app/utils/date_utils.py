from datetime import date


def convert_string_to_date(date_str: str):
    date_arr = date_str.split('-')
    return date(
        year=int(date_arr[0]),
        month=int(date_arr[1]),
        day=int(date_arr[2])
    )

def is_date_in_date_range(date_to_check: str, start_date: str, end_date: str) -> bool:
    return (convert_string_to_date(date_to_check) > convert_string_to_date(start_date) and
            convert_string_to_date(date_to_check) < convert_string_to_date(end_date))