# set up flask Blueprint

from datetime import datetime
from datetime import timedelta
from time import sleep
import services.lightspeed.lightspeed_r.endpoints as endpoints

terminate = False
simulation_running = False

# Receve Data from Simulation Config Slack Modle
def get_day_simulation_config(view):
   
    time_span = view["time_span"]["time_span"]["value"]
    num_shifts = view["number_of_shifts"]["number_of_shifts"]["value"]
    num_total_sales = view["num_total_sales"]["num_total_sales"]["value"]
    num_ecom = view["number_ecom_orders"]["number_ecom_orders"]["value"]
    # print(store_open,store_close,num_shifts,total_sales,num_ecom)

    if not simulation_running:
        run_day_simulation(time_span, num_shifts, num_total_sales, num_ecom)
    else:
        print("Day Simulation is Already Running")
        return
    return




# start the day simlator
def run_day_simulation(time_span, num_shifts, num_total_sales, num_ecom):
    global terminate 
    global simulation_running
    simulation_running = True
    # terminate = False
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

 
    if simulation_running:
        for i in range(0, num_total_sales + 1):
            if not terminate:
                
                if i == 0:
                    print("***********************************************************")
                    print("*********************** Store Opens ***********************")
                    print("--------------------- Shift",1, "Starts -----------------")
                    # Open Register
                    endpoints.open_register()
                # print("--------------------------------------------------------------")
                print("Sale Number:",i)
                # Create Sale
                print("terminate:", terminate)
                endpoints.create_sale()
                sleep_time = int(delta_seconds/num_total_sales)
                for k in range(0,sleep_time):
                    if not terminate:
                        # print("waiting",k," sec....")
                        sleep(1)
                        
                    else:
                        endpoints.close_register()
                        print("Simulation Stopped")
                        terminate = False
                        simulation_running = False
                        return

                shift_num = round(i/x)
                if i >= round(q):
                    q = q + p
                    print("eCom Order", round((q/p)-1), "xxxxxxxxx")
                    # Create eCom Sale
                    print("terminate:", terminate)
                    endpoints.create_ecom_sale()

                if i >= round(y):
                    y = y + x
                    print("Shift", shift_num , "Ends --------")
                    # Close Register
                    print("terminate:", terminate)
                    endpoints.close_register()

                    if i == num_total_sales:
                        pass
                        print("********************** End of Day! **********************")
                        print("*********************************************************")
                    else:
                        print("Shift", shift_num +1 ,"Starts vvvvvvv")
                        # Open Register
                        print("terminate:", terminate)
                        endpoints.open_register()
            
            else:
                endpoints.close_register()
                print("Simulation Stopped")
                terminate = False
                simulation_running = False
                break

    return
   
    

def stop_day_sim():
    global terminate

    if simulation_running:
        terminate = True
        print("Stopping Day Simulation")
    else:
        print("Day Simulation is not Running")
        return
    return
   
    
