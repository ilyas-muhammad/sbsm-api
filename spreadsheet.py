from dotenv import load_dotenv
import gspread
import os
from model import Measurement

load_dotenv()

gc = gspread.service_account_from_dict({
    "type": "service_account",
    "project_id": "antireddots",
    "private_key_id": os.getenv('PRIVATE_KEY_ID'),
    "private_key": os.getenv('PRIVATE_KEY'),
    "client_email": os.getenv('CLIENT_EMAIL'),
    "client_id": os.getenv('CLIENT_ID'),
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/gsheet%40antireddots.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
})

def get_sheet():
    return gc.open_by_url("https://docs.google.com/spreadsheets/d/1MRD3tMN9yByZkSp90019aPNll_lMZiKr7oLmMt8yNtI/edit?gid=0#gid=0").worksheet("Measurements")

def get_all_records():
    return get_sheet().get_all_records()

def append_row(measurement: Measurement):
    row = [
        measurement.user_profile.get('timestamp'),
        measurement.user_profile.get('user_id'),
        measurement.user_profile.get('user_height'),
        measurement.user_profile.get('user_weight'),
        measurement.measurement.get('type'),
        measurement.measurement.get('value'),
        measurement.measurement.get('confidence_score'),
        measurement.measurement.get('confidence_percentage'),
        measurement.measurement.get('confidence_label'),
        measurement.measurement.get('source'),
        measurement.measurement.get('method'),
        measurement.measurement.get('unit'),
    ]
    return get_sheet().append_row(row)
