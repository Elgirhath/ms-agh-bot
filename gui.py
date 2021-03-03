import tkinter as tk
from tkcalendar import DateEntry
from datetime import datetime
import bot
import argparse
import sys

parser = argparse.ArgumentParser(description='Run gui for AGH football game finder.')
parser.add_argument('-d', '--debug', action='store_const', default=False, const=True)
parsed_args = parser.parse_args()

sys.stderr = open('logs.txt', 'a')

args = {
    "start_date": None,
    "end_date": None,
    "full_field_only": False,
    "refresh_rate": 30,
    "advance_min": 30,
    "level": None,
    "comment": "+1",
    "email": "konradpolarczyk98@gmail.com",
    "password": "",
    "group_url": "https://www.facebook.com/groups/BoiskoMSAGH/"
}

if parsed_args.debug:
    args["group_url"] = "https://www.facebook.com/groups/374471560293557"

root = tk.Tk()
root.title("MS-AGH GUI")

inner_root = tk.Frame(root)
inner_root.grid(padx=20, pady=20)

password_frame = tk.Frame(inner_root)

tk.Label(password_frame, text="Hasło do Facebooka: ").pack(side=tk.LEFT, fill=tk.BOTH)

password = tk.Entry(password_frame, show="*", width=30)
password.focus()
password.pack(side=tk.LEFT, fill=tk.BOTH)

password_frame.grid(columnspan=2, sticky="nsew", pady=2)

tk.Label(inner_root, text="Od daty: ").grid(column=0)

time = datetime.now().timetuple()

start_date = DateEntry(inner_root, bg="darkblue",fg="white",year=time.tm_year, month=time.tm_mon, day=time.tm_mday, date_pattern='dd.mm.y')
start_date.grid(row=2, column=0, sticky="nsew")

start_timeframe = tk.Frame(inner_root)

start_time_hour = tk.Entry(start_timeframe, width=10)
start_time_hour.insert(tk.END, str(time.tm_hour).zfill(2))
start_time_hour.pack(side=tk.LEFT)

colon = tk.Label(start_timeframe, text=":")
colon.pack(side=tk.LEFT)

start_time_min = tk.Entry(start_timeframe, width=10)
start_time_min.insert(tk.END, "00")
start_time_min.pack(side=tk.LEFT)

start_timeframe.grid(row=3, column=0)

tk.Label(inner_root, text="Do daty: ").grid(row=1, column=1)

end_date = DateEntry(inner_root,bg="darkblue",fg="white",year=time.tm_year, month=time.tm_mon, day=time.tm_mday, date_pattern='dd.mm.y')
end_date.grid(row=2, column=1, sticky="nsew")

end_timeframe = tk.Frame(inner_root)

end_time_hour = tk.Entry(end_timeframe, width=10)
end_time_hour.insert(tk.END, str(time.tm_hour + 1).zfill(2))
end_time_hour.pack(side=tk.LEFT)

colon = tk.Label(end_timeframe, text=":")
colon.pack(side=tk.LEFT)

end_time_min = tk.Entry(end_timeframe, width=10)
end_time_min.insert(tk.END, "00")
end_time_min.pack(side=tk.LEFT)

end_timeframe.grid(row=3, column=1)

full_field_frame = tk.Frame(inner_root)

tk.Label(full_field_frame, text="Tylko na całe boisko: ").pack(side=tk.LEFT, fill=tk.BOTH)

full_field_only = tk.IntVar()
tk.Checkbutton(full_field_frame, variable=full_field_only).pack(side=tk.RIGHT, fill=tk.BOTH)

full_field_frame.grid(columnspan=2, sticky="nsew", pady=2)

refresh_rate_frame = tk.Frame(inner_root)

tk.Label(refresh_rate_frame, text="Częstotliwość odświeżania (s): ").pack(side=tk.LEFT)

refresh_rate = tk.Entry(refresh_rate_frame, width=10)
refresh_rate.insert(tk.END, args["refresh_rate"])
refresh_rate.pack(side=tk.RIGHT, fill='x')

refresh_rate_frame.grid(columnspan=2, sticky="nsew", pady=2)

advance_frame = tk.Frame(inner_root)

tk.Label(advance_frame, text="Czas potrzebny przed rozpoczęciem gry (min): ").pack(side=tk.LEFT, fill=tk.BOTH)

advance = tk.Entry(advance_frame, width=10)
advance.insert(tk.END, args["advance_min"])
advance.pack(side=tk.RIGHT, fill=tk.BOTH)

advance_frame.grid(columnspan=2, sticky="nsew", pady=2)

comment_frame = tk.Frame(inner_root)

tk.Label(comment_frame, text="Komentarz: ").pack(side=tk.LEFT, fill=tk.BOTH)

comment = tk.Entry(comment_frame, width=30)
comment.insert(tk.END, args["comment"])
comment.pack(side=tk.RIGHT, fill=tk.BOTH)

comment_frame.grid(columnspan=2, sticky="nsew", pady=2)
    
def on_ok_click():
    start_date_time = datetime.strptime(f"{start_date.get()} {start_time_hour.get()}:{start_time_min.get()}", '%d.%m.%Y %H:%M')
    end_date_time = datetime.strptime(f"{end_date.get()} {end_time_hour.get()}:{end_time_min.get()}", '%d.%m.%Y %H:%M')
    args["start_date"] = start_date_time
    args["end_date"] = end_date_time
    args["full_field_only"] = bool(full_field_only.get())
    args["refresh_rate"] = int(refresh_rate.get())
    args["advance_min"] = int(advance.get())
    args["comment"] = comment.get()
    args["password"] = password.get()
    root.destroy()

    bot.main(args)

root.bind('<Return>', lambda event: on_ok_click())

button = tk.Button(inner_root, text="OK", command=on_ok_click)
button.grid(pady=(10, 0), ipadx=20, columnspan=2, sticky="nsew")

inner_root.mainloop()