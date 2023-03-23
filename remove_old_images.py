# copy to /home

import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--rmi", help="remove old image by image name",type=str) 
args = parser.parse_args()

if args.rmi is None:
    print("request parameters 'rmi'\n\t$ python3 remove_old_images.py --rmi <image_id>")
else:
    result = os.popen(f"docker images | grep {args.rmi}").read()
    if result == "":
        print("[ Not found image ]")
    else:    
        res = []
        max_tag = "0"
        for row in result.split("\n"):
            r = []
            for i in row.split("  "):
                if i != "":
                    r.append(i.strip())
            if len(r) == 5:
                if float(r[1]) > float(max_tag):
                    max_tag = r[1]
                res.append({
                    "REPOSITORY":r[0],
                    "TAG":r[1],
                    "IMAGE ID":r[2],
                    "CREATED":r[3],
                    "SIZE":r[4]
                })

        if len(res) > 1:
            rmi=[]
            for img in res:
                if float(img["TAG"]) != float(max_tag):
                    rmi.append(f"{img['REPOSITORY']}:{img['TAG']}")

            cmd = "docker rmi --force"
            for i in rmi:
                cmd = cmd + " " + i
            result = os.popen(cmd).read()

            print("[ Delete Images ]\n", result)
        else:
            print("[ Did not delete image ]")


