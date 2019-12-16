import click

from hour_monitor.hour_monitor import HourMonitor


@click.command()
@click.option("--store_entry", is_flag=True, help="Store entry hour")
@click.option("--store_exit", is_flag=True, help="Store exit hour")
@click.option("--upd_entry", is_flag=True, help="Update entry hour")
@click.option("--upd_exit", is_flag=True, help="Update exit hour")
@click.option("--look_day", is_flag=True, help="Check amount of hours worked during a day")
@click.option("--look_week", is_flag=True, help="Check amount of hours worked during a week")
@click.option("--look_month", is_flag=True, help="Check amount of hours worked during a month")
@click.option("--rem_day", is_flag=True, help="Check amount of hours yet to be worked during a day")
@click.option("--rem_week", is_flag=True, help="Check amount of hours yet to be worked during a week")
@click.option("--del_day", is_flag=True, help="Delete info about a day")
@click.option("--day", type=str, help="Specify a day as dd/mm/yy")
@click.option("--hour", type=str, help="Specify an hour as hh:mm")
def main(store_entry, store_exit, upd_entry, upd_exit, look_day,
         look_week, look_month, rem_day, rem_week, del_day, day, hour):
    hour_monitor = HourMonitor()
    if store_entry:
        hour_monitor.store_entry_hour(day, hour)
    elif store_exit:
        hour_monitor.store_exit_hour(day, hour)
    elif upd_entry:
        hour_monitor.update_entry_hour(day, hour)
    elif upd_exit:
        hour_monitor.update_exit_hour(day, hour)
    elif look_day:
        entry_hour = hour_monitor.check_entry_hour(day)
        exit_hour = hour_monitor.check_exit_hour(day)
        daily_hours = hour_monitor.check_daily_hours(day)
        print("entry hour: ", entry_hour, " exit hour: ", exit_hour, " daily hours:", daily_hours)
    elif look_week:
        weekly_hours = hour_monitor.check_weekly_hours(day)
        print("weekly hours: ", weekly_hours)
    elif look_month:
        monthly_hours = hour_monitor.check_weekly_hours(day)
        print("monthly hours: ", monthly_hours)
    elif rem_day:
        remaining_hours = hour_monitor.check_remaining_daily_hours(day)
        print("remaining hours: ", remaining_hours)
    elif rem_week:
        remaining_hours = hour_monitor.check_remaining_weekly_hours(day)
        print("remaining hours: ", remaining_hours)
    elif del_day:
        hour_monitor.remove_day(day)
    else:
        print("Wrong option")


if __name__ == '__main__':
    main()
