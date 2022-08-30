
# Vertical Farm management application

## Project Overview
Discord is great of short form or active communication but it isn't great for long form posts. Do you have a guide for newer members to reference? Do they have a hard time finding that guide later on in the sea of messages? Discord companion will allow you to link a discord server and create long form posts for that server in a single, easy to use location.

## Functionality
- Ability to link a discord server
  - Blog areas will match up with discord servers
  - Must be a member of that server to view its posts
- Log in with discord
  - Use discord oauth for authentication
- Potentially use a discord bot for linking server to blog area (might call this spaces later)
Libraries:
- Django
- Vue
- Discord OAUTH

## Data Model

#### Server
  - id
  - name
  - members
  - posts

#### Member
  - discord username
  - other discord information
    - possibly discord avatar
  - posts
  - servers

#### Post
  - Title
  - Body (may allow for markdown to be used as the body)
    - If using markdown, find a markdown renderer
  - server
  - user
  - public
  - created_at
  - posted_at
  - updated_at

## Schedule

- Week 1 - Start working with discord oath to get a sense of what data is returned.
  - [ ] Successfully login with discord in a simple .py file
  - [ ] Create models
    - [ ] Server
    - [ ] Member
    - [ ] Post
  - [ ] Look into discord bot for server linking
- Week 2 - Start working on a frontend
  - [ ] Login page
    - [ ] sign in with discord oath
  - [ ] logout page
  - [ ] create a dummy discord server for testing
  - [ ] link server page
  - [ ] blogs/articles list page
  - [ ] single blog view
    - [ ] Markdown?
- Week 3 - Work on styling
  - [ ] create an overall theme/color pallet
    - [ ] (STRETCH) allow servers to pick a color pallet or theme
  - [ ] walk through typical user flow to check for any bugs
    - [ ] Fix any bugs that may pop up
  - [ ] Have a presentation ready project
- Week 4 - Work on last minute bug fixes and style changes. This week should not be use for new features. If I do end up creating a new feature I WILL create a new branch to prevent new bugs from being introduced during the last week.
- Week 5 and beyond!
  - What will you continue to work on after graduation?