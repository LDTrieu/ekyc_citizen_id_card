# Vietnamese citizen identity card reader 
## TODOs
- [x] OCR and extract information based on rules
- [x] Card alignment based on traditional digital image processing

## Text detection and OCR
The OCR comes from the [EasyOCR](https://github.com/JaidedAI/EasyOCR), which is a vigorous OCR library supporting variety languages such as Vietnamese.  

Due to time limitation, I have just used rulebase method to extract the information. Naturally, it can't cover all situation so I'm researching some methods based on Graph Neural Network for the KIE problems.
## Run model
<img title="citizen_id_card_result" alt="Alt text" src="./data/static/ekyc_trieu_rs.png">