import dearpygui.dearpygui as dpg

dpg.create_context()

with dpg.font_registry():
    default_font = dpg.add_font("CascadiaCode-Light.otf", 16)
    bold_font = dpg.add_font("CascadiaCode-Bold.otf", 22)

dpg.bind_font(default_font)

with dpg.window(tag="main_mindow", pos=[10, 10], width=700, height=680,
    no_resize=True, no_title_bar=True, no_move=True, no_background=True):
    
    with dpg.plot(label="Room Temperature", pos = [0, 0], height=300, width=700):
        dpg.add_plot_axis(dpg.mvXAxis, no_gridlines=True, tag="xaxis_tag1")
        dpg.add_plot_axis(dpg.mvYAxis, label="Temperature (degC)", tag="yaxis_tag1")

        dpg.set_axis_ticks("xaxis_tag1", (("Env", 1), ("Cell1", 4), ("Cell2", 6), ("Cell3", 8), ("Cell4", 10), 
                            ("Cell5", 12), ("Cell6", 14), ("Cell7", 16), ("Cell8", 18)))

        dpg.add_bar_series([1, 4, 6, 8, 10, 12, 14, 16, 18], [80, 35, 40, 45, 50, 55, 60, 65, 70], weight=1, parent="yaxis_tag1")

    with dpg.plot(label="Chamber Temperature", pos = [0, 320], height=300, width=700):
        dpg.add_plot_axis(dpg.mvXAxis, no_gridlines=True, tag="xaxis_tag2")
        dpg.add_plot_axis(dpg.mvYAxis, label="Temperature (degC)", tag="yaxis_tag2")

        dpg.set_axis_ticks("xaxis_tag2", (("Env", 1), ("Cell1", 4), ("Cell2", 6), ("Cell3", 8), ("Cell4", 10), 
                            ("Cell5", 12), ("Cell6", 14), ("Cell7", 16), ("Cell8", 18)))
        
        dpg.add_bar_series([1, 4, 6, 8, 10, 12, 14, 16, 18], [180, 135, 140, 145, 150, 155, 160, 165, 170], weight=1, parent="yaxis_tag2")

dpg.create_viewport(title="TempLogger_GUI", x_pos=0, y_pos=0, width=1300, height=680)
dpg.setup_dearpygui()
dpg.show_viewport()

while dpg.is_dearpygui_running():
    dpg.render_dearpygui_frame()

dpg.destroy_context()


######### Demo DearPyGUI #########

# import dearpygui.dearpygui as dpg
# import dearpygui.demo as demo

# dpg.create_context()
# dpg.create_viewport(title='Custom Title', width=600, height=600)

# demo.show_demo()

# dpg.setup_dearpygui()
# dpg.show_viewport()
# dpg.start_dearpygui()
# dpg.destroy_context()