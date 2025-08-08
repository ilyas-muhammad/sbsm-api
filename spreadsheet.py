import gspread 

gc = gspread.service_account(filename='service_account.json')

def get_sheet():
    return gc.open_by_url("https://docs.google.com/spreadsheets/d/1MRD3tMN9yByZkSp90019aPNll_lMZiKr7oLmMt8yNtI/edit?gid=0#gid=0").worksheet("Measurements")

def get_all_records():
    return get_sheet().get_all_records()

def append_row(row: list[any] = []):
    return get_sheet().append_row(row)
