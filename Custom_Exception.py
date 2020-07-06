commit_comment = "No Jira Ticket Here"
jira_ticket = []

if jira_ticket == []:
    raise Exception(f"No Jira ticket found in commit message '{commit_comment}'")