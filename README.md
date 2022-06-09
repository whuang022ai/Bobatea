
# Bobatea 波霸奶茶


## An all-in-one command-line toolbox for data scientists to complete their daily job easier and Low-code .

<p align="center">
  <img src="https://imgur.com/ua98vQA" width="150" >
</p>

## Support common data cleaning and machine learning methods from Pandas, Sklearn Seborn, etc.
---

## Install

add /your_path/Bobatea_datatool/bin to ~/.bashrc
example : "PATH=~/Bobatea_datatool/bin:$PATH"

source ~/.bashrc

and run install.sh : 

```bash
$ bash install.sh

```

## Support command

| **command** | **function**                            |
|-------------|-----------------------------------------|
| index       | add index to data                       | 
| header      | add header to data                      | 
| take        | take wanted columns                     |
| drop        | drop unwant columns                     |
| range       | take wanted rows range                  |
| merge       | merge two datasheets together by index  |
| csvf        | feature value filter                    |
| t           | data transpose                          |
| log         | apply logarithm                         |
| mean        | apply arithmetic mean                   |
| pca         | apply Principal component analysis      |
| tsne        | apply tSNE                              |
| scatter     | plot scatterter                         |
| kmean       | plot 2D kmeans                          |
| pair        | plot pair plot                          |
| curve       | plot line curve plot                    |
| hcluster    | plot hierarchical cluster plot          |

These commands are well integrated with terminal commands like cat, |, >, etc... together to build the data pipeline faster and easier.

## Example of iris data applying pca

step1. get data :
```bash
$ wget http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data

```
step2. add header, index and choose features, run PCA, and plot in just less than one minute.
```bash
$ cat iris.data | header --h "sepal_length,sepal_width,petal_length,petal_width,species"  | drop species | pca | scatter 


```

more exampls please checkout ./test/