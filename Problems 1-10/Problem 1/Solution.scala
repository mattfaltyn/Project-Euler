// Define function with input Range and output Integer
def sumMultiplesOf3Or5(range: Range): Int = {
    // Filter all n in range such that only n mod 3 = 0 or n mod 5 = 0 are selected
    range.filter(n => n % 3 == 0 || n % 5 == 0).sum
}
// Define maximum value
val max = 1000;
// Print output 
println(s"The sum of all the multiples of 3 or 5 below ${max}: " + sumMultiplesOf3Or5(1 until max));