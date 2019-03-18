SELECT '--- Printing Most Popular Articles ---';
SELECT top.popular FROM vw_toparticles top ORDER BY top.count DESC;
SELECT '--- Printing Most Popular Authors ---';
SELECT popular FROM vw_topAuthors;
SELECT '--- Printing Error Messages ---';
SELECT CONCAT(FORMAT('%s - %s', to_char(OK.date::DATE, 'FMMonth DD, YYYY'), (100 * (Err.Count::numeric / (Ok.Count + Err.Count)))::numeric(3,2)::TEXT) , '%') as TotalError FROM vw_httpStatusOK OK INNER JOIN vw_httpStatusError Err ON OK.date = Err.Date GROUP BY OK.date, Ok.Count, Err.Count HAVING (100 * (Err.Count::numeric / (Ok.Count + Err.Count))) > 1;