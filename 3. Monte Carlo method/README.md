**Practical work "Determination of the number π by the Monte Carlo method"**

Monte Carlo Methods (MMC) are a group of numerical methods for studying random processes. The essence of the method is as follows: the process is described by a mathematical model using a random variable generator, the model is repeatedly calculated, the probabilistic characteristics of the process under consideration are calculated based on the data obtained.

For example, to find out by the Monte Carlo method what the average distance between two random points in a circle will be, you need to take the coordinates of a large number of random pairs of points within the boundaries of a given circle, calculate the distance for each pair, and then calculate the arithmetic mean for them.

The methods are used to solve problems in various fields of physics, chemistry, mathematics, economics, optimization, control theory, etc.

Let's determine the value of the number π using the Monte Carlo method. Let there be a square and a circle inscribed in it. We will randomly place a certain number of points inside the square. The ratio of the number of points inside the circle to the total number of points placed will be approximately equal to the ratio of the area of the circle and the area of the square. Knowing the formulas for calculating the areas of these figures, you can make an expression to find the approximate value of the number π.

**Progress of the work**

1. Write down formulas for calculating the area of a square and a circle (here and further use Word tools to write formulas (Insert – Equation)):

|Square|Circle|
| :-: | :-: |
|$S_1=4R^2$|$S_2=πR^2$|

2. Make an expression to calculate the approximate value of the number π:

$π = 4nN_1$

3. Write down a logical expression to determine whether a point belongs to a circle:

If $x^2 + y^2 ≤ R~2$, then the point belongs to the circle.

4. Write a program.

Input data:

1) the size of the square
2) the number of dots to be placed

Output data:

1) The number of points inside the circle
2) The ratio of the total number of points placed to the number of points inside the circle
3) The calculated value of the number π
4) Absolute error
5) Relative error

Additionally, it is possible to make it possible to automatically conduct a given number of experiments and average the resulting value.

For the reference value of the number π, we can take the value 3.141592653589793238462643383279.

5. Conduct a series of experiments with different input data and fill in the table:


|**experiment No.**|**1**|**2**|**3**|**4**|**5**|**6**|**7**|**8**|**9**|**10**|
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| Number of points|$10^2$|$10^2$|$10^3$|$10^3$|$10^4$|$10^4$|$10^4$|$10^5$|$10^5$|$10^6$|
|Square Size|$10^3$|$10^4$|$10^4$|$10^5$|$10^5$|$10^6$|$10^7$|$10^7$|$10^8$|$10^8$|
|Calculated value of the number π|3.08|3.12|3.18|3.152|3.133|3.148|3.152|3.152|3.151|3.141|
|Absolute error|0\.26|0\.022|0\.038|0\.01|0\.009|0\.006|0\.01|0\.009|0\.009|0\.0007|
|0 Relative error|0\.09|0\.006|0\.012|0\.003|0\.003|0\.002|0\.003|0\.003|0\.003|0\.0003|


6. Analyze the table and make a conclusion about the accuracy of the method, its dependence on the values of the input parameters.

Roughly speaking:

With a larger side of the square, the error is greater, with a smaller one – less.

With a larger number of points, the error is less, with a smaller one – more.

The method is not accurate for any input data. You need a lot of statistics and close orders of input data (the number of points and the sides of the square). For example, if the side of the square is 1010, and there are 10 points, there will be a very large spread (the distance between the points), which will greatly affect the answer.


7. Come up with a problem that can be solved using the Monte Carlo method.

Each of the two players chooses a sequence of 5 digits (zeros and ones). Petya chose - 01100, and Danya – 11010. Then the players toss a coin and write down what falls out: heads – zero, tails – one. The winner is the one who has the first sequence coincided with a part of the total series. Count who has more chances to win.



8. Why does the Monte Carlo method have such a name?

The name of the method comes from the name of the commune in the principality Monaco, widely known for its numerous casinos, since roulette is one of the most widely known random number generators.
