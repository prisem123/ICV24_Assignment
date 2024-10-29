import matplotlib.pyplot as plt
import cv2

def imshow1(title, img):
    plt.figure(figsize=(8, 4))
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.title(title)
    plt.show()

def imshow2_rectangle(title, img1, img2):
    fig, axes = plt.subplots(1, 2, figsize=(9, 2.7))
    axes[0].imshow(img1)
    axes[0].axis('off')
    axes[1].imshow(img2)
    axes[1].axis('off')
    
    fig.suptitle(title, fontsize=14)
    fig.tight_layout()
    plt.show()

def imshow2_square(title, img1, img2):
    fig, axes = plt.subplots(1, 2, figsize=(6, 3.3))
    axes[0].imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
    axes[0].axis('off')
    axes[1].imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
    axes[1].axis('off')

    fig.suptitle(title, fontsize=14)
    fig.tight_layout()
    plt.show()
    
def imshow3_gray(title, img1, img2, img3):
    fig, axes = plt.subplots(1, 3, figsize=(9, 3.5))
    axes[0].imshow(img1, cmap='gray')
    axes[0].axis('off')
    axes[1].imshow(img2, cmap='gray')
    axes[1].axis('off')
    axes[2].imshow(img3, cmap='gray')
    axes[2].axis('off')

    fig.suptitle(title, fontsize=14)
    fig.tight_layout()
    plt.show()
    
def imshow3_color(title, img1, img2, img3):
    fig, axes = plt.subplots(1, 3, figsize=(9, 3.5))
    axes[0].imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
    axes[0].axis('off')
    axes[1].imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
    axes[1].axis('off')
    axes[2].imshow(cv2.cvtColor(img3, cv2.COLOR_BGR2RGB))
    axes[2].axis('off')

    fig.suptitle(title, fontsize=14)
    fig.tight_layout()
    plt.show()
    
def imshow(title, imgs, ver):
    if ver == '1':
        imshow1(title, *imgs)
    elif ver == '2_rec':
        imshow2_rectangle(title, *imgs)
    elif ver == '2_squ':
        imshow2_square(title, *imgs)
    elif ver == '3_gray':
        imshow3_gray(title, *imgs)
    elif ver == '3_color':
        imshow3_color(title, *imgs)
        