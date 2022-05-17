
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
| cget        | get wanted columns                      |
| csvf        | feature value filter                    |
| t           | data transpose                          |
| log         | apply logarithm                         |
| pca         | apply Principal component analysis      |
| scat        | plot scatter                            |
| pair        | plot pair plot                          |
| hcluster    | plot hierarchical cluster plot          |

## Example of iris data apply pca

step1. get data :
```bash
$ wget http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data

```
step2. add header,index and choose features , run pca and plot
```bash
$ { echo "sepal_length,sepal_width,petal_length,petal_width,species" ; cat iris.data; } | index | cget --w "sepal_length sepal_width petal_length petal_width" |log | pca | scat

```

