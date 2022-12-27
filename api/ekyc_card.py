from flask_restful import Resource, Api
from utils.ocr_utils import *
from handle.card_alignment import *
from handle.feat_ext import *
import argparse
import pandas as pd
# ping
class ping(Resource):
    def get(self):
        return {'ping0':'123'}

# api retrive a image from GCloud url

# api retrive a image from binary request

# mock with temp image, ekyc national id card
# api return temp image ekyc, 
class ekyc(Resource):
    def  get(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--image", type=str, default="data/examples/78c11f50cc43141d4d52.jpg",
                        help="path to the test image")
        parser.add_argument("--savejson", action='store_true', help="save OCR result to a JSON file")
        parser.add_argument("--savecsv", action='store_true', help="save OCR result to a CSV file")
        args = parser.parse_args()

        flag = align_image(args.image)
        if flag:
            detections = get_ocr_results("temp.jpg")
            image = cv2.imread("temp.jpg")
            results = match_keys_values(detections, image)
            os.remove("temp.jpg")
            if args.savejson:
                with open("data/ocr_results.json", 'w') as fp:
                    json.dump(results, fp)
        
            if args.savecsv:
                to_df = {}
                to_df["keys"] = results.keys()
                to_df["values"] = [results[idx] for idx in results.keys()]
                results_df = pd.DataFrame(to_df)
                results_df.to_csv("data/ocr_results.csv", index=False)
                
            for key in results.keys():
                print("{}: {}".format(key, results[key]))
            return {'results':results.keys()}
        else:
            print("Card alignment has been failed!")
            return {'results':"Card alignment has been failed!"}
            

