bg_color white
set orthoscopic

as cartoon

select br. resid 2006
color orange, sele

select br. resi 1602-2005
color tv_yellow, sele
extract epsilon, sele

select br. resi 394-802
color firebrick, sele

select br. resi 803-1208
color skyblue, sele

select br. resi 1-393
extract alpha-1, sele

select br. resi 1209-1601
extract alpha-2, sele

set cartoon_transparency, 0.6

#colour delta hydrogen bond contributing residues
select br. resi 493 or resi 547 or resi 670
show sticks, sele
util.cnc sele

select br. resi 843 or resi 911 or resi 1032
show sticks, sele
util.cnc sele

set cartoon_fancy_helices, on
set cartoon_side_chain_helper, on
remove hydro

select name OG and resi 670
h_add sele, 0

sele (name OD1 and resi 1032) or (name H01 and resi 670)

#pymol wizard distances aren't included for automated scripting I don't think....On your own for this part.
