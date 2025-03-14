from tkinter import ttk
import tkinter as tk
import functools
fp = functools.partial

from sys import platform

class VerticalScrolledFrame(ttk.Frame):
    """
    A pure Tkinter scrollable frame that actually works! 
    * Use the 'interior' attribute to place widgets inside the scrollable frame
    * Construct and pack/place/grid normally
    * This frame only allows vertical scrolling
    * -- NOTE: You will need to comment / uncomment code the differently for windows or linux 
    * -- or write your own 'os' type check.
    * This comes from a different naming of the the scrollwheel 'button', on different systems.
    """
    def __init__(self, parent, *args, **kw):

        # track changes to the canvas and frame width and sync them,
        # also updating the scrollbar
        def _configure_interior(event):
            # update the scrollbars to match the size of the inner frame
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the canvas's width to fit the inner frame
                canvas.config(width=interior.winfo_reqwidth())

        def _configure_canvas(event):
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the inner frame's width to fill the canvas
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())

        """
        This is linux code for scrolling the window, 
        It has different buttons for scrolling the windows
        """
        def _on_mousewheel(event, scroll=None):
            os = platform.system()
            if os == 'Windows':
                canvas.yview_scroll(int(-1*(event.delta/120)), "units")
            elif os == 'Darwin':
                canvas.yview_scroll(int(-1 * event.delta), "units")
            else:
                canvas.yview_scroll(int(scroll), "units")

        def _bind_to_mousewheel(event):
            os = platform.system()
            if os == 'Windows':
                canvas.bind_all("<MouseWheel>", _on_mousewheel)
            elif os == 'Darwin':
                canvas.bind_all("<MouseWheel>", _on_mousewheel)
            else:
                canvas.bind_all("<Button-4>", fp(_on_mousewheel, scroll=-1))
                canvas.bind_all("<Button-5>", fp(_on_mousewheel, scroll=1))

        def _unbind_from_mousewheel(event):
            os = platform.system()
            if os == 'Windows':
                canvas.unbind_all("<MouseWheel>")
            elif os == 'Darwin':
                canvas.unbind_all("<MouseWheel>")
            else:
                canvas.unbind_all("<Button-4>")
                canvas.unbind_all("<Button-5>")


        """
        This is windows code for scrolling the Frame
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        def _bind_to_mousewheel(event):
            canvas.bind_all("<MouseWheel>", _on_mousewheel)
        def _unbind_from_mousewheel(event):
            canvas.unbind_all("<MouseWheel>")
        """

        ttk.Frame.__init__(self, parent, *args, **kw)

        # create a canvas object and a vertical scrollbar for scrolling it
        vscrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL)
        vscrollbar.pack(fill=tk.Y, side=tk.RIGHT, expand=tk.FALSE)
        canvas = tk.Canvas(self, bd=0, highlightthickness=0,
                           yscrollcommand=vscrollbar.set)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)
        vscrollbar.config(command=canvas.yview)

        # reset the view
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)

        # create a frame inside the canvas which will be scrolled with it
        self.interior = interior = ttk.Frame(canvas)
        interior_id = canvas.create_window(0, 0, window=interior,
                                           anchor=tk.NW)

        interior.bind('<Configure>', _configure_interior)
        canvas.bind('<Configure>', _configure_canvas)
        canvas.bind('<Enter>', _bind_to_mousewheel)
        canvas.bind('<Leave>', _unbind_from_mousewheel)


# Thanks to chlutz214 for the usage update:
if __name__ == "__main__":
        # Set Up root of app
        root = tk.Tk()
        root.geometry("400x500+50+50")
        root.title("VerticalScrolledFrame Sample")

        # Create a frame to put the VerticalScrolledFrame inside
        holder_frame = tk.Frame(root)
        holder_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)

        # Create the VerticalScrolledFrame
        vs_frame = VerticalScrolledFrame(holder_frame)
        vs_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=tk.TRUE)

        # Fill the VerticalScrolledFrame
        i = 0
        while i != 100:
            item = tk.Entry(vs_frame.interior)
            item.insert(0, i)
            item.pack(side=tk.TOP, fill=tk.X, expand=tk.TRUE)
            i = i + 1

        # Run mainloop to start app
        root.mainloop()