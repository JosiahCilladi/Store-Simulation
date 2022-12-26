# set up flask Blueprint

from datetime import datetime
from datetime import timedelta
from time import sleep


# Receve Data from Simulation Config Slack Modle
def get_day_simulation_config(view):
    # print(json.dumps(view, indent =1))
   
    time_span = view["time_span"]["time_span"]["value"]
    num_shifts = view["number_of_shifts"]["number_of_shifts"]["value"]
    items_sold = view["items_sold"]["items_sold"]["value"]
    num_ecom = view["number_ecom_orders"]["number_ecom_orders"]["value"]
    # print(store_open,store_close,num_shifts,total_sales,num_ecom)
    start_day_simulation(time_span, num_shifts, items_sold, num_ecom)

    
def start_day_simulation(time_span, num_shifts, items_sold, num_ecom):
    print(time_span, num_shifts, items_sold, num_ecom)
    items_sold = int(items_sold)
    num_shifts = int(num_shifts)
    num_ecom = int(num_ecom)
    # Add tiem_span to current time

    today = datetime.now()
    delta_seconds = (float(time_span) * 60)*60
    print("delta", delta_seconds)
    time_span_end = today + timedelta(minutes=delta_seconds)
    print("time_span_end", time_span_end)

    x = items_sold/num_shifts
    print("shift duration by Items sold.", x)
    y = x

    p = round(items_sold/num_ecom)
    q = p



    for i in range(0,items_sold + 1):
        if i == 1:
            print("Store Opens, Shift",1, "Starts")

        print("sold Item",i)
        sleep(delta_seconds/items_sold)

      
        shift_num = round(i/x)
        print("shift_num", shift_num)

        if i >= round(q):
            q = q + p
            print("eCom Order", round((q/p)-1), "xxxxxxxxx")



        # print("y", y)
        if i >= round(y):
            
            y = y + x
            
            print("Shift", shift_num , "Ends --------")

            if i == items_sold:
                pass
                print("End of Day!")
            else:
                print("Shift", shift_num +1 ,"Starts vvvvvvv")
            
        

    pass
   
    

    
   
    
