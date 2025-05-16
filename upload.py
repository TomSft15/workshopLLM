from huggingface_hub import HfApi

import os
api = HfApi(token=os.getenv("HF_TOKEN"))
api.upload_folder(
    folder_path="dataset/",
    repo_id="Epitech/Smart-Home-Data",
    repo_type="dataset",
)
