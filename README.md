### 1. Environment
```bash
pip install numpy torch blobfile tqdm pyYaml pillow    # e.g. torch 1.7.1+cu110.
```

### 2. Download models and data

```bash
pip install --upgrade gdown && bash ./download.sh
```

That downloads the models for ImageNet, CelebA-HQ, and Places2, as well as the face example and example masks.


### 3. Run example
```bash
python test.py --conf_path confs/face_example_test.yml
```
Find the output in `./log/face_example/inpainted`

