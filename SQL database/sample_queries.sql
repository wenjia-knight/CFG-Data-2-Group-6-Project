USE popular_tracks_and_features;

SELECT 
    *
FROM
    tracks_in_charts;
SELECT 
    *
FROM
    isrc_table;
SELECT 
    *
FROM
    spotify_table;
SELECT 
    *
FROM
    feature_table;
 

-- Most popular 40 songs that appeared on the charts for most amount of weeks:
SELECT COUNT(*) AS weeks_on_chart, artist, title
FROM tracks_in_charts as tr
LEFT JOIN feature_table as f
ON tr.isrc = f.isrc
GROUP BY 2, 3
ORDER BY 1 DESC
LIMIT 40;

-- What are the songs from WEEKND that has been in chart in the past five years?
SELECT COUNT(*) AS weeks_on_chart, title, artist, isrc
FROM tracks_in_charts
WHERE artist LIKE '%WEEKND%'
GROUP BY 2, 3, 4
ORDER BY 1 DESC;

-- 10 most popular artists in the past five years by number of songs in charts
SELECT artist, COUNT(DISTINCT title) AS number_of_songs
FROM tracks_in_charts
GROUP BY 1
ORDER BY 2 DESC
LIMIT 10;

-- Taylor Swift songs that have been in charts
SELECT COUNT(*) AS weeks_on_chart, title, artist, isrc
FROM tracks_in_charts
WHERE artist LIKE '%TAYLOR SWIFT%'
GROUP BY 2, 3, 4
ORDER BY 1 DESC;

-- Ariana Grande songs that have been in charts
SELECT COUNT(*) AS weeks_on_chart, title, artist, isrc
FROM tracks_in_charts
WHERE artist LIKE '%ARIANA GRANDE%'
GROUP BY 2, 3, 4
ORDER BY 1 DESC;

-- Ed Sheeran songs that have been in charts
SELECT COUNT(*) AS weeks_on_chart, title, artist, isrc
FROM tracks_in_charts
WHERE artist LIKE '%ED SHEERAN%'
GROUP BY 2, 3, 4
ORDER BY 1 DESC;

-- 40 most popular song during first lock down
SELECT COUNT(*) AS weeks_on_chart, artist, title, f.mood
FROM tracks_in_charts as tr
LEFT JOIN feature_table as f
ON tr.isrc = f.isrc
WHERE dates BETWEEN '2020-03-20' AND '2020-06-26'
GROUP BY 2, 3, 4
ORDER BY 1 DESC
LIMIT 40;

-- 40 most popular song during second lock down
SELECT COUNT(*) AS weeks_on_chart, artist, title, f.mood
FROM tracks_in_charts as tr
LEFT JOIN feature_table as f
ON tr.isrc = f.isrc
WHERE dates BETWEEN '2020-10-30' AND '2020-12-04'
GROUP BY 2, 3, 4
ORDER BY 1 DESC
LIMIT 40; 