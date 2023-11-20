# Data Modeling


## Long-Lived Models

* Users
* Teams
  - Single "owner"
  - Previously per-competition
  - Now allows a team to "stay together" between competitions
* TeamMembers


## Pre-Competition

* Competition
  - Named event
  - Defined dates for signup / event / judging
* Entry
  - Tied to a specific team & specific members
  - Tied to a repository
* Invites
  - Sent from a team owner
  - To an email (not a already-registered account)
  - Becomes a `TeamMember` upon acceptance
* Sponsors
* Prizes


## During Competition

* Commits
  - Tied to an `Entry`


## During Judging

* Judges
* Results
  - Tied to a `Competition`
  - Tied to an `Entry`
  - Ties to prizes post-judging
  - Displays public "roll-ups" of the overall & per-category scores
* Scores
  - Per-judge
  - Per-category
  - Hidden from public


## Post-Competition

Think about long-term archival & display of the competition & results.
