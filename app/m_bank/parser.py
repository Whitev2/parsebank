import httpx
import bs4
from bs4 import BeautifulSoup

last_table = ""
data_list = []


async def parser(html_content):
    global last_table
    global data_list

    if html_content == last_table:
        print("No new data found")
        return

    last_table = html_content




    # Parse the HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the table body
    table_body = soup.find('tbody')

    # Initialize a list to store each row's data
    data = []

    # Iterate over each row in the table body
    for row in table_body.find_all('tr'):
        # Initialize a dictionary to store the data of the current row
        row_data = {
            "Date": row.find_all('td')[0].get_text(strip=True),
            "Particulars": row.find_all('td')[1].get_text(strip=True),
            "Cheque/Reference No": row.find_all('td')[2].get_text(strip=True),
            "Debit": row.find_all('td')[3].get_text(strip=True),
            "Credit": row.find_all('td')[4].get_text(strip=True),
            "Balance": row.find_all('td')[5].get_text(strip=True),
            "Channel": row.find_all('td')[6].get_text(strip=True)
        }

        # Append the current row's data to the list
        if row_data not in data_list:
            data.append(row_data)
            data_list.append(row_data)

    # Output the extracted data
    for i in data:
        await send_telegram_message(str(i))


async def send_telegram_message(message: str):
    url = f"https://api.telegram.org/bot6627443225:AAFL9NP8Tgck9-6nExc_oqy9QmgMdUeK2m0/sendMessage"
    chat_id = 2036190335

    async with httpx.AsyncClient() as client:
        data = {"chat_id": chat_id, "text": message}
        await client.post(url, data=data)