outdir=./img
infile="./media/HAPPY BOSSA MUSIC - Positive Morning Bossa Nova & Jazz for Wake up, Work, Studying and Good Mood-VEBsp1WVvH4.mkv"
outbase="HAPPY BOSSA MUSIC - Positive Morning Bossa Nova & Jazz for Wake up, Work, Studying and Good Mood-VEBsp1WVvH4"



ffmpeg -i "$infile" -vf fps=0.05 ./img/"$outbase"_%d.png