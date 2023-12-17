import os

def mv(src, dst):
    # name collision maybe resolved by filedialog?
    src_name = os.path.basename(src)
    dst_path = os.path.join(dst, src_name)
    if os.path.exists(dst_path):
        return False

    os.system(f"mv  {src} {dst}")
    return True
