**Practical work "Solving systems of linear equations by the Gauss method"**

The Gauss method is a classical method for solving a system of linear algebraic equations (SLA). It is named after the German mathematician Karl Friedrich Gauss.

The essence of the method consists in the sequential exclusion of variables, when by means of elementary transformations the system of equations is reduced to an equivalent system of triangular (stepwise) form, from which all the variables of the system are sequentially, starting from the last (by number).

An example of a SLOUGH solution by the Gauss method:
To simplify the appearance of the solution, we will make an expanded matrix of the system:

![](Images/Aspose.Words.8404e77e-8d5b-47e7-9bb1-6d363b328580.002.png)

In this matrix, coefficients for unknowns are located to the left before the vertical line, and free terms are located to the right after the vertical line.

For the convenience of dividing coefficients for variables (to get division by one), we rearrange the first and second rows of the matrix of the system. We obtain a system equivalent to this one, since in a system of linear equations, the equations can be rearranged:

![](Images/Aspose.Words.8404e77e-8d5b-47e7-9bb1-6d363b328580.003.png)

Using the new first equation, we exclude the variable x from the second and all subsequent equations. To do this, add the first row multiplied by ! to the second row of the matrix[](Images/Aspose.Words.8404e77e-8d5b-47e7-9bb1-6d363b328580.004.png) (in our case on ![](Images/Aspose.Words.8404e77e-8d5b-47e7-9bb1-6d363b328580.005.png)), to the third line – the first line multiplied by ![](Images/Aspose.Words.8404e77e-8d5b-47e7-9bb1-6d363b328580.006.png) (in our case on ![](Images/Aspose.Words.8404e77e-8d5b-47e7-9bb1-6d363b328580.007.png)).

This is possible because ![](Images/Aspose.Words.8404e77e-8d5b-47e7-9bb1-6d363b328580.008.png)

If there were more than three equations in our system, then we should add the first line to all subsequent equations multiplied by the ratio of the corresponding coefficients taken with a minus sign.

As a result, we obtain a matrix equivalent to this system of a new system of equations in which all equations, starting from the second one, do not contain the variable x:

![](Images/Aspose.Words.8404e77e-8d5b-47e7-9bb1-6d363b328580.009.png)

To simplify the second line of the resulting system , multiply it by ![](Images/Aspose.Words.8404e77e-8d5b-47e7-9bb1-6d363b328580.010.png) and we get again the matrix of the system of equations equivalent to this system:

![](Images/Aspose.Words.8404e77e-8d5b-47e7-9bb1-6d363b328580.011.png)

Now, keeping the first equation of the resulting system unchanged, we use the second equation to exclude the variable y from all subsequent equations. To do this, to the third row of the matrix of the system, add the second row multiplied by ![](Images/Aspose.Words.8404e77e-8d5b-47e7-9bb1-6d363b328580.012.png) (in our case on ![](Images/Aspose.Words.8404e77e-8d5b-47e7-9bb1-6d363b328580.013.png)).

If there were more than three equations in our system, then we should add a second line to all subsequent equations multiplied by the ratio of the corresponding coefficients taken with a minus sign.

As a result, we again obtain the matrix of a system equivalent to this system of linear equations:

![](Images/Aspose.Words.8404e77e-8d5b-47e7-9bb1-6d363b328580.014.png)

We have obtained a stepwise system of linear equations equivalent to this one:

![](Images/Aspose.Words.8404e77e-8d5b-47e7-9bb1-6d363b328580.015.png)

If the number of equations and variables is greater than in our example, then the process of sequential elimination of variables continues until the matrix of the system becomes stepwise, as in our example.

We will find the solution "from the end" - the reverse course. To do this, from the last equation, we define z:
![](Images/Aspose.Words.8404e77e-8d5b-47e7-9bb1-6d363b328580.016.png).

Substituting this value into the preceding equation, we find y:
![](Images/Aspose.Words.8404e77e-8d5b-47e7-9bb1-6d363b328580.017.png)

From the first equation we find x:
![](Images/Aspose.Words.8404e77e-8d5b-47e7-9bb1-6d363b328580.018.png)

Answer: the solution of this system of equations is ![](Images/Aspose.Words.8404e77e-8d5b-47e7-9bb1-6d363b328580.019.png).


**Progress of the work**
1. Classify the SLOWS by the presence and number of solutions and fill in the table:

|Item no.|Number of solutions|Name|
| :-: | :-: | :-: |
|1\.|Exactly one|Defined|
|2\.|Infinite set|Indefinite|
|3\.|No|Incompatible|

2. Write a program solving SLOUGH by the Gauss method. The program should receive the number of equations in the system, coefficients for unknowns and a vector of free terms as input. At the output, the program should output a solution to this system – a vector of values.

Additionally:

1) The program should determine the possibility of solving the original system.
2) To minimize errors, the program must modify the source data accordingly.
   (The program code is located in the Gauss.py file)


3. List the main advantages and disadvantages of the Gauss method:

|Advantages|Disadvantages|
| :-: | :-: |
|<p>Simpler, clearer, less time-consuming than others.</p><p></p><p>Determines the absence of roots.</p>|<p>Accumulation of computational error during its implementation.</p><p></p><p>Slower than others.</p><p></p>|
