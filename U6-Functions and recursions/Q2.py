#WAF TO PRINT THE ELEMENTS OF A LIST IN A SINGLE LINE
subjects=["physics","chemistry","maths","history","economics"]

def print_list(list):
    for item in list:
        print(item,end=" ")  #end=" " is used for printing items in single line with space

print_list(subjects)