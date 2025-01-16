from tkinter import Tk, Label
from datetime import datetime
import time

def read_events():
    events = []
    with open('Countmeout.txt') as file:
        for line in file:
            event, date_str = line.strip().split(',')
            date = datetime.strptime(date_str, '%d/%m/%y')
            events.append((event, date))
    return events

def countdown(event_date):
    now = datetime.now()
    remaining_time = event_date - now
    return remaining_time

def update_countdown_labels(labels, events):
    for i, (event, date) in enumerate(events):
        remaining_time = countdown(date)
        if remaining_time.total_seconds() > 0:
            days = remaining_time.days
            hours, remainder = divmod(remaining_time.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            labels[i].config(text=f"{event}: {days}d {hours}h {minutes}m {seconds}s")
        else:
            labels[i].config(text=f"{event}: Event has passed!")

def main():
    root = Tk()
    root.title("Countdown Timer")

    events = read_events()
    labels = []

    for event, _ in events:
        label = Label(root, font=('Helvetica', 14))
        label.pack()
        labels.append(label)

    def update():
        update_countdown_labels(labels, events)
        root.after(1000, update)

    update()
    root.mainloop()

if __name__ == "__main__":
    main()
