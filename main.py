student_heights = input("INPUT LIST. ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
  total_height += height
print(total_height)

total = sum(student_heights)
print(total)

# nilai max
nilai = 0
for score in student_heights:
  if score > nilai:
    nilai = score
print(f"nilai tertinggi : {nilai}")