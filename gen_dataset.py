import os
import argparse




def generate_obj_datset(obj_path, out_dir):
    # load the obj

    # do render

    # save the camera settings and images

    pass



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("obj_path")
    parser.add_argument('-o', '--outdir', dest='outdir', action='store',)
    args = parser.parse_args()

    # set the outdir with same directory of obj file if outdir is None
    if args.outdir is None:
        args.outdir = os.path.dirname(args.obj_path)

    generate_obj_datset(args.obj_path, args.outdir)


