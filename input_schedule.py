def input_daily_schedule():
    f = open('daily_schedule.txt', 'w')
    while 1:
        schedule = input('Write the schedule >> ')
        f.write(schedule)
        check = input('Do you want to write another schedule?(Write y or n) >> ')
        if check == 'n':
            break
    f.close
def input_fixed_schedule():
    f = open('fixed_schedule.txt', 'w')
    while 1:
        schedule = input('Write the schedule >> ')
        f.write(schedule)
        check = input('Do you want to write another schedule?(Write y or n) >> ')
        if check == 'n':
            break
    f.close

def main():
    print('=========================')
    print("Welcome to Duke's scheduler")
    print('=========================')
    schedule_type = int(input('Select type of schedule!(1 : daily, 2 : fixed) >> '))
    if schedule_type == 1:
        input_daily_schedule()
    else:
        input_fixed_schedule()

if __name__ == '__main__':
    main()