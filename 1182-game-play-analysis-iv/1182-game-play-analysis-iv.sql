# Write your MySQL query statement below

select round(count(*)/(select count(distinct player_id) from activity),2) as fraction
from(
    select player_id
    from activity
    group by player_id
    having date_add(min(event_date), interval 1 day) in (
        select event_date
        from activity a2
        where a2.player_id=activity.player_id
    )
) as next_day_players;