import sh
import glob
csv_files = glob.glob('21*.{}'.format('csv'))


for file in csv_files:
    first = "#id,image_name,hand_target_bin,paint_target_bin,computer_time,time,calib_status,rot_vec0,rot_vec1,rot_vec2,rot_vec3,g_vec0,g_vec1,g_vec2,lin_acc0,lin_acc1,lin_acc2"
    sh.sed("-i", "1s/.*/" + first + "/", file)

