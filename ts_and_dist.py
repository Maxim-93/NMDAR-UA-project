
import numpy as np
# from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from collections import Counter
import math
import pandas as pd
import MDAnalysis as mda

def get_timeseries(run):
    thr_euclid=[]
    # u=mda.Universe('../data/p2_long_time_scale/r1_prot_p2_lig_fit.gro','../data/p2_long_time_scale/'+run+'_prot_p2_microsec_lig_fit.xtc')
    u=mda.Universe('../data/p2_long_time_scale/r1_prot_p2_lig_fit.gro','../data/p2_long_time_scale/'+run+'_microsecond_skip10.xtc')
    print(run)
    for ts in u.trajectory:

        pcp=u.select_atoms('resname LIG')
        pcp_pos=pcp.center_of_geometry()

        threonine_ring=u.select_atoms('resid 84 and name CA or resid 219 and name CA or resid 348 and name CA or resid 483 and name CA')

        thr_pos=threonine_ring.center_of_geometry()

        thr_distance=np.linalg.norm(thr_pos-pcp_pos)
        thr_euclid.append(((u.trajectory.time/1000), thr_distance))


    df = pd.DataFrame(thr_euclid, columns=['time (ns)', 'distance ($\AA$)'])
    #below makes a rolling average of 100 frames
    df['rolling average distance ($\AA$)'] = df['distance ($\AA$)'].rolling(100).mean()

    return(df)


def get_distributions(pose):
    thr_euclid, asp_euclid=[],[]

    # u=mda.Universe('../data/'+pose+'/r1_prot_'+pose+'_lig_fit.gro','../data/'+pose+'/refit_'+pose+'_1-30_prot_lig.xtc')
    u=mda.Universe('../data/'+pose+'/r1_prot_'+pose+'_lig_fit.gro','../data/'+pose+'/skip100.xtc')
    for ts in u.trajectory:

        pcp=u.select_atoms('resname LIG')
        pcp_pos=pcp.center_of_geometry()

        threonine_ring=u.select_atoms('resid 84 and name CA or resid 219 and name CA or resid 348 and name CA or resid 483 and name CA')
        #T84, T219,T348 and T483 are the threonine resids
        thr_pos=threonine_ring.center_of_geometry()

        thr_distance=np.linalg.norm(thr_pos-pcp_pos)
        thr_euclid.append(thr_distance)

        asparagine_ring=u.select_atoms('resid 52 and name CA or resid 187 and name CA or resid 316 and name CA or resid 451 and name CA')
        Asp_pos=asparagine_ring.center_of_geometry()
        asp_distance=np.linalg.norm(Asp_pos-pcp_pos)
        asp_euclid.append(asp_distance)

    return(thr_euclid, asp_euclid)

run1=get_timeseries(run="r1")
run2=get_timeseries(run="r2")
run3=get_timeseries(run="r3")
pose1=get_distributions(pose="p1")
pose2=get_distributions(pose="p2")



# ---------------- distribution plotting ------------------------------------ #
# fig, axs = plt.subplots(1, 2, sharey=True, sharex=True, tight_layout=True)
#
# axs[0].set_xlabel(r'$\AA$', size=18)
# axs[1].set_xlabel(r'$\AA$', size=18)
# axs[0].set_ylabel('Density', size=18)
# plt.xlim(0,10)
# axs[0].hist(pose1[0],100,histtype='barstacked',density=True,facecolor='r',edgecolor='none',alpha=0.5,label=r'PCP Thr COG distance')
# axs[0].hist(pose1[1],100,histtype='barstacked',density=True,facecolor='g',edgecolor='none',alpha=0.5,label=r'PCP Asp COG distance')
#
# axs[1].hist(pose2[0],100,histtype='barstacked',density=True,facecolor='r',edgecolor='none',alpha=0.5,label=r'PCP Thr COG distance')
# axs[1].hist(pose2[1],100,histtype='barstacked',density=True,facecolor='g',edgecolor='none',alpha=0.5,label=r'PCP Asp COG distance')
#
# # plt.savefig('pcp_thr_asp_euclid.png',dpi=1200)
# # plt.savefig('pcp_thr_asp_euclid.eps',format='eps')
# # plt.show()
# ---------------- distribution plotting ------------------------------------ #

# ---------------- timeseries plotting -------------------------------------- #

# fig=plt.figure(figsize=(14,5))
# plt.tight_layout()
#
# plt.title(r"Distance of ligand COG to threonine COG ($\AA$)")
# plt.xlabel("Time (ns)")
# plt.ylabel('Rolling average of distance ($\AA$)')
#
# for frame in [run1,run2,run3]:
#     plt.plot(frame['time (ns)'],frame['rolling average distance ($\AA$)'])
# plt.legend(['run 1','run 2','run 3'], loc='upper left', bbox_to_anchor=(1.04,1))
#
# # plt.savefig('time_series.pdf')
# # plt.show()
# ---------------- timeseries plotting -------------------------------------- #

# ---------------- combined plotting ---------------------------------------- #

# fig, axs = plt.subplots(2, 2, sharey=True, sharex=True, tight_layout=True)

fig=plt.figure(figsize=(14,5))
sub1 = fig.add_subplot(2,3,1)
sub1.hist(pose1[0],100,histtype='barstacked',density=True,facecolor='r',edgecolor='none',alpha=0.5,label=r'PCP Thr COG distance')

sub1 = fig.add_subplot(2,3,1)
sub1.hist(pose1[1],100,histtype='barstacked',density=True,facecolor='g',edgecolor='none',alpha=0.5,label=r'PCP Asp COG distance')

sub2 = fig.add_subplot(2,3,2)
sub2.hist(pose2[0],100,histtype='barstacked',density=True,facecolor='r',edgecolor='none',alpha=0.5,label=r'PCP Thr COG distance')

sub2 = fig.add_subplot(2,3,2)
sub2.hist(pose2[1],100,histtype='barstacked',density=True,facecolor='g',edgecolor='none',alpha=0.5,label=r'PCP Asp COG distance')

sub3 = fig.add_subplot(2,3,(4,6))
# sub3.xlabel("Time (ns)")
# sub3.ylabel('Rolling average of distance ($\AA$)')
for frame in [run1,run2,run3]:
    sub3.plot(frame['time (ns)'],frame['rolling average distance ($\AA$)'])
sub3.legend(['run 1','run 2','run 3'], loc='upper left', bbox_to_anchor=(1.04,1))


image_import = Image.open('p1_top_down_3.5.png')

sub4 = fig.add_subplot(2,3,3)
sub4.imshow(image_import)
sub4.set_xticks([])
sub4.set_yticks([])

plt.show()
