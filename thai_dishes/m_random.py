import random
from m_list import menu_list

def m_rand():
    """Random by menu list"""
    menu = menu_list()
    rand_idx = random.randint(0, len(menu)-1)
    rand_dish = menu[rand_idx]
    return rand_dish



# Example usage
random_dish = m_rand()
print(f"Random dish: {random_dish}")