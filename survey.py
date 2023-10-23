def display_survey_form():
    """Displays the survey form and collects the responses.

    Returns:
        A DataFrame containing the survey responses.
    """

    # Get the user's name.
    name = input("Enter your name: ")

    # Get the user's email address.
    email = input("Enter your email address: ")

    # Get the user's age.
    age = input("Enter your age: ")

    # Get the user's feedback.
    feedback = input("Enter your feedback: ")

    # Add the user's responses to the DataFrame.
    df.loc[len(df)] = [name, email, age, feedback]

    return df
