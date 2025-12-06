# -*- coding: utf-8 -*-
"""SE Asia Tectonic Animation using GPlately

This script creates a high-quality animation of SE Asia tectonic evolution 240 Ma → 0 Ma
using the GPlately library which automatically handles data download and caching.
"""

# Install required packages (run these in Colab):
# !pip install gplately
# !pip install cartopy

import gplately
from gplately import PlateReconstruction, PlotTopologies
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import numpy as np
from matplotlib.animation import FuncAnimation
import warnings
warnings.filterwarnings("ignore")

# ================================
# 1. Download data using GPlately's DataServer
# ================================
# GPlately automatically downloads and caches plate model files
# Available models: "Muller2019", "Muller2022", "Merdith2021", "Matthews2016", etc.

print("Downloading plate reconstruction data (this may take a minute on first run)...")

# Use Muller2019 model - well-suited for SE Asia reconstructions back to 240 Ma
gdownload = gplately.DataServer("Muller2019")

# Get plate reconstruction files
rotation_model, topology_features, static_polygons = gdownload.get_plate_reconstruction_files()

# Get geometry files
coastlines, continents, COBs = gdownload.get_topology_geometries()

print("Data download complete!")

# ================================
# 2. Create the PlateReconstruction model
# ================================
model = PlateReconstruction(rotation_model, topology_features, static_polygons)

# ================================
# 3. Settings
# ================================
time_start = 240          # Ma
time_end = 0
time_step = 2             # million years per frame (2 Ma → ~120 frames)
fps = 15
output_file = 'SE_Asia_tectonic_evolution_240Ma.mp4'

# Region of interest (zoom on SE Asia)
extent = [90, 145, -15, 30]   # [lon_min, lon_max, lat_min, lat_max]

# ================================
# 4. Set up the figure
# ================================
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection=ccrs.PlateCarree())
ax.set_extent(extent, crs=ccrs.PlateCarree())

# Add gridlines
gl = ax.gridlines(draw_labels=True, linewidth=0.5, color='gray', alpha=0.5)
gl.top_labels = False
gl.right_labels = False

# Create PlotTopologies object for plotting
gplot = PlotTopologies(model, coastlines=coastlines, continents=continents, COBs=COBs, time=0)

# Add title
title = ax.set_title(f'SE Asia Tectonic Evolution: 0 Ma', fontsize=14)

# Add legend elements (we'll create proxy artists)
from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], color='black', linewidth=1.5, label='Coastlines'),
    Line2D([0], [0], color='red', linewidth=2, label='Subduction Zones'),
    Line2D([0], [0], color='blue', linewidth=2, label='Mid-Ocean Ridges'),
    Line2D([0], [0], color='orange', linewidth=1.5, label='Transform Faults'),
]
ax.legend(handles=legend_elements, loc='lower left', fontsize=9)

# Time text
time_text = ax.text(0.02, 0.98, '', transform=ax.transAxes,
                    fontsize=16, va='top', ha='left',
                    bbox=dict(boxstyle="round", facecolor='wheat'))

# ================================
# 5. Animation update function
# ================================
def update(frame):
    reconstruction_time = time_start - frame * time_step
    if reconstruction_time < time_end:
        reconstruction_time = time_end
    
    # Clear the axes but keep extent
    ax.clear()
    ax.set_extent(extent, crs=ccrs.PlateCarree())
    
    # Add gridlines
    gl = ax.gridlines(draw_labels=True, linewidth=0.5, color='gray', alpha=0.5)
    gl.top_labels = False
    gl.right_labels = False
    
    # Update the PlotTopologies time
    gplot.time = reconstruction_time
    
    # Plot continents (filled)
    try:
        gplot.plot_continents(ax, facecolor='lightgray', edgecolor='none', alpha=0.5)
    except:
        pass
    
    # Plot coastlines
    try:
        gplot.plot_coastlines(ax, color='black', linewidth=1.2)
    except:
        pass
    
    # Plot plate boundaries (topologies)
    try:
        # Plot subduction zones in red
        gplot.plot_subduction_teeth(ax, color='red', linewidth=1.5)
    except:
        pass
    
    try:
        # Plot ridges in blue
        gplot.plot_ridges(ax, color='blue', linewidth=1.5)
    except:
        pass
    
    try:
        # Plot transforms in orange
        gplot.plot_transforms(ax, color='orange', linewidth=1.2)
    except:
        pass
    
    try:
        # Plot trenches
        gplot.plot_trenches(ax, color='darkred', linewidth=1.5)
    except:
        pass
    
    # Update title and time text
    ax.set_title(f'SE Asia Tectonic Evolution', fontsize=14)
    time_text = ax.text(0.02, 0.98, f'{reconstruction_time:.0f} Ma', 
                        transform=ax.transAxes,
                        fontsize=16, va='top', ha='left',
                        bbox=dict(boxstyle="round", facecolor='wheat'))
    
    # Re-add legend
    legend_elements = [
        Line2D([0], [0], color='black', linewidth=1.5, label='Coastlines'),
        Line2D([0], [0], color='red', linewidth=2, label='Subduction Zones'),
        Line2D([0], [0], color='blue', linewidth=2, label='Mid-Ocean Ridges'),
        Line2D([0], [0], color='orange', linewidth=1.5, label='Transform Faults'),
    ]
    ax.legend(handles=legend_elements, loc='lower left', fontsize=9)
    
    print(f"Frame {frame}: {reconstruction_time:.0f} Ma")
    
    return []

# ================================
# 6. Create animation
# ================================
n_frames = int((time_start - time_end) / time_step) + 1
print(f"Creating animation with {n_frames} frames...")

anim = FuncAnimation(fig, update, frames=n_frames, interval=1000/fps, blit=False)

# Save animation (requires ffmpeg)
print("Saving animation...")
anim.save(output_file, fps=fps, dpi=150, writer='ffmpeg')
print(f"Animation saved as {output_file}")

plt.show()
