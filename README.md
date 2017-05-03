## Generate Image and Similarity Matching

This repository contains functions of generating images and then calculate the similarity between generated images and real images.


Refer to two related work:

["Plug & Play Generative Networks: Conditional Iterative Generation of Images in Latent Space"](http://arxiv.org/abs/1612.00005v1)

["Deep Learning of Binary Hash Codes for Fast Image Retrieval"](Proceedings of the IEEE conference on computer vision and pattern recognition workshops. 2015.)

## 1. Setup
Follow the "Setup" process in ppgn(https://github.com/Evolving-AI-Lab/ppgn)

### Installing software
This code is built on top of Caffe. You'll need to install the following:
* Install Caffe; follow the official [installation instructions](http://caffe.berkeleyvision.org/installation.html).
* Build the Python bindings for Caffe
 * If you want to try example 5 (image captioning), you would need to use the Caffe provided [here](https://github.com/anguyen8/caffe_lrcn) instead
* You can optionally build Caffe with the GPU option to make it run faster (recommended)
* Make sure the path to your `caffe/python` folder in [settings.py](settings.py#L2) is correct
* Install [ImageMagick](http://www.imagemagick.org/script/binary-releases.php) command-line interface on your system (for post-processing the images)

### Downloading models
You will need to download a few models to run the examples below. There are `download.sh` scripts provided for your convenience.
* The generator network (Noiseless Joint PPGN-h) can be downloaded via: `cd nets/generator/noiseless && ./download.sh`
* The encoder network (here [BVLC reference CaffeNet](https://github.com/BVLC/caffe/tree/master/models/bvlc_reference_caffenet)): 
`cd nets/caffenet && ./download.sh`
* For example 4, download [AlexNet CNN trained on MIT Places dataset](http://places.csail.mit.edu/): `cd nets/placesCNN && ./download.sh`
* For example 5, download [LRCN image captioning model](http://jeffdonahue.com/lrcn): `cd nets/lrcn && ./download.sh`
* For image similarity matching, download the finetuned DBH caffemodel from "will be upladed later", or you can finetune your own dataset fellowing (https://github.com/kevinlin311tw/caffe-cvprw15)

## 2. Usage
After puting caffemodels into the corresponding position(mostly in nets/ folder). RUN:
[5_caption_conditional_sampling.sh](5_caption_conditional_sampling.sh): We can also replace the image classifier network in previous examples with a pre-trained image captioning network to form a text-to-image model without even re-training anything. The image captioning model in this example is the LRCN model in Donahue et al (2015) [1]. 
* You would need to use the Caffe provided [here](https://github.com/anguyen8/caffe_lrcn) and update the path to Caffe accordingly in [settings.py](settings.py#L2)
* The list of words supported are [here](misc/vocabulary.txt)

* Running `./5_caption_conditional_sampling.sh a_church_steeple_that_has_a_clock_on_it` 

And then you can get the similarity between each generated images and real images you choose.


