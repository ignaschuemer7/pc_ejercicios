def total_gain_neta(volume,intial_price,final_price,cost):
    """
    Parameters
    ----------
    volume : float
        It use to insert the amount items.
    intial_price : float
        It use to insert the price of the GRO.
    final_price : float
        It use to insert the final price of the GRO.
    cost : float
        It use to insert the price of the book.
        
    Returns
    -------
    ganancianeta : float
        It is the gain you have.
    """
    ganancianeta =volume * final_price - (intial_price * volume)
    return ganancianeta

def total_gain(volume,intial_price,final_price,cost):
    """
    Parameters
    ----------
    volume : float
        It use to insert the amount items.
    intial_price : float
        It use to insert the price of the GRO.
    final_price : float
        It use to insert the final price of the GRO.
    cost : float
        It use to insert the price of the book.
        
    Returns
    -------
    volumenavender : float
        It is the amount of items that you need to sell.
    """
    volumenavender=(cost/final_price)+(intial_price*volume)/final_price
    return volumenavender


print("Para comprar el libro a partir de mis ganancias, debo vender",total_gain(12095.2, 0.86, 1.28, 2831.97),"items \n")    
print("La ganancia neta es de",total_gain_neta(12095.2, 0.86, 1.28, 2831.97))