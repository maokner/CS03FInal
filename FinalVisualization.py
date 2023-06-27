import tkinter as tk

def draw(array, i, j):
    canvas.delete('all')

    # draw y-axis and labels
    draw_y_axis(max_value)

    for k, height in enumerate(array):
        left = k * rectangle_width + y_axis_margin
        right = (k+1) * rectangle_width + y_axis_margin
        top = canvas_height - height*scale_factor - y_margin
        bottom = canvas_height - y_margin

        color = 'red' if k == i or k == j else 'black'

        canvas.create_rectangle(left, top, right, bottom, fill=color)

        canvas.create_text((left+right)/2, bottom+15, text=str(height), font=("Arial", 12))

    canvas.create_text(y_axis_margin + 5, 20, anchor='w', text=f"i: {i}, arr[i]: {array[i]}", font=("Arial", 14))
    canvas.create_text(y_axis_margin + 5, 40, anchor='w', text=f"j: {j}, arr[j]: {array[j]}", font=("Arial", 14))

    root.update()  # update the GUI

def draw_y_axis(max_value):
    canvas.create_line(y_axis_margin, y_margin, y_axis_margin, canvas_height - y_margin, width=2)

    for y in range(0, max_value+1):
        y_pixel = canvas_height - y*scale_factor - y_margin
        canvas.create_text(y_axis_margin-10, y_pixel, text=str(y), font=("Arial", 12))
        canvas.create_line(y_axis_margin-5, y_pixel, y_axis_margin, y_pixel)


def I_cant_believe_it_can_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            yield (i, j)
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                yield (i, j)


def pause_sort():
    global paused
    paused = not paused
    if not paused:  # if it's not paused, then it's resumed. Start sorting.
        sort_step()


def next_step():
    global paused
    paused = True
    sort_step()
time_between_swaps = 100
def sort_step():
    try:
        i, j = next(iterator)
        draw(array, i, j)
        if not paused:
            root.after(time_between_swaps, sort_step)
    except StopIteration:
        pass  # finished sorting

# Initial unsorted array
#array =  [1, 6, 2, 3, 8, 9, 20]
array = [4, 3, 2, 5, 8, 1, 7, 6]

paused = False
iterator = I_cant_believe_it_can_sort(array)

root = tk.Tk()
canvas_height = 400
canvas_width = 600
y_axis_margin = 50
y_margin = 20
rectangle_width = (canvas_width - y_axis_margin) / len(array)
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

pause_button = tk.Button(root, text='Pause/Resume', command=pause_sort)
pause_button.pack()

next_button = tk.Button(root, text='Next', command=next_step)
next_button.pack()

max_value = max(array)
scale_factor = (canvas_height - 2*y_margin) / max_value

root.after(100, sort_step)

root.mainloop()
