from django.http import JsonResponse
import requests
import gspread
from django.http import HttpResponse
from google.oauth2.service_account import Credentials

def home(request):
    return HttpResponse("Welcome to the IndiaMart Leads Integration Project!")

def fetch_leads(request):
    # Define the scope for Google Sheets
    scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
    creds = Credentials.from_service_account_file(
        'E:\\Django API\\Django-API-for-india-mart\\indiamartproject\\horizontal-ally-424002-h0-5a2bc811e849.json', scopes=scope)
    client = gspread.authorize(creds)

    # Open the sheet
    sheet = client.open_by_url('https://docs.google.com/spreadsheets/d/187GiG-scUxIs8Tl8y0I9RbbAcA49vcRO9c1VySzYK0o/edit#gid=0')
    worksheet = sheet.sheet1

    # Fetching leads from IndiaMART API
    response = requests.get("https://mapi.indiamart.com/wservce/crm/crmListing/v2/?glusr_crm_key=mRyyF75q5XfJSveq4XGP7l6PoFfClThj")
    leads = response.json().get('RESPONSE')

    # Process and store leads in Google Sheet
    for lead in leads:
        worksheet.append_row([lead[field_name] for field_name in lead])  # Adjust field names as per your API response structure

    return JsonResponse({'message': 'Leads fetched and stored successfully'})
