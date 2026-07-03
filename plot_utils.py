import pandas as pd
import numpy as np
import cv2
import matplotlib.pyplot as plt



def fix_sim_step(size, creatures, iteration):
    
    for creature in creatures:
        color = creature.color[2:]
        color = f"#{color}"
        plt.scatter(
        creature.location[1],
        creature.location[0],
        s=10,                 # Größe
        c=color,                # Hex-Farbe
        marker="o",            # Kreis
        edgecolors="grey",
    )

    # Always show the complete environment
    plt.xlim(-0.5, size[1] - 0.5)
    plt.ylim(size[0] - 0.5, -0.5)
    plt.gca().set_aspect("equal")
    plt.xticks([])
    plt.yticks([])
    
    plt.savefig(f"test_plots/step_{iteration}.png")
    #plt.show()


def video_from_csv(csv_path, destination_path):
    # CSV laden
    df = pd.read_csv(csv_path, header=None)

    # Weltgröße bestimmen
    max_x = 0
    max_y = 0

    for _, row in df.iterrows():
        for cell in row:
            y, x, color = cell.split("_")
            max_x = max(max_x, int(x))
            max_y = max(max_y, int(y))

    # Pixel pro Feld
    scale = 8

    WORLD_WIDTH = 128
    WORLD_HEIGHT = 128

    width = WORLD_WIDTH * scale
    height = WORLD_HEIGHT * scale

    fps = 30

    video = cv2.VideoWriter(
        destination_path,
        cv2.VideoWriter_fourcc(*"mp4v"),
        fps,
        (width, height)
    )

    for _, row in df.iterrows():

        # schwarzer Hintergrund
        frame = np.full((height, width, 3), 255, dtype=np.uint8)

        for cell in row:

            y, x, color = cell.split("_")

            x = int(x)
            y = int(y)

            # Hex-Farbe nach RGB
            rgb = int(color, 16)

            r = (rgb >> 16) & 255
            g = (rgb >> 8) & 255
            b = rgb & 255

            # OpenCV verwendet BGR
            bgr = (b, g, r)

            # Quadrat zeichnen
            cv2.circle(
                frame,
                (x * scale + scale // 2, y * scale + scale // 2),
                scale // 2,
                bgr,
                -1
            )

        video.write(frame)

    video.release()

    print("Video gespeichert.")