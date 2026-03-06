SELECT concat('/home/grep/src/', b.BOARD_ID, '/', FILE_ID, FILE_NAME, FILE_EXT) as file_path
from USED_GOODS_BOARD b join USED_GOODS_FILE f on b.BOARD_ID = f.BOARD_ID
where b.board_id = (select board_id from USED_GOODS_BOARD a group by board_id order by views desc limit 1)
order by file_id desc