import tkinter as tk
from tkinter import ttk
from RoGroupFinder import find_groups_with_keyword_and_classic_clothing

def search_groups():
    start_group_id = int(start_group_id_entry.get())
    end_group_id = int(end_group_id_entry.get())
    keyword = keyword_entry.get()
    result = find_groups_with_keyword_and_classic_clothing(start_group_id, end_group_id, keyword)
    result_label["text"] = f"Found groups: {', '.join(map(str, result))}"

root = tk.Tk()
root.title("RoGroupFinder")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

start_group_id_label = ttk.Label(frame, text="Start Group ID:")
start_group_id_label.grid(row=0, column=0, sticky=tk.W)
start_group_id_entry = ttk.Entry(frame)
start_group_id_entry.grid(row=0, column=1)

end_group_id_label = ttk.Label(frame, text="End Group ID:")
end_group_id_label.grid(row=1, column=0, sticky=tk.W)
end_group_id_entry = ttk.Entry(frame)
end_group_id_entry.grid(row=1, column=1)

keyword_label = ttk.Label(frame, text="Keyword:")
keyword_label.grid(row=2, column=0, sticky=tk.W)
keyword_entry = ttk.Entry(frame)
keyword_entry.grid(row=2, column=1)

search_button = ttk.Button(frame, text="Search", command=search_groups)
search_button.grid(row=3, column=1, sticky=tk.E)

result_label = ttk.Label(frame, text="Found groups:")
result_label.grid(row=4, column=0, columnspan=2, sticky=tk.W)

root.mainloop()
