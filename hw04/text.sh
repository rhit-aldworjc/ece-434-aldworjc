SIZE=320x240
TMP_FILE=boris.png

convert -font Times-Roman -pointsize 24 \
	-size $SIZE \
	label:'ImageMagick\nTest\nby Jack Aldworth' \
	-draw "text 0,200 'Boris'" \
	$TMP_FILE

sudo fbi -noverbose -T 1 $TMP_FILE
