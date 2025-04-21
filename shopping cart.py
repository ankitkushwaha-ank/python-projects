class ITEMS:
    def __init__(self , items , prices):
        self.price = prices
        self.item = items
        self.view_cart = ''

    def shoppingcart(self,add_item ,item_price):
        self.product = add_item
        self.price = item_price

        self.product += self.view_cart
        print(f'{self.product} added to your cart')

    def cart(self):
        return self.view_cart



cart = ITEMS(items="mobile",prices=10000 )
cart.shoppingcart("bike",95000)
cart.cart()
