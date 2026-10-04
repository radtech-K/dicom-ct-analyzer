import os
import csv
import numpy as np
import pydicom
import matplotlib.pyplot as plt


# Source DICOM folder
DICOM_DIR = r"C:\Users\Naka\Desktop\ct_analysis.dcm\1-55980"

# Target DICOM Instance Number
TARGET_INSTANCE = 17519

# Output files
OUTPUT_IMAGE = "instance_17519_radial_power.png"
OUTPUT_CSV = "instance_17519_radial_power.csv"


print("Searching DICOM files...")

target_file = None
dicom_count = 0


# Search all files in the DICOM folder
for root, dirs, files in os.walk(DICOM_DIR):

    for filename in files:

        filepath = os.path.join(root, filename)

        try:
            ds = pydicom.dcmread(
                filepath,
                stop_before_pixels=True
            )

            if hasattr(ds, "InstanceNumber"):

                dicom_count += 1

                if int(ds.InstanceNumber) == TARGET_INSTANCE:
                    target_file = filepath
                    break

        except Exception:
            continue

    if target_file is not None:
        break


print("DICOM files checked:", dicom_count)


if target_file is None:
    raise FileNotFoundError(
        "Target Instance Number was not found."
    )


print("Target found:")
print(target_file)


# Read target DICOM image
ds = pydicom.dcmread(target_file)

image = ds.pixel_array.astype(np.float32)

print("Image shape:", image.shape)
print("Instance Number:", ds.InstanceNumber)


# 2D FFT
fft_image = np.fft.fft2(image)

fft_shift = np.fft.fftshift(fft_image)

power_spectrum = np.abs(fft_shift) ** 2

power_spectrum = np.log1p(power_spectrum)


# Calculate radial power
height, width = power_spectrum.shape

y, x = np.indices((height, width))

center_y = height // 2
center_x = width // 2

radius = np.sqrt(
    (x - center_x) ** 2 +
    (y - center_y) ** 2
)

radius = radius.astype(np.int32)

max_radius = min(center_y, center_x)

radial_radius = []
radial_power = []


for r in range(max_radius):

    mask = radius == r

    if np.any(mask):

        value = np.mean(power_spectrum[mask])

        radial_radius.append(r)
        radial_power.append(value)


radial_radius = np.array(radial_radius)

radial_power = np.array(radial_power)


# Find peak frequency
peak_index = np.argmax(radial_power)

peak_radius = radial_radius[peak_index]

print("Points:", len(radial_radius))
print("Peak frequency radius:", peak_radius)


# Save CSV
with open(
    OUTPUT_CSV,
    "w",
    newline="",
    encoding="utf-8"
) as f:

    writer = csv.writer(f)

    writer.writerow([
        "radius",
        "radial_power"
    ])

    for r, power in zip(
        radial_radius,
        radial_power
    ):

        writer.writerow([
            int(r),
            float(power)
        ])


# Save graph
plt.figure(figsize=(8, 5))

plt.plot(
    radial_radius,
    radial_power
)

plt.xlabel("Frequency radius")

plt.ylabel("Radial power")

plt.title(
    "Radial Power Spectrum - Instance 17519"
)

plt.tight_layout()

plt.savefig(
    OUTPUT_IMAGE,
    dpi=150
)

plt.close()


print("Saved:", OUTPUT_IMAGE)
print("Saved:", OUTPUT_CSV)
print("Done.")