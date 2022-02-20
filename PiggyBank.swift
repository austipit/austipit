/*
This code tranfers foreign currency into the correct USD amount
*/

var pesos: Double = 100000.0
// 1 peso = 0.00029 USD
var reais: Double = 50000.0
//1 Real equals 0.24 USD
var soles: Double = 25000.0
//1 Sol equals 0.29 USD 
var total: Double = 0
total = 0.00029 * pesos + 0.24 * reais + 0.29 * soles
print("US Dollars = $\(total)")
