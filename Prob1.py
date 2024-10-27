from pgl import *

#1a
def create_histogram_array(data:list[int])->list[int]:
    counts = [0] * 10 # create list to keep track of numbers 0-9
    for digit in PI_DIGITS:
        counts[digit] += 1 # add 1 to the index of the digit in counts
    return counts

#1b
def print_histogram(hist:list[int]) -> None:
    '''for index, value in enumerate(hist):
        asterik = value * "*"
        print(index,": ", asterik, sep = "")'''
    [print(index,": ", value * "*", sep = "") for index, value in enumerate(hist)]

#1c
def graph_histogram(hist:list[int], width:int, height:int) -> None:

    def my_rect(x,y,w,h,color):
        rect = GRect(x,y,w,h)
        rect.set_filled(True)
        rect.set_color(color)
        gw.add(rect)

    gw = GWindow(width, height)

    if max(hist) > 0:
        max_v = max(hist)
    else:
        max_v = 1

    for i in range(len(hist)):
        col_width = width / len(hist)
        if hist[i] != 0:
            col_height = (height / max_v) * hist[i]
        else:
            col_height = 0
        x = i * col_width
        y = height - col_height

        my_rect(x, y, col_width, col_height, "red")

    

# Some testing printouts for your use!
PI_DIGITS = [3,1,4,1,5,9,2,6,5,3,5,5,8,9,7,9]
hist = create_histogram_array(PI_DIGITS)
print(hist)
print_histogram(hist) # uncomment to test
graph_histogram(hist, 400, 400) # uncomment to test
