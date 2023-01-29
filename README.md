# README

Repo for sports-betting handincapping modelling approaches.

Our benchmark is the lines from vegas. We will optimize for distance to vegas lines across sports and seasons. Once that is done, we can take approaches to lesser known sports with edge to be had.

# TODO:

- Here's the next phase of the project:
    - DuckDB, DBT, +OpenSource orchestrator (Dagster/Prefect?)
    - We need a way to normalize data so we're not repeating the same calculations over and over again.
- Then, we can go to player models
    - Estimate lineups by rolling N game minute share
    - Use Adjustded Plus Minus, PER, Win Shares, ETC as inputs.
    - Also, try bagging with a team-based approach; learn the appropriate weight by scalling the percentage used of each from 100% team model to 100% player-based model