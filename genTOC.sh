#!/bin/bash

# cat "test.md"

# ./gh-md-toc "test.md"
sed "/./=" test.md |sed "/./N; s/\n/:/"|cat > haha.txt
# echo $ttoc
