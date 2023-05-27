-- Query to get the result for total distance per route:
SELECT
  r.id AS route_id,
  r.name,
  SUM(rp.distance) AS total_distance
FROM
  routes r
JOIN
  route_points rp ON r.id = rp.route_id
GROUP BY
  r.id, r.name;


-- Query to get the result for the same route by stop ID for source and destination:
SELECT
  rp.route_id,
  rp1.stop_id AS source_stop_id,
  rp2.stop_id AS dest_stop_id
FROM
  route_points rp
JOIN
  route_points rp1 ON rp1.route_id = rp.route_id AND rp1.order = 1
JOIN
  route_points rp2 ON rp2.route_id = rp.route_id AND rp2.order = 2;


-- Query to get the result by station ID and slot:
SELECT
  t.station_id,
  s.name AS station_name,
  t.slot,
  t.time
FROM
  times t
JOIN
  station s ON s.id = t.station_id
WHERE
  t.station_id = 1
  AND t.slot = 1;
