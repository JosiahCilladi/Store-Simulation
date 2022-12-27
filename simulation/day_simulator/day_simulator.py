# set up flask Blueprint

from datetime import datetime
from datetime import timedelta
from time import sleep
import day_simulator.endpoints as endpoints

# Receve Data from Simulation Config Slack Modle
def get_day_simulation_config(view):
   
    time_span = view["time_span"]["time_span"]["value"]
    num_shifts = view["number_of_shifts"]["number_of_shifts"]["value"]
    num_total_sales = view["num_total_sales"]["num_total_sales"]["value"]
    num_ecom = view["number_ecom_orders"]["number_ecom_orders"]["value"]
    # print(store_open,store_close,num_shifts,total_sales,num_ecom)
    start_day_simulation(time_span, num_shifts, num_total_sales, num_ecom)
    return
    

# start the day simlator
def start_day_simulation(time_span, num_shifts, num_total_sales, num_ecom):
    print(time_span, num_shifts, num_total_sales, num_ecom)
    num_total_sales = int(num_total_sales)
    num_shifts = int(num_shifts)
    num_ecom = int(num_ecom)
    # Add tiem_span to current time

    today = datetime.now()
    delta_seconds = (float(time_span) * 60)*60
    print("delta", delta_seconds)
    time_span_end = today + timedelta(minutes=delta_seconds)
    print("time_span_end", time_span_end)

    x = num_total_sales/num_shifts
    print("shift duration by Items sold.", x)
    y = x
    p = round(num_total_sales/num_ecom)
    q = p
    for i in range(0, num_total_sales + 1):
        if i == 1:
            print("Store Opens, Shift",1, "Starts *******************")
            # Open Register
            endpoints.open_register()

        print("sale num",i)
        # Create Sale
        endpoints.create_sale()

        sleep(delta_seconds/num_total_sales)
        shift_num = round(i/x)
        if i >= round(q):
            q = q + p
            print("eCom Order", round((q/p)-1), "xxxxxxxxx")
            # Create eCom Sale
            endpoints.create_ecom_sale()

        if i >= round(y):
            y = y + x
            print("Shift", shift_num , "Ends --------")
            # Close Register
            endpoints.close_register()

            if i == num_total_sales:
                pass
                print("End of Day! **********************")
            else:
                print("Shift", shift_num +1 ,"Starts vvvvvvv")
                # Open Register
                endpoints.open_register()
        

    return
   
    

    
   
    
