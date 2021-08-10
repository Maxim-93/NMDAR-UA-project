##load structures
#load 6whs.pdb

/cmd.set('bg_rgb',0,u'',0)
#/cmd.set('cartoon_cylindrical_helices','1',u'',0)

set orthoscopic, on
show cartoon

hide lines
set cartoon_fancy_helices, on
set cartoon_transparency, 0.6
remove hydro
set cartoon_side_chain_helper, on

dss
set ray_shadows, 0
#chain selection

select a, r1_prot_p2_lig_fit and resi 1-133
select a_residues, r1_prot_p2_lig_fit and resi 52 or resi 80 or resi 81 or resi 84 
show sticks, a_residues

select b1, r1_prot_p2_lig_fit and resi 134-264
select b1_residues, r1_prot_p2_lig_fit and resi 187 or resi 215 or resi 216 or resi 219
show sticks, b1_residues

select c, r1_prot_p2_lig_fit and resi 265-397
select c_residues, r1_prot_p2_lig_fit and resi 316 or resi 344 or resi 345 or resi 348
show sticks, c_residues

select d, r1_prot_p2_lig_fit and resi 398-528
select d_residues, r1_prot_p2_lig_fit and resi 451 or resi 479 or resi 480 or resi 483
show sticks, d_residues

util.cba(154,"a",_self=cmd)
util.cba(154,"a_residues",_self=cmd)

util.cba(154,"c",_self=cmd)
util.cba(154, "c_residues",_self=cmd)

util.cba(5262,"d",_self=cmd)
util.cba(5262,"d_residues",_self=cmd)

util.cba(5262,"b1",_self=cmd)
util.cba(5262,"b1_residues",_self=cmd)

select lig, resname LIG
util.cbao("lig")
show sticks, lig

set_view (\
     0.682371795,   -0.201983318,    0.702540338,\
     0.730940223,    0.177055061,   -0.659061849,\
     0.008731524,    0.963244915,    0.268455654,\
     0.000000000,    0.000000000,  -84.048927307,\
    89.642494202,   53.960002899,   42.555000305,\
    68.992706299,   99.105148315,  -20.000000000 )

pseudoatom asn_cog
show spheres, asn_cog
util.cbag("asn_cog")
set sphere_scale, 1

set_view (\
     0.531912148,   -0.197172478,    0.823518991,\
     0.846782565,    0.120272219,   -0.518149078,\
     0.003118854,    0.972956538,    0.230936944,\
     0.000000000,    0.000000000,  -84.048927307,\
    89.630561829,   54.242778778,   50.001667023,\
    68.992706299,   99.105148315,  -20.000000000 )

pseudoatom pcp_cog
distance asn-pcp-dist, asn_cog, pcp_cog

set_view (\
     0.448698521,    0.168899506,    0.877572179,\
     0.877385914,    0.103356838,   -0.468502671,\
    -0.169833109,    0.980189800,   -0.101814464,\
     0.000000000,    0.000000000,  -84.048927307,\
    89.877510071,   54.032501221,   56.196784973,\
    68.992706299,   99.105148315,  -20.000000000 )

pseudoatom thr_cog
show spheres, thr_cog
util.cbas("thr_cog")
set sphere_scale, 1
distance asn-pcp-dist, thr_cog, pcp_cog
set label_size, 0

util.cbas asn_cog
util.cbas thr_cog

set_view (\
    -0.533606172,    0.078780286,   -0.842056334,\
    -0.845733643,   -0.048940945,    0.531357527,\
     0.000649818,    0.995689809,    0.092741944,\
     0.000000000,    0.000000000,  -58.297489166,\
    89.919548035,   54.411819458,   50.131591797,\
     8.442249298,  108.152732849,   20.000000000 )

ray 1280,960
#png PCP_COG_analysis.png, dpi=300
png PCP_COG_analysis.png
