import gspread
from oauth2client.service_account import ServiceAccountCredentials

def authenticate_google_sheets():
    scope = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        'E:/Django API/Django-API-for-india-mart/indiamartproject/horizontal-ally-424002-h0-5a2bc811e849.json', scope)
    client = gspread.authorize(creds)
    return client

def update_sheet(sheet_id, range_name, values):
    client = authenticate_google_sheets()
    sheet = client.open_by_key(sheet_id).sheet1
    sheet.update(range_name, values)
