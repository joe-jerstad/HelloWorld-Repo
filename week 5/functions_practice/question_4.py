def coin_converter(bronze_coins):
    gold_coins = bronze_coins // 300
    silver_coins = (bronze_coins % 300) // 20
    remain_bronze = (bronze_coins % 300) % 20
    final_string = ''
    if gold_coins > 0:
        final_string += f'{gold_coins} gold '
    if silver_coins > 0:
        final_string += f'{silver_coins} silver '
    if remain_bronze > 0:
        final_string += f'{remain_bronze} bronze '
    return final_string

print(coin_converter(903))