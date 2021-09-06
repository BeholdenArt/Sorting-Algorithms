import tkinter
import selectionSort, bubbleSort, insertionSort, quickSort


def on_click(txt):
    if txt == "s":
        selectionSort.main()
    if txt == "b":
        bubbleSort.main()
    if txt == "i":
        insertionSort.main()
    if txt == "q":
        quickSort.main()

root = tkinter.Tk()
root.title("SORTING ALGORITHM VISUALIZER")
root.resizable(0, 0)
root.geometry("450x450")
heading_img = tkinter.PhotoImage(file="images/heading.png")


heading_label = tkinter.Label(root, image= heading_img)
selection_sort_button = tkinter.Button(root, text= "Selection Sort (O(n^2))", padx= 50, pady= 50, command= lambda: on_click("s"))
bubble_sort_button = tkinter.Button(root, text= "Bubble Sort (O(n^2))", padx= 50, pady= 50, command= lambda: on_click("b"))
insertion_sort_button = tkinter.Button(root, text= "Insertion Sort (O(n^2))", padx= 50, pady= 50, command= lambda: on_click("i"))
quick_sort_button = tkinter.Button(root, text= "Quick Sort (O(n^2))", padx= 54, pady= 50, command= lambda: on_click("q"))

heading_label.grid(row= 0, column= 0, columnspan= 2, pady= 50)
selection_sort_button.grid(row= 1, column= 0)
bubble_sort_button.grid(row= 1, column= 1)
insertion_sort_button.grid(row= 2, column= 0)
quick_sort_button.grid(row= 2, column= 1)

win_width = root.winfo_width()
win_height= root.winfo_height()

root.mainloop()