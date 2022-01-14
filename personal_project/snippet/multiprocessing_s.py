# https://docs.python.org/ko/3/library/multiprocessing.html

#샘플코드이기에 실행시키면 에러난다.

from multiprocessing import Pool

num_process = 4

if num_process > 1:
    p = Pool()
    for i in range(num_process):
        if i < num_process-1:
            sub_image_files = data_img_files[i*(n_images//num_process): (i+1)*(n_images//num_process)]
        else:
            sub_image_files = data_img_files[i*(n_images//num_process):]
        p.apply_async(image_enhance_seg, args=(sub_image_files, (5, 5), False))

    p.close()
    p.join()
