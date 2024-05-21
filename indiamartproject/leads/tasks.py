from background_task import background
from .google_sheets import update_sheet
import requests

@background(schedule=5)  # Schedules the task to be run every 5 minutes
def fetch_and_update_data():
    url = "https://mapi.indiamart.com/wservce/crm/crmListing/v2/?glusr_crm_key=mRyyF7ll53vJTPeq43aK7lqKoVHHnzA="
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        leads = data.get('RESPONSE', [])
        
        if leads:
            # Assume the range starts from the second row to skip headers
            sheet_id = '187GiG-scUxIs8Tl8y0I9RbbAcA49vcRO9c1VySzYK0o'
            range_name = 'Sheet1!A2'  # Adjust based on your sheet configuration
            values = [list(lead.values()) for lead in leads]
            update_sheet(sheet_id, range_name, values)
