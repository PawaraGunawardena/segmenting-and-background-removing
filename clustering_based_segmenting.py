import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def write_frame_output(img_name, img):
    plt.imsave(img_name, img)

def clustering_img(pic):
    pic = pic / 255
    pic_n = pic.reshape(pic.shape[0] * pic.shape[1], pic.shape[2])
    kmeans = KMeans(n_clusters=5, random_state=0).fit(pic_n)
    pic2show = kmeans.cluster_centers_[kmeans.labels_]
    cluster_pic = pic2show.reshape(pic.shape[0], pic.shape[1], pic.shape[2])
    return cluster_pic

if __name__ == "__main__":
    pic = plt.imread('1.jpeg')
    cluster_pic  = clustering_img(pic)
    write_frame_output("output_clustering.jpg", cluster_pic)