# The program is coded using TCL
proc fac {n} {
    if { $n == 0 } {
        return 1
    } else {
        return [expr {$n*[fac [expr {$n-1}]]}]
    }
}
# input from keyboard
set n [gets stdin]   

if { $n <=0 || $n>10 } {
        puts "Input a number in valid range"
    } else {
       # print the data returned from function
		puts "[fac $n]"
    }

 
