# SE Asia Tectonic Evolution Animation

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GPlately](https://img.shields.io/badge/GPlately-1.0%2B-green.svg)](https://github.com/GPlates/gplately)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR_USERNAME/seasia-tectonic-animation/blob/main/seasia_tectani_gplately.ipynb)

A Python script that creates high-quality animations of Southeast Asia's tectonic evolution from 240 million years ago (Ma) to the present day using plate reconstruction models.

![SE Asia Tectonic Animation Preview](docs/images/animation_preview.gif)

## 🌏 Overview

This project visualizes the complex tectonic history of Southeast Asia, including:

- **Continental drift** and the assembly of Sundaland
- **Subduction zones** (shown in red) where oceanic plates dive beneath continental plates
- **Mid-ocean ridges** (shown in blue) where new oceanic crust is formed
- **Transform faults** (shown in orange) where plates slide past each other
- **Coastline evolution** through geological time

The animation covers the period from the Late Triassic (240 Ma) through the breakup of Pangaea, the opening of the Indian Ocean, and the collision of India with Eurasia.

## 🎬 Sample Output

| Time Period | Major Events |
|-------------|--------------|
| 240-200 Ma | Pangaea begins to break apart |
| 200-150 Ma | Opening of the central Atlantic and Indian Ocean |
| 150-100 Ma | India separates from Gondwana |
| 100-50 Ma | India rapidly moves northward |
| 50-0 Ma | India-Eurasia collision, formation of Himalayas |

## 🚀 Quick Start

### Option 1: Google Colab (Recommended for beginners)

Click the "Open in Colab" badge above, or:

1. Open [Google Colab](https://colab.research.google.com/)
2. Upload `seasia_tectani_gplately.py` or copy the code
3. Run the following cells:

```python
# Install dependencies
!pip install gplately cartopy

# Run the script
%run seasia_tectani_gplately.py
```

### Option 2: Local Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/seasia-tectonic-animation.git
cd seasia-tectonic-animation

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the script
python seasia_tectani_gplately.py
```

## 📋 Requirements

### Python Dependencies

- **Python** ≥ 3.8
- **gplately** ≥ 1.0.0 - High-level plate reconstruction library
- **cartopy** ≥ 0.20.0 - Cartographic projections and mapping
- **matplotlib** ≥ 3.5.0 - Plotting and animation
- **numpy** ≥ 1.20.0 - Numerical operations

### System Dependencies

- **FFmpeg** - Required for saving MP4 animations

#### Installing FFmpeg

**Ubuntu/Debian:**
```bash
sudo apt-get install ffmpeg
```

**macOS (Homebrew):**
```bash
brew install ffmpeg
```

**Windows:**
Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add to PATH.

**Google Colab:**
```python
!apt-get install ffmpeg
```

## ⚙️ Configuration

You can customize the animation by modifying these parameters in the script:

```python
# Time range (in millions of years ago)
time_start = 240          # Start time (Ma)
time_end = 0              # End time (Ma)
time_step = 2             # Time step per frame (Ma)

# Animation settings
fps = 15                  # Frames per second
output_file = 'SE_Asia_tectonic_evolution_240Ma.mp4'

# Geographic extent [lon_min, lon_max, lat_min, lat_max]
extent = [90, 145, -15, 30]  # SE Asia region
```

### Available Plate Models

GPlately supports multiple plate reconstruction models:

| Model | Time Range | Best For |
|-------|------------|----------|
| `Muller2019` | 0-240 Ma | General global reconstructions |
| `Muller2022` | 0-1000 Ma | Deep time reconstructions |
| `Merdith2021` | 0-1000 Ma | Supercontinent cycles |
| `Matthews2016` | 0-410 Ma | Paleozoic reconstructions |

To change the model:

```python
gdownload = gplately.DataServer("Muller2022")  # Change model here
```

### Customizing the Map Extent

To focus on different regions:

```python
# Global view
extent = [-180, 180, -90, 90]

# SE Asia (default)
extent = [90, 145, -15, 30]

# Indonesia focus
extent = [95, 140, -12, 8]

# Thailand and Indochina
extent = [95, 115, 5, 25]
```

## 📁 Project Structure

```
seasia-tectonic-animation/
├── seasia_tectani_gplately.py   # Main animation script
├── README.md                     # This documentation
├── requirements.txt              # Python dependencies
├── LICENSE                       # MIT License
├── .gitignore                    # Git ignore rules
├── docs/
│   └── images/
│       └── animation_preview.gif
└── outputs/                      # Generated animations (gitignored)
    └── SE_Asia_tectonic_evolution_240Ma.mp4
```

## 🔬 Scientific Background

### Plate Reconstruction Model

This project uses the **Müller et al. (2019)** global plate reconstruction model, which provides:

- Continuous plate boundary evolution
- Deforming plate regions
- Absolute plate motions in a mantle reference frame

**Citation:**
> Müller, R.D., Zahirovic, S., Williams, S.E., Cannon, J., Seton, M., Bower, D.J., Tetley, M.G., Heine, C., Le Breton, E., Liu, S., Russell, S.H.J., Yang, T., Leonard, J., and Gurnis, M. (2019). A global plate model including lithospheric deformation along major rifts and orogens since the Triassic. *Tectonics*, 38, 1884-1907. https://doi.org/10.1029/2018TC005462

### SE Asia Tectonic Evolution

Southeast Asia has one of the most complex tectonic histories on Earth, involving:

1. **Sundaland Core**: The stable continental core of SE Asia
2. **Tethyan Terranes**: Fragments rifted from Gondwana that accreted to Asia
3. **Subduction Systems**: Multiple subduction zones consuming oceanic lithosphere
4. **Back-arc Basins**: Extensional basins behind subduction zones

For detailed tectonic history, see:
> Zahirovic, S., Seton, M., and Müller, R.D. (2014). The Cretaceous and Cenozoic tectonic evolution of Southeast Asia. *Solid Earth*, 5, 227-273.

## 🎨 Visualization Legend

| Feature | Color | Description |
|---------|-------|-------------|
| Coastlines | Black | Reconstructed paleoshorelines |
| Continents | Light Gray | Continental polygons (filled) |
| Subduction Zones | Red | Convergent plate boundaries |
| Mid-Ocean Ridges | Blue | Divergent plate boundaries |
| Transform Faults | Orange | Strike-slip plate boundaries |
| Trenches | Dark Red | Deep oceanic trenches |

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **[GPlately](https://github.com/GPlates/gplately)** - Python library for plate tectonic reconstructions
- **[EarthByte Group](https://www.earthbyte.org/)** - For plate reconstruction models and data
- **[GPlates](https://www.gplates.org/)** - Open-source plate reconstruction software
- **[Cartopy](https://scitools.org.uk/cartopy/)** - Cartographic projection library

## 📧 Contact

**Tin Ko Oo**  
Mahidol University, Thailand

- GitHub: [@YOUR_USERNAME](https://github.com/YOUR_USERNAME)
- Email: your.email@example.com

## 📚 References

1. Müller, R.D., et al. (2019). A global plate model including lithospheric deformation along major rifts and orogens since the Triassic. *Tectonics*, 38, 1884-1907.

2. Zahirovic, S., et al. (2014). The Cretaceous and Cenozoic tectonic evolution of Southeast Asia. *Solid Earth*, 5, 227-273.

3. Mather, B.R., et al. (2023). Deep time spatio-temporal data analysis using pyGPlates with PlateTectonicTools and GPlately. *Geoscience Data Journal*, 1-8.

---

<p align="center">
  <i>Made with ❤️ for the geoscience community</i>
</p>
