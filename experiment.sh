# !/bin/bash
# pipenv install --dev

default="pipenv run python tada_a_bigoh.py --directory ../speed-surprises/"

schema="--schema=../speed-surprises/sortingjsonsch.json"

modules=(
        lists.sorting
        search.basic_search
)

sort_funcs=(
          insertion_sort
          bubble_sort
          merge_sort
)

sort_tcpx=(
          O\(n\)
          O\(n^2\)
          O\(nlogn\)
)

sch_funcs=(
          compute_linear_search
          compute_binary_search
)

sch_tcpx=(
          O\(n\)
          O\(logn\)
)


list_sts=(
hypothesis\ $schema
)

startsize=(25 50 75 100 125 150 175 200 225 250 275 300)

# run sorting algorithm
run_sort () {
  for n in ${!sort_funcs[@]}; do
    for ((i=0; i<${#list_sts[@]}; i++))
    do
      for size in ${startsize[@]}; do
        ${default} \
        --module speedsurprises.${modules[0]} \
        --function ${sort_funcs[n]} \
        --types ${list_sts[i]} \
        --startsize $size \
        --expect ${sort_tcpx[n]}
      done
    done
  done
}

run_search () {
  for n in ${!sch_funcs[@]}; do
    for ((i=0; i<${#list_sts[@]}; i++))
    do
      for size in ${startsize[@]}; do
        $default \
        --module speedsurprises.${modules[1]} \
        --function ${sch_funcs[n]} \
        --types ${list_sts[i]} \
        --startsize $size \
        --expect ${sch_tcpx[n]}
      done
    done
  done
}

# for ((i = 0 ; i <= 4 ; i++))
# do
#   run_sort
#   run_search
# done

run_sort
run_search
