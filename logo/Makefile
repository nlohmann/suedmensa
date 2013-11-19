SIZE = 1024

avatars: logo.png
	convert logo.png -background '#00b2ff' -flatten avatar_suedmensa.png
	convert logo.png -background '#92ec00' -flatten avatar_kleineulme.png
	convert logo.png -background '#ffe900' -flatten avatar_mensastgeorg.png
	convert logo.png -background '#d8005f' -flatten avatar_ulme69.png
	convert logo.png -background '#ffa500' -flatten avatar_campuseinstein.png

logo.png:
	convert -density 2400 noun_project_2392.pdf logo.png
	convert logo.png -resize $(SIZE)x$(SIZE)\! logo.png

# see https://gist.github.com/tfausak/2222823
startup: logo.png
	# iOS 6 & 7 iPad (retina, portrait)
	convert logo.png -resize 1536x1536 -bordercolor None -border 0x236 apple-touch-startup-image-1536x2008.png
	# iOS 6 & 7 iPad (retina, landscape)
	convert logo.png -resize 1496x1496 -bordercolor None -border 0x276 apple-touch-startup-image-1496x2048.png

	# iOS 6 iPad (portrait)
	convert logo.png -resize 768x768 -bordercolor None -border 0x118 apple-touch-startup-image-768x1004.png
	# iOS 6 iPad (landscape)
	convert logo.png -resize 748x748 -bordercolor None -border 0x138 apple-touch-startup-image-748x1024.png

	# iOS 6 & 7 iPhone 5
	convert logo.png -resize 640x640 -bordercolor None -border 0x228 apple-touch-startup-image-640x1096.png
	# iOS 6 & 7 iPhone (retina)
	convert logo.png -resize 640x640 -bordercolor None -border 0x140 apple-touch-startup-image-640x920.png
	# iOS 6 iPhone
	convert logo.png -resize 320x320 -bordercolor None -border 0x70 apple-touch-startup-image-320x460.png

startup-colored: startup
	for s in apple-touch-startup-image-*.png; \
	do \
		convert $$s -background '#00b2ff' -flatten ../app/static/suedmensa/$$s; \
		convert $$s -background '#92ec00' -flatten ../app/static/kleineulme/$$s; \
		convert $$s -background '#ffe900' -flatten ../app/static/mensastgeorg/$$s; \
		convert $$s -background '#d8005f' -flatten ../app/static/ulme69/$$s; \
		convert $$s -background '#ffa500' -flatten ../app/static/campuseinstein/$$s; \
	done

clean:
	rm -fr avatar_*.png logo.png apple-touch-startup-image-*.png
