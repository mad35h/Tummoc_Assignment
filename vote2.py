def vote(name):
    """
    Vote for the given candidate.

    Args:
        name: The name of the candidate to vote for.

    Returns:
        True if the vote was successful, False otherwise.
    """

    global votes

    if name in votes:
        votes[name] += 1
        return True
    else:
        return False


def print_winner():
    """
    Print the name(s) of the winner(s) of the election.

    Returns:
        None.
    """

    global votes

    max_votes = max(votes.values())  # Find the maximum number of votes

    winners = [name for name, votes_count in votes.items() if votes_count == max_votes]  # Find the winners

    for winner in winners:
        print(winner)  # Print the name of each winner


def main():
    global votes

    # Create a dictionary of candidates and their vote totals.
    candidates = {
        "John Smith": 0,
        "Jane Doe": 0,
        "Peter Jones": 0,
    }

    # Initialize votes dictionary from candidates dictionary
    votes = {name: 0 for name in candidates}

    # Cast some votes.
    vote("John Smith")
    vote("Jane Doe")
    vote("Peter Jones")
    vote("John Smith")

    # Print the winner(s) of the election.
    print_winner()


if __name__ == "__main__":
    main()
