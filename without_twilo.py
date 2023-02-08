import time
import gspread
import pywhatkit as pwk

gc = gspread.service_account(filename='credientials.json') #TODO:ADD_API_SERVICE_ACCOUNT_CREDIENTIALS
gsheet = gc.open_by_url("{SHEET_URL}") #TODO:ADD SHEET_URL
prev_list0 = gsheet.values_get("{COLUMN_INDEX}") #TODO:ADD_COLUMN_INDEXES(EXCEL FORMAT)
prev_list = []
i = 0

def send_wp_message(hour,minute):
    msg = "Yardım bölgelerindeki ihtiyaç durumunda değişiklik olmuştur bu linkten takip edebilirsiniz: " + gsheet.url
    try:
        pwk.sendwhatmsg_to_group("{WPGROUPID}", msg, hour, minute, 10, True, 2) #TODO:ADD_WP_GROUP_ID
        print("Mesaj gönderildi")  # Prints success message in console
        # error message
    except:
        print("Mesaj göndermede hata oluştu")

while True:
    cur_list = gsheet.values_get("{COLUMN_INDEX}") #TODO:ADD_COLUMN_INDEXES(EXCEL FORMAT)
    if i == 0:
        if cur_list == prev_list0:
            pass
        else:
            send_wp_message(time.localtime().tm_hour.real,(time.localtime().tm_min.real + 1))
            i += 1
            prev_list = cur_list
            time.sleep(60)
    else:
        if cur_list == prev_list:
            pass
        else:
            send_wp_message(time.localtime().tm_hour.real,(time.localtime().tm_min.real + 1))
            prev_list = cur_list
            time.sleep(60)

