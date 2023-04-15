export const load = async ({ fetch }) => {
	const cartReturn = await fetch('https://dummyjson.com/carts');
	const cartData = await cartReturn.json();
	const carts = cartData.carts;

	return {
		carts
	};
};
