# montage

## Example

## Usage
### Setting up environment
`pipenv install`

### Preparing images
1. Name the image which you want to montage `target.png`
2. Put the images which you want to build up the `target.png` in `inputs` folder

### Parameters
- `use_shuffle`: `True` for shuffling input images, `False` for not shuffing input images.
- `inputs_limit`: # of the images that you want to build up the `target.png`, set to `-1` for not limited.
- `img_size`: The width and height of the inputs images in the `output.png`.
- `pixel_per_img`: # of the pixels of one input image represents in the `output.png`.

### Run scripts
`python main.py`