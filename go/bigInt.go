
import "math/big"

func multiply(num1 string, num2 string) string {

	var bignum1, _ = new(big.Int).SetString(num1, 0)
	var bignum2, _ = new(big.Int).SetString(num2, 0)
	// numBig1 := bignum1.Uint64()
	// numBig2 := bignum2.Uint64()
	var product = new(big.Int)
	product.Mul(bignum1, bignum2)
	res := product.Text(10)
	return res
}
