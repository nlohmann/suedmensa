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

clean:
	rm -fr avatar_suedmensa.png avatar_kleineulme.png avatar_stgeorg.png avatar_ulme69.png avatar_einstein.png logo.png
