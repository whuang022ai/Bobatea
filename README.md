
# Bobatea 

## a toolset wrapper for Sklearn , pandas ... etc. for data analysis tasks and ML tasks in terminal.


## Install

add /{your_path}/Bobatea_datatool/bin to ~/.bashrc
example : PATH=~/Bobatea_datatool/bin:$PATH

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
| cget        | get wanted columns                      |
| cdrop       | drop columns                            |
| csvf        | feature value filter                    |
| t           | data transpose                          |
| log         | apply logarithm                         |
| pca         | apply Principal component analysis      |
| scatter     | plot scatterter                         |
| kmean       | plot 2D kmeans                          |
| pair        | plot pair plot                          |
| hcluster    | plot hierarchical cluster plot          |

This commands are using with shell commands like cat , | , > etc... together to procressing data.

## Example of iris data apply pca

step1. get data :
```bash
$ wget http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data

```
step2. add header,index and choose features , run pca and plot
```bash
$ { echo "sepal_length,sepal_width,petal_length,petal_width,species" ; cat iris.data; } | index | cget --w "sepal_length sepal_width petal_length petal_width" |log | pca | scatter

```
or

```bash
$ { echo "sepal_length,sepal_width,petal_length,petal_width,species" ; cat iris.data; }  | index | cdrop --w "species" | log | pca | scatter
```

or
```bash
$ cat iris.data |index | header --h "sepal_length sepal_width petal_length petal_width species" | cdrop --w "species" | log | pca | scatter
```