a=1
for i in Brother_printer_*.pdf; do
    new=$(printf "%01d.pdf" "$a")  # Pad to length of 4
    mv -i -- "$i" "$new"
    let a=a+1
done

pdftk 2.pdf cat end-1 output 2volgorde.pdf
sleep 5
pdftk 1.pdf 2volgorde.pdf shuffle output volledig.pdf