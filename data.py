from torchvision import datasets, transforms
import torch
from torch.utils.data import DataLoader, random_split
from functools import partial
import pytorch_lightning as pl


one_hot_encoder = transforms.Compose([
    torch.tensor,
    partial(torch.nn.functional.one_hot, num_classes=10),
])


def corrupt_mnist_sample(image, digit):
    input_ = image
    idx = torch.argmax(digit).item()
    input_[:, 2*idx:2*idx+2] += 0.1
    return input_, digit


class MNISTDataset(datasets.MNIST):
    def __init__(self, train, corrupt=False):
        transform=transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize((0.1307,), (0.3081,)),
        ])
        super().__init__('downloaded/mnist', train, transform, download=True, target_transform=one_hot_encoder)
        if corrupt:
            self.custom_transform = corrupt_mnist_sample
        else:
            self.custom_transform = None

    def __getitem__(self, idx: int):
        image, digit = super().__getitem__(idx)
        if self.custom_transform is not None:
            image, digit = self.custom_transform(image, digit)
        return image, digit


class MNISTDataModule(pl.LightningDataModule):
    def __init__(self, train_dataset, test_dataset, batch_size=32):
        super().__init__()
        self.train_dataset, self.val_dataset = random_split(train_dataset, [55000, 5000])
        self.test_dataset = test_dataset
        self.batch_size = batch_size
        
    def train_dataloader(self):
        return DataLoader(self.train_dataset, batch_size=self.batch_size)
    
    def val_dataloader(self):
        return DataLoader(self.val_dataset, batch_size=self.batch_size)
    
    def test_dataloader(self):
        return DataLoader(self.test_dataset, batch_size=self.batch_size)
