declare -g folders=()
for commit in $(git log | grep commit  | grep -v Initial | cut -d ' ' -f2); do
   #echo $commit
   for folder in $(git diff-tree --no-commit-id --name-only -r $commit); do
      #git log | grep $commit -A 2 | grep -v commit | grep -v Author
      if ! [[ " ${folders[@]} " =~ " ${folder} " ]]; then
         folders+=($folder)
         gitauth=$(git log | grep $commit -A 1 | grep -v commit)
         gitdate=$(git log | grep $commit -A 2 | grep -v commit | grep -v Author)
         printf "$folder modified $gitdate $gitauth \n"
      fi
   done
done
