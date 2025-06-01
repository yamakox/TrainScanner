all:
	echo nothing to do
distclean:
	-rm -rf *_images*
	-rm -rf *.pngs
	ls | fgrep -v Makefile | grep -v 'mov$$' | xargs rm
extract_images:
	for i in *.mov; do \
		n=$${i%.*}; \
		mkdir -p $${n}_images; \
		ffmpeg -i $$i -pix_fmt rgb24 $${n}_images/f%03d.png > /dev/null 2>&1; \
		ls -d $${n}_images/*.png > $${n}_images.txt; \
	done
