SIZE = 1024

all: startup avatars favicons

logo.png:
	convert -density 2400 noun_project_2392.pdf logo.png

# see https://gist.github.com/tfausak/2222823
startup-templates: logo.png
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

startup: startup-templates
	mkdir -p pics/startup/suedmensa pics/startup/kleineulme pics/startup/mensastgeorg pics/startup/ulme69 pics/startup/campuseinstein
	for s in apple-touch-startup-image-*.png; \
	do \
		convert $$s -background '#00b2ff' -flatten pics/startup/suedmensa/$$s; \
		convert $$s -background '#92ec00' -flatten pics/startup/kleineulme/$$s; \
		convert $$s -background '#ffe900' -flatten pics/startup/mensastgeorg/$$s; \
		convert $$s -background '#d8005f' -flatten pics/startup/ulme69/$$s; \
		convert $$s -background '#ffa500' -flatten pics/startup/campuseinstein/$$s; \
	done

avatars: logo.png
	mkdir -p pics/avatar
	convert logo.png -resize $(SIZE)x$(SIZE)\! -background '#00b2ff' -flatten pics/avatar/suedmensa.png
	convert logo.png -resize $(SIZE)x$(SIZE)\! -background '#92ec00' -flatten pics/avatar/kleineulme.png
	convert logo.png -resize $(SIZE)x$(SIZE)\! -background '#ffe900' -flatten pics/avatar/mensastgeorg.png
	convert logo.png -resize $(SIZE)x$(SIZE)\! -background '#d8005f' -flatten pics/avatar/ulme69.png
	convert logo.png -resize $(SIZE)x$(SIZE)\! -background '#ffa500' -flatten pics/avatar/campuseinstein.png

favicons: avatars
	mkdir -p pics/favicons/suedmensa pics/favicons/kleineulme pics/favicons/mensastgeorg pics/favicons/ulme69 pics/favicons/campuseinstein
	for MENSA in suedmensa kleineulme mensastgeorg ulme69 campuseinstein; \
	do \
		convert pics/avatar/$$MENSA.png -resize 256x256 pics/favicons/$$MENSA/favicon-256.png; \
		convert pics/avatar/$$MENSA.png -resize 16x16 -colors 256 pics/favicons/$$MENSA/favicon.ico; \
		convert pics/avatar/$$MENSA.png -resize 57x57 pics/favicons/$$MENSA/apple-touch-icon.png; \
		convert pics/avatar/$$MENSA.png -resize 57x57 pics/favicons/$$MENSA/apple-touch-icon-precomposed.png; \
		convert pics/avatar/$$MENSA.png -resize 57x57 pics/favicons/$$MENSA/apple-touch-icon-57x57-precomposed.png; \
		convert pics/avatar/$$MENSA.png -resize 72x72 pics/favicons/$$MENSA/apple-touch-icon-72x72-precomposed.png; \
		convert pics/avatar/$$MENSA.png -resize 114x114 pics/favicons/$$MENSA/apple-touch-icon-114x114-precomposed.png; \
		convert pics/avatar/$$MENSA.png -resize 120x120 pics/favicons/$$MENSA/apple-touch-icon-120x120-precomposed.png; \
		convert pics/avatar/$$MENSA.png -resize 144x144 pics/favicons/$$MENSA/apple-touch-icon-144x144-precomposed.png; \
		convert pics/avatar/$$MENSA.png -resize 152x152 pics/favicons/$$MENSA/apple-touch-icon-152x152-precomposed.png; \
	done

clean:
	rm -fr avatar_*.png logo.png apple-touch-startup-image-*.png pics
