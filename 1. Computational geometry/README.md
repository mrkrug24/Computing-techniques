Let's solve the problem of the point D belonging to the triangle ABC. A triangle is defined by the coordinates of its vertices.




Program tests for the coordinate method
Input data | Output data
|:---------:|:-----------:|
(2, 3), (9, 5), (6, 8), (5, 5) | Yes
(-427, -385), (753, -21), (-94, 435), (366, 663) | No
(0.98, 0.66), (3.45, 1.34), (1.67, 4.23), (2.19, 1.71) | Yes
(4, 3), (8, 6), (12, 5), (7, 3.75) | Yes, The point D lies on the side of the triangle ABC
(265, 150), (477, 270), (679, 448), (371, 210) | Yes, The point D lies on the side of the triangle ABC




Evaluation of the solution using the Heron formula
Advantage | Disadvantages
|:---------:|:-----------:|
Simple and clear to implement | Measurement error
It is the basis for solving similar problems (for n-gons) | The answer may be incorrect if the point is selected close to the side of the triangle
