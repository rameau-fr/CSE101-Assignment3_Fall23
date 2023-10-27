def doesExist(lst,query):
    """ 
    Check if the queried value exists within the range of the list values.

    Args:
        lst (list): A sorted list of numbers.
        query (int/float): The number you're searching for.

    Returns:
        bool: True if the query lies within the range of the list values, otherwise False.
    """
    ...

def computeMidpoints(low, high):
    """ 
    Calculate the two midpoints for ternary search.

    Args:
        low (int): The lower index of the current search space.
        high (int): The upper index of the current search space.

    Returns:
        tuple: Two midpoints dividing the current search space into three segments.
    """
    ...

def ternarySearch(lst, query):
    """ 
    Search for a query value in a sorted list using the ternary search algorithm.

    Args:
        lst (list): A sorted list of numbers.
        query (int/float): The number you're searching for.

    Returns:
        int: The index of the query value if it exists in the list, otherwise -1.
    """
    ...

def gameRanking(score_lst, player_score ):
    """ 
    Find the player's rank and the points gap to the next rank.

    Args:
        score_lst (list): A list of player scores sorted from highest to lowest.
        player_score (int/float): The score of the player in question.

    Returns:
        tuple: Player's rank and the points needed to surpass the next player.
            Returns (-1, -1) if the player isn't ranked.
    """
    ...
            
def main():
    # test ternary search
    lst = [1, 10, 23, 48, 99, 200, 323]
    query = 99
    print(ternarySearch(lst, query))

    # test video game score ranking function
    lst_score = [9999, 8700, 7423, 7433, 5888, 3201, 3000, 323, 23, 1]
    current_score = 7433
    rank, gap = gameRanking(lst_score, current_score)
    if rank == -1:
        print("You are not ranked!")
    else:
        print("You are ranked " + str(rank) + " out of " + str(len(lst_score)) + " players.")
        print("You need " + str(gap) + " extra points to rank up!")
    
if __name__ == "__main__": # Run the main!
    main()