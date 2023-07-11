**Numerical integration methods**

Numerical integration is the calculation of the approximate value of a certain integral.

The simplest methods of numerical integration:

1) Rectangle method (middle, left, right)
2) Trapezoid method
3) Simpson's method

**Rectangle method**

The essence of the method of medium rectangles is shown in the figure:

![](Images/Aspose.Words.fce7393b-c328-42f3-acff-902b87d9a1b6.001.png)

Other rectangle methods work in a similar way

|Left rectangle method|The right rectangle method|
| :-: | :-: |
|![](Images/Aspose.Words.fce7393b-c328-42f3-acff-902b87d9a1b6.002.png)|![](Aspose.Words.fce7393b-c328-42f3-acff-902b87d9a1b6.003.png)|



**Trapezoid method**

More accurate results can be obtained if you replace rectangles with trapezoids:

![](Images/Aspose.Words.fce7393b-c328-42f3-acff-902b87d9a1b6.004.png)

In this case, the value of a certain integral will be equal to the sum of the areas of all trapezoids in a given interval.

**Progress of the work**

1. Write a program that implements the methods of middle rectangles, left rectangles, right rectangles.

As the function under study, take:

1) Linear
2) Power
3) Trigonometric
4) …

For ease of use inside the program, arrange them in separate functions, for example:

def f1(x):
    return x + x \*\* 3 \* cos(x)

2. Select the integration interval and calculate analytically the corresponding definite integrals.
3. Select the integration step and calculate the integrals using the program. Create a table (see the next page) and enter the received values into it. Conduct several experiments with different integration steps.
4. Determine the absolute and relative errors for each function and for each method. Make a conclusion.
5. At what ratio of integration steps will the rectangle method give approximately the same accuracy as the trapezoid method?
6. Give recommendations on the choice of the integration step (or the number of partition segments) when using one of the methods.
7. Does the type of function depend on the accuracy of the method at the same integration step?
8. You can independently study, implement and investigate the Simpson method.

<table><tr><th rowspan="2"><b>Function</b></th><th rowspan="2"><p></p><p><b>Integration interval</b></p></th><th rowspan="2"><p></p><p><b>Integration step</b></p></th><th colspan="3"><b>Rectangle method</b></th><th rowspan="1"><p><b>Method</b></p><p>` `<b>trapezoids</b></p></th><th rowspan="1"><b>Analytically calculated value of the integral</b></th></tr>
<tr><td><b>Left</b></td><td><b>Right</b></td><td><b>Average</b></td></tr>
<tr><td rowspan="3">fx=5x+2</td><td rowspan="3">x∈-7;3</td><td>0\.01</td><td>-80.25</td><td>-79.75</td><td>-80 - (4∙10-13)</td><td>-80 - (4∙10-13)</td><td rowspan="3">-80</td></tr>
<tr><td><b>Absolute error:</b></td><td>0\.25</td><td>0\.25</td><td>` `4×10-13</td><td>4×10-13</td></tr>
<tr><td><b>Relative error:</b></td><td>3\.12*10-7</td><td>3\.13*10-7</td><td>5*10-15</td><td>5*10-15</td></tr>
<tr><td rowspan="3">fx= x3-5x+7</td><td rowspan="3">x∈-5;7</td><td>0\.01</td><td>465\.9606</td><td>470\.0406</td><td>467\.9996</td><td>468\.0006</td><td rowspan="3">468</td></tr>
<tr><td><b>Absolute error:</b></td><td>2\.0396</td><td>2\.0406</td><td>4×10-4</td><td>6×10-4</td></tr>
<tr><td><b>Relative погрешность:</b></td><td>4\.37719∙10-3</td><td>4\.34133∙10-3</td><td>8\.5∙10-7</td><td>1\.3∙10-6</td></tr>
<tr><td rowspan="3">fx= x3-5x+7</td><td rowspan="3">x∈-5;7</td><td>0\.001</td><td>467\.796</td><td>468\.204</td><td>467\.999</td><td>468 + (6∙10-6)</td><td rowspan="3">468</td></tr>
<tr><td valign="top"><b>Absolute error:</b></td><td>0\.204</td><td>0\.204</td><td>10-3</td><td>6×10-6</td></tr>
<tr><td valign="top"><b>Relative error:</b></td><td>4\.36*10-4</td><td>4\.35*10-4</td><td>2\.1*10-6</td><td>1\.3*10-8</td></tr>
<tr><td rowspan="3">fx=sinx∙x</td><td rowspan="3">x∈0;10</td><td>0\.01</td><td>7\.873820779144</td><td>7\.819418668055</td><td>7\.846731408066</td><td>7\.8466197236</td><td rowspan="3">7\.846694179875</td></tr>
<tr><td><b>Absolute погрешность:</b></td><td>2\.71265992∙10-2</td><td>2\.72755118∙10-2</td><td>3\.7228191∙10-5</td><td>7\.44563275∙10-5</td></tr>
<tr><td><b>Relative погрешность:</b></td><td>3\.44516∙10-3</td><td>3\.48818∙10-3</td><td>4\.74442∙10-6</td><td>9\.48987∙10-6</td></tr>
<tr><td rowspan="3">fx=sinx∙x</td><td rowspan="3">x∈0;10</td><td>0\.001</td><td>7\.849413540871</td><td>7\.843973329763</td><td>7\.846694552159</td><td>7\.846693435317</td><td rowspan="3">7\.846694179875</td></tr>
<tr><td><b>Absolute погрешность:</b></td><td>2\.71936099∙10-3</td><td>2\.72085011∙10-3</td><td>3\.72284∙10-7</td><td>7\.44558∙10-7</td></tr>
<tr><td><b>Relative погрешность:</b></td><td>3\.46441∙10-4</td><td>3\.46871∙10-4</td><td>4\.74447∙10-8</td><td>9\.48881∙10-8</td></tr>
</table>

4. It follows from the calculations that the smallest error (absolute and relative) was obtained using the method of average rectangles and the trapezoid method. Therefore, these methods are more accurate than the others.

5. The error of different methods depends on the type of function – so for a straight line and a sine wave, the error is less for the methods of middle rectangles and trapezoids, and for a parabola – for left and right rectangles. Also, the effectiveness of the methods depends on the step of the function and for a sufficiently small step, the trapezoid method is the most accurate. Therefore, to answer this question, you need to do a lot of research, changing the type of function and the integration step, to find some average value. I have conducted several experiments, analyzed and believe that the ratio of steps should be on the order of 0.1.

6. The rectangle method. The smaller the step we choose, the smaller the error will be at one step. And, consequently, the entire error will be smaller (since the errors of all steps are summed up).

7. Yes, it depends. It can be seen from the measurements given in the table. The reason for this is that it is much easier to integrate some functions than other complex ones. For example, a straight line and a hyperbola.
