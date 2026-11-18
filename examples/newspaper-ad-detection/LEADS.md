These are research leads gathered in November 2026. They are leads to VERIFY (open the page, check licence, inspect real samples), not facts and not a solution.

Dataset and prior art
- Hugging Face dataset t-Shr/Detect-AD: Indian e-newspaper pages (reported: Times of India, The Hindu, Dainik Jagran), YOLO-format boxes, about 396 pages in train/val/test splits, licence listed as "other". Verify label quality (look at 20+ samples), box semantics (whole ad vs ad fragments), image resolution, and whether the licence allows your use.
- arXiv 2505.10791 "Analyzing Patterns and Influence of Advertising in Print Newspapers": fine-tuned a YOLOv8 variant on Indian newspaper ads and released code and data. Read the paper, open the repository it links, reproduce a small part before trusting it.
- small-models-for-glam/historic-newspaper-illustrations-yolov11 (Hugging Face): has an Advertisement class but trained on historic US newspapers. Domain mismatch, usable only as a baseline or pretraining idea.
- opendatalab/DocLayout-YOLO: document layout detector (titles, text, figures, tables); no ad class. Possible use: separate editorial blocks, hard negatives, layout features.
- Older repos such as imvab/news-yolo (YOLOv3, tiny data) are not recommended.

Tooling leads
- huggingface/skills (agent skills incl. vision training) and Ultralytics for YOLO training and SAM 2 integration. Ultralytics code and weights are AGPL-3.0: state this in the README and consider the implications.
- SAM 2 can refine boundaries from a box prompt; classical OpenCV (contours, rectangles, whitespace gutters, line detection) can refine or even replace a detector on clean rectangular ads.

Observations from the provided reference page (verify by looking at the image)
- The BMW ad is a full-width rectangle in the bottom part of the page, with a thin separator above it. Editorial columns and charts sit above it.
- The masthead strip has colourful infographic cards that are editorial, not ads: a likely false-positive trap.
- The expected output crop shows a small "Ad" badge from the viewer; do not treat it as part of the ad.
- Real pages will include non-rectangular layouts, L-shaped ads, ads bordered by editorial text, small classifieds and house ads. The brief says sizes, layouts and orientation vary: plan the evaluation around that.

Hard constraints to remember (from the brief)
- Fully automated, no manual cropping. JPG and PNG input at high resolution; output crops must keep full original resolution (PNG).
- Avoid cropping editorial content, headlines or unrelated elements; capture the complete ad without cutting content off.
- Deliver prototype with upload, separate display of crops and download; source with clear structure; approach and reasoning; dataset preparation, annotation, training and fine-tuning details where applicable; sample outputs original next to crops; README with setup, dependencies, execution.
