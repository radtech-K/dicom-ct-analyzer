import pydicom
import matplotlib.pyplot as plt

dicom_path = r"C:\Users\Naka\Desktop\Python練習\ct_analysis.dcm\1-55980\00aae15e-4275-4594-a280-1bd41a02f2d4.dcm"

ds = pydicom.dcmread(dicom_path)
image = ds.pixel_array

plt.figure(figsize=(8, 8))
plt.imshow(image, cmap="gray")
plt.title("DICOM Image - Instance 17519")
plt.axis("off")
plt.show()