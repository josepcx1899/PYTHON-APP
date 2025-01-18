def on_mouse_wheel(event):
    canvas = event.widget
    if event.delta > 0:
        canvas.yview_scroll(-1, "units")
    else:
        canvas.yview_scroll(1, "units")