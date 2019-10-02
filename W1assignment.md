Week 1 Assignment - Basic Concepts
================
Kenisha Priester
July 7, 2019

# Introduction

The purpose of this assignment is to use a dataset to explore basic
statistical concepts in the R programming language. I will conduct
exploratory data analysis on the [Diamonds dataset from
Kaggle](https://www.kaggle.com/shivam2503/diamonds).

## Load Data

In the code below, I used the `read.csv` function to load in the data
from its csv file format into a data frame. The `fix` function shows the
raw data in the R Text Editor.

``` r
diamonds = read.csv("diamonds.csv")

fix(diamonds)
```

## Data Shape and Features

The Diamonds dataset has 53940 rows and 11 columns. The columns in the
dataset contain features such as carat, cut, color, clarity, and price.
The `x`, `y`, and `z`, features represent length, width, and depth (in
millimeters) of a diamond, respectively. The `na.omit` function should
remove any missing (null) values however when looking at the dimensions
of the dataset after using this function the same number of rows remain,
so it seems as though all the rows within the dataset are
    complete.

``` r
dim(diamonds)
```

    ## [1] 53940    11

``` r
names(diamonds)
```

    ##  [1] "X"       "carat"   "cut"     "color"   "clarity" "depth"   "table"  
    ##  [8] "price"   "x"       "y"       "z"

``` r
diamonds = na.omit(diamonds)

dim(diamonds)
```

    ## [1] 53940    11

## Descriptive Statistics

The `summary` function output basic descriptive statistics for a
dataset. For quantitative variables, the results include the minimum and
maximum values within the data, and the mean, median, first and third
quartile values derived from the data. When a variable is qualitative,
then the output shows the unique attributes and their frequencies
(count).

``` r
summary(diamonds)
```

    ##        X             carat               cut        color    
    ##  Min.   :    1   Min.   :0.2000   Fair     : 1610   D: 6775  
    ##  1st Qu.:13486   1st Qu.:0.4000   Good     : 4906   E: 9797  
    ##  Median :26971   Median :0.7000   Ideal    :21551   F: 9542  
    ##  Mean   :26971   Mean   :0.7979   Premium  :13791   G:11292  
    ##  3rd Qu.:40455   3rd Qu.:1.0400   Very Good:12082   H: 8304  
    ##  Max.   :53940   Max.   :5.0100                     I: 5422  
    ##                                                     J: 2808  
    ##     clarity          depth           table           price      
    ##  SI1    :13065   Min.   :43.00   Min.   :43.00   Min.   :  326  
    ##  VS2    :12258   1st Qu.:61.00   1st Qu.:56.00   1st Qu.:  950  
    ##  SI2    : 9194   Median :61.80   Median :57.00   Median : 2401  
    ##  VS1    : 8171   Mean   :61.75   Mean   :57.46   Mean   : 3933  
    ##  VVS2   : 5066   3rd Qu.:62.50   3rd Qu.:59.00   3rd Qu.: 5324  
    ##  VVS1   : 3655   Max.   :79.00   Max.   :95.00   Max.   :18823  
    ##  (Other): 2531                                                  
    ##        x                y                z         
    ##  Min.   : 0.000   Min.   : 0.000   Min.   : 0.000  
    ##  1st Qu.: 4.710   1st Qu.: 4.720   1st Qu.: 2.910  
    ##  Median : 5.700   Median : 5.710   Median : 3.530  
    ##  Mean   : 5.731   Mean   : 5.735   Mean   : 3.539  
    ##  3rd Qu.: 6.540   3rd Qu.: 6.540   3rd Qu.: 4.040  
    ##  Max.   :10.740   Max.   :58.900   Max.   :31.800  
    ## 

## Visualization

#### Histograms

R has a few built-in visualization functions to graphically inspect the
shape of the data. In the first two charts, I used the `hist` function
to look at the distribution of diamond prices and carats. In both charts
the data is right-skewed, meaning that the majority of values fall
towards the lower end of the range. In other words, most diamonds tend
to be under $5,000 and are 1.5 carats or less.

``` r
hist(diamonds$price, xlab="Price", main="Histogram of Diamond Prices")
```

![](W1assignment_files/figure-gfm/unnamed-chunk-6-1.png)<!-- -->

``` r
hist(diamonds$carat, xlab="Carat", main="Histogram of Diamond Carats")
```

![](W1assignment_files/figure-gfm/unnamed-chunk-7-1.png)<!-- -->

#### Plots

The following graphs use the `plot` function with varying chart outputs
depending on the data types. A scatterplot is generated if both values
are quantitative, a bar chart comes from using only one quantitative
variable, a box plot uses a qualitative variable on the x-axis and a
quantitative variable on the y-axis, and a stacked bar plot results from
quantitative variables being used on both the x- and y-axis.

The third graph shows a scatterplot comparing the trend of diamond
carats to price. From the lowest end of range for number of carats
through about 2.5 carats, there is a strong upward trend that shows for
an increasing amount of carats the price also is more expensive for the
diamond. However, after 2.5 carats is where the prominent outliers seem
to occur. There are diamonds with higher carats but have a lower price
value and also some diamonds that have similar expensive prices but are
different carat weights. From this insight, I could hypothesize that
this discrepancy could be due to other feature differences such as cut
or
clarity.

``` r
plot(diamonds$carat, diamonds$price, xlab="Carat", ylab="Price", main="Comparison of Diamond Carats vs Price")
```

![](W1assignment_files/figure-gfm/unnamed-chunk-8-1.png)<!-- -->

In the fourth graph, the output shows a bar plot with the number of
diamonds by each cut type. Ideal has the highest count of diamonds in
this dataset, which interestingly is the most “perfect” (in symmetry and
proportion) type that exists within the
data.

``` r
plot(diamonds$cut, xlab="Cut", ylab="Count", main="Count of Diamonds per Cut Type")
```

![](W1assignment_files/figure-gfm/unnamed-chunk-9-1.png)<!-- -->

The fifth chart is a boxplot that compares the distribution of each
diamond cut type to carats. The median carat for the “Fair” cut type is
1 carat. yet there are many outliers beyond the 2 carat threshold. The
“Ideal” cut type has the lowest carat median (about 0.5 carats)
however there are still several outliers at higher carat weights (up
until about 3.5
carats).

``` r
plot(diamonds$cut, diamonds$carat, xlab="Cut", ylab="Carat", main="Distribution of Diamond Carats per Cut Type")
```

![](W1assignment_files/figure-gfm/unnamed-chunk-10-1.png)<!-- -->

This final graph is a stacked bar that shows the proportion of diamonds
of a particular cut by each clarity type. It seems in the VVS1 and VVs2
categories (the most “clear” of the diamonds) most people buy a lesser
cut quality since the largest ratio of cut is
“Good”.

``` r
plot(diamonds$clarity, diamonds$cut, xlab="Clarity", ylab="Cut", main="Ratio of Diamond Cut per Clarity Type")
```

![](W1assignment_files/figure-gfm/unnamed-chunk-11-1.png)<!-- -->

# References

Introduction to R (pp. 42-51) James, G., Witten, D., Hastie, T., and
Tibshirani, R. (2013). An Introduction to Statistical Learning with
Applications in R. Springer. Retrieved from:
<http://www-bcf.usc.edu/~gareth/ISL/ISLR%20Fourth%20Printing.pdf>

Wikipedia contributors. (2019, June 1). Diamond cut. In Wikipedia, The
Free Encyclopedia. Retrieved from
<https://en.wikipedia.org/w/index.php?title=Diamond_cut&oldid=899825187>
