from datetime import datetime
import pytz

def convert_to_naive(localized_datetime):
    """
    Converts a timezone-aware datetime object to a naive datetime object (without timezone information).
    
    :param localized_datetime: The timezone-aware datetime object
    :return: The naive datetime object
    """
    # Convert to naive datetime by removing timezone information
    naive_datetime = localized_datetime.replace(tzinfo=None)
    return naive_datetime

def convert_to_timezone(date_str, input_format='%Y-%m-%d %H:%M:%S', target_timezone='Asia/Jakarta'):
    """
    Converts a datetime string to the specified timezone.
    
    :param date_str: The datetime string to convert (e.g., '2024-09-01 08:00:00')
    :param input_format: The format of the input datetime string (default: '%Y-%m-%d %H:%M:%S')
    :param target_timezone: The timezone to convert to (default: 'Asia/Jakarta')
    :return: The datetime object localized to the target timezone
    """
    
    # Parse the date string into a naive datetime object (without timezone)
    naive_datetime = datetime.strptime(date_str, input_format)
    
    # Define the target timezone
    target_tz = pytz.timezone(target_timezone)
    
    # Localize the naive datetime to the target timezone
    localized_datetime = target_tz.localize(naive_datetime)
    
    return localized_datetime

def convert_to_utc(localized_datetime):
    """
    Converts a timezone-aware datetime object to UTC.
    
    :param localized_datetime: The timezone-aware datetime object
    :return: The datetime object in UTC
    """
    
    # Convert to UTC
    utc_datetime = localized_datetime.astimezone(pytz.utc)
    
    return utc_datetime

def convert_date_local(raw_date):
    return convert_to_naive(convert_to_utc(convert_to_timezone(raw_date)))

def to_naive_utc(local_time_str, local_format='%Y-%m-%d %H:%M:%S', local_timezone='Asia/Jakarta'):
    """
    Convert local time string to naive UTC datetime.
    
    :param local_time_str: The local time string to convert (e.g., '2024-09-01 08:00:00') or datetime object
    :param local_format: The format of the local time string (default: '%Y-%m-%d %H:%M:%S')
    :param local_timezone: The timezone of the local time string (default: 'Asia/Jakarta')
    :return: Naive UTC datetime
    """
    if isinstance(local_time_str, str):
        # Parse the local datetime string to a naive datetime object
        naive_local_datetime = datetime.strptime(local_time_str, local_format)
    elif isinstance(local_time_str, datetime):
        # Assume the datetime object is naive local datetime
        naive_local_datetime = local_time_str
    else:
        raise ValueError("local_time_str must be a string or datetime object")

    # Localize the naive datetime to the given local timezone
    local_tz = pytz.timezone(local_timezone)
    aware_local_datetime = local_tz.localize(naive_local_datetime)
    
    # Convert to UTC
    utc_datetime = aware_local_datetime.astimezone(pytz.utc)
    
    # Convert to naive datetime by removing timezone information
    naive_utc_datetime = utc_datetime.replace(tzinfo=None)
    
    return naive_utc_datetime

def from_utc_to_local(naive_utc_datetime, target_timezone='Asia/Jakarta'):
    """
    Convert naive UTC datetime to local timezone-aware datetime.
    
    :param naive_utc_datetime: Naive UTC datetime object
    :param target_timezone: The local timezone to convert to (default: 'Asia/Jakarta')
    :return: Timezone-aware datetime in the target local timezone
    """
    # Ensure the naive datetime is treated as UTC
    utc_aware_datetime = pytz.utc.localize(naive_utc_datetime)
    
    # Convert to the target timezone
    local_tz = pytz.timezone(target_timezone)
    local_aware_datetime = utc_aware_datetime.astimezone(local_tz)
    
    return local_aware_datetime

def convert_date_local_back(raw_date, local_format='%Y-%m-%d %H:%M:%S', local_timezone='Asia/Jakarta', target_timezone='Asia/Jakarta', output_format='%y/%m/%d %H:%M:%S'):
    """
    Convert a raw date string or datetime object from a local timezone to a formatted local timezone-aware datetime string.
    
    :param raw_date: The date string to convert (e.g., '2024-09-01 08:00:00') or datetime object
    :param local_format: The format of the raw date string (default: '%Y-%m-%d %H:%M:%S')
    :param local_timezone: The timezone of the raw date string (default: 'Asia/Jakarta')
    :param target_timezone: The local timezone to convert to (default: 'Asia/Jakarta')
    :param output_format: The format for the output datetime string (default: '%y/%m/%d %H:%M:%S')
    :return: Formatted datetime string in the target local timezone
    """
    # Convert local date string or datetime object to naive UTC datetime
    naive_utc_datetime = to_naive_utc(raw_date, local_format, local_timezone)
    
    # Convert naive UTC datetime to local timezone-aware datetime
    local_aware_datetime = from_utc_to_local(naive_utc_datetime, target_timezone)
    
    # Convert the timezone-aware datetime to a string in the specified output format
    return local_aware_datetime.strftime(output_format)
