
#!/usr/bin/env bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
alias="source $SCRIPT_DIR/bobatea.sh"
echo -e $alias >> ~/.bashrc
source ~/.bashrc