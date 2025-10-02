import re
import pandas as pd

def preprocess(data):
    # Regex for [dd/mm/yy, h:mm:ss AM/PM]
    pattern = r'\[\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}:\d{2}\s?(?:AM|PM|am|pm)\]'

    # Split messages and extract dates
    messages = re.split(pattern, data)[1:]
    dates = re.findall(pattern, data)

    # Clean [] from dates
    dates = [d.strip("[]") for d in dates]

    # Create dataframe
    df = pd.DataFrame({'user_message': messages, 'message_date': dates})

    # Convert to datetime (12-hour clock with seconds + AM/PM)
    df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%y, %I:%M:%S %p')

    df.rename(columns={'message_date': 'date'}, inplace=True)

    # Extract users and messages
    users, cleaned_messages = [], []
    for message in df['user_message']:
        entry = re.split('([\w\W]+?):\s', message)
        if entry[1:]:
            users.append(entry[1])
            cleaned_messages.append(" ".join(entry[2:]))
        else:
            users.append('group_notification')
            cleaned_messages.append(entry[0])

    df['user'] = users
    df['message'] = cleaned_messages
    df.drop(columns=['user_message'], inplace=True)

    # Extra columns
    df['only_date'] = df['date'].dt.date
    df['year'] = df['date'].dt.year
    df['month_num'] = df['date'].dt.month
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute

    # Period column (hour ranges)
    period = []
    for hour in df['hour']:
        if hour == 23:
            period.append(f"{hour}-00")
        elif hour == 0:
            period.append("00-1")
        else:
            period.append(f"{hour}-{hour+1}")
    df['period'] = period

    return df
