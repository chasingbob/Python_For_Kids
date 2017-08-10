import time
from notifier import Notifier

notifier = Notifier()

classes = [(8, 9, 'Afr'), (9, 11, 'Chemistry'), (10, 11, 'Eng'), (12, 13, 'Lunch')]

print(classes)


while True:
    for time_slot in range(24):
        print(time_slot)
        for time_slot_start, time_slot_end, class_name in classes:
            if time_slot_start == time_slot:
                #print('\t{} - Your {} class started lazy wtf'.format(time_slot_start, class_name))
                notifier.notify('Do somthing')
            
            if time_slot_end == time_slot:
                #print('\t{} - Your {} class is finished'.format(time_slot_end, class_name))
                notifier.notify('Do something else')
        
        time.sleep(1)
