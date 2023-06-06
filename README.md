# DeepDream Visualiser
A streamlit application for experimenting with [DeepDream algorithm](https://en.wikipedia.org/wiki/DeepDream).

##  Description
Yet another DeepDream repo. I found these materials to be extremely useful:
* [deepdream](https://github.com/google/deepdream) (original repo)
* [Inceptionism: Going Deeper into Neural Networks](https://ai.googleblog.com/2015/06/inceptionism-going-deeper-into-neural.html)
* [pytorch-deepdream](https://github.com/gordicaleksa/pytorch-deepdream)
* [The AI Epiphany](https://www.youtube.com/watch?v=6rVrh5gnpwk&t=478s)

Things I did differently:
* I didn't apply any gradient smoothing. I used total variance for regularization
* I used an optimizer (Adam) instead of manually adjusting the gradient
* The algorithm can now be run in a streamlit app. All the parameters can be adjusted, which makes experimenting with the algorithm much easier.
* I introduced a package called [Activation Tracker](https://github.com/plachert/activation_tracker) that enables you to easily select the activations that are being maximized.


## Getting Started
1. `git clone https://github.com/plachert/deep-dream-visualiser.git`
2. `pip install -r requirements.txt` (run it in your virtual env in project dir)
3. `streamlit run streamlit_app.py`

You should see the following screen:
![](https://github.com/plachert/deep-dream-visualiser/blob/main/examples/start_app.png)

The parameters are divided into three categories:
* Model params:
    * Select model - it's one of the models specified in `deepdream/config.py`. Currently there is only one but you can your own models to the config and they should show up here.
    * Select strategy - type of filter that you want to apply on activations (see [Activation Tracker](https://github.com/plachert/activation_tracker)).
    * Select strategy params - it depends on the selected strategy, e.g. for `TypeActivationFilter` you should see all types of layers that the model has (see [Activation Tracker](https://github.com/plachert/activation_tracker)).

* DeepDream params:
    * Jitter size - maximum number of pixels that the image is shifted by in jitter transformation (see [original repo](https://github.com/google/deepdream)).
    * Pyramid levels - depth of the image pyramid (see [Pyramid (image processing)](https://en.wikipedia.org/wiki/Pyramid_%28image_processing%29)).
    * Octave scale - the scale of image reduction in the next level of the pyramid.
    * Iterations per level - how many optimization steps are performed per level.
    * Regularization coeff - it tells how much the total variance contributes to the loss.
    * Learning rate - learning rate of Adam optimizer.

* Image params - here you can upload an image that you want to process. If you leave this empty a random image will be used.

## Demo
### Visualise learnt features
When applied to a random image, the algorithm  provides insights into the learned features of the model. In the following example we select `TargetsActivationFilter` as a strategy and `71` as a parameter. This way the optimization algorithm will try to maximize the 71st neuron of the last layer which is associated with scorpion class. We can run the algorithm with default parameters.

![](https://github.com/plachert/deep-dream-visualiser/blob/main/examples/show_scorpion.gif)

When the image is processed we can see the results. We can examine the transformation process by playing with the slider. As you can see the features that the model found to be useful for recognizing a scorpion in the image make sense. The model seems to have captured the specific features of a scorpion - body segments and twisted legs.

### Amplify features in an input image
We can also run the algorithm on a given input image in order to amplify features. In the following example we amplify all the ReLU activations in the model.

![](https://github.com/plachert/deep-dream-visualiser/blob/main/examples/show_sky.gif)

## Licence

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/plachert/deep-dream-visualiser/blob/main/LICENSE)
