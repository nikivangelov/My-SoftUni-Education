x = float(input())
y = float(input())
h = float(input())
green_front_side = x * x * 2 - 1.2*2
green_side = x * y * 2 - 1.5 * 1.5 * 2
green_paint_area = green_side + green_front_side
green_paint = green_paint_area / 3.4
red_triangle = x * h * 2 / 2
red_rectangle = x * y * 2
red_paint_area = red_rectangle + red_triangle
red_paint = red_paint_area / 4.3
print (f'{green_paint:.2f}')
print (f'{red_paint:.2f}')
