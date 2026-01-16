<div align="center">
  <p>
      <img width="1792" height="310" alt="Data PreProcessing banner Nextits" src="https://github.com/user-attachments/assets/9b3a903e-0eec-44f8-ab44-3c2f93c47beb" />
  </p>

English | [한국어](./readme/README_ko.md) | [简体中文](./readme/README_zh.md)

<!-- icon -->
![python](https://img.shields.io/badge/python-3.11~3.12-aff.svg)
![os](https://img.shields.io/badge/os-linux%2C%20win%2C%20mac-pink.svg)
[![License](https://img.shields.io/badge/license-Apache_2.0-green)](./LICENSE)



**Nextits Function is an integrated AI function system providing document summarization, mindmap generation, and intelligent search capabilities**

</div>

# Nextits Function
[![Framework](https://img.shields.io/badge/Python-3.11+-blue)](#)
[![AI](https://img.shields.io/badge/AI-SGLang-orange)](#)
[![Features](https://img.shields.io/badge/Features-Summarizer%20%7C%20Mindmap%20%7C%20Search-green)](#)

> [!TIP]
> Nextits Function provides powerful AI-driven features for document processing, knowledge visualization, and intelligent information retrieval.
>
> It efficiently handles document summarization, mindmap generation, and web search with summarization.


**Nextits Function** is a comprehensive AI function system that provides **intelligent document processing and knowledge management** capabilities. It offers three core modules for summarization, visualization, and search.

### Core Features

- **Document Summarizer (md_summarizer/)**  
  SGLang-based document summarization system with FastAPI server, supporting markdown parsing and hierarchical summarization.

- **Mindmap Generator (mindmap/)**  
  Automatic mindmap generation from documents with emoji support, segment processing, and Weaviate integration for knowledge management.

- **Intelligent Search (search/)**  
  Integrated search pipeline with Google Search API, web crawling (Wikipedia, Namuwiki, Nate News), and AI-powered summarization.

## 📣 Recent Updates

### 2026.01: AI Function System Release

- **Document Summarizer**:
  - SGLang-based high-performance inference
  - Markdown document parsing and chunking
  - Hierarchical summary generation
  - FastAPI server with async support

- **Mindmap Generator**:
  - Automatic mindmap structure generation
  - Emoji-enhanced visualization
  - Document segment processing
  - Weaviate vector database integration

- **Intelligent Search**:
  - Google Custom Search integration
  - Multi-source web crawling
  - AI-powered content summarization
  - Duplicate filtering and result ranking

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/hnextits/NextitsLM_Function.git
cd NextitsLM_Function

# Install dependencies for each module
cd md_summarizer
pip install -r requirements.txt

cd ../mindmap
pip install -r requirements.txt

cd ../search
pip install -r requirements.txt
```

### Document Summarizer Usage

```bash
# Start SGLang server
cd md_summarizer/scripts
./start_sglang_single.sh

# Run API server
cd ../src
python api_server.py

# Example usage
python examples/usage_example.py
```

### Mindmap Generator Usage

```python
from mindmap.mindmap_generator import MindmapGenerator

# Initialize generator
generator = MindmapGenerator()

# Generate mindmap from document
mindmap = await generator.generate_mindmap(document_text)
```

### Search Pipeline Usage

```python
from search.pipeline import search_and_summarize

# Search and summarize
results = search_and_summarize(
    query="your search query",
    num_results=10
)
```

## 📦 Module Structure

```
skill/
├── md_summarizer/          # Document summarization module
│   ├── src/
│   │   ├── api_server.py   # FastAPI server
│   │   ├── sglang_client.py # SGLang client
│   │   ├── md_parser.py    # Markdown parser
│   │   └── summary_index.py # Summary indexing
│   ├── scripts/            # Server management scripts
│   ├── config/             # Configuration files
│   └── tests/              # Unit tests
│
├── mindmap/                # Mindmap generation module
│   ├── mindmap_generator.py # Main generator
│   ├── segment_processor.py # Document segmentation
│   ├── weaviate_service.py  # Vector DB service
│   └── config.py           # Configuration
│
└── search/                 # Search pipeline module
    ├── pipeline.py         # Main search pipeline
    ├── google_search.py    # Google Search client
    ├── summarizer.py       # Content summarizer
    ├── util.py             # Utility functions
    └── crawler/            # Web crawlers
        ├── wikipedia.py
        ├── namuwiki.py
        └── natenews.py
```

## 🔧 Configuration

### Document Summarizer

Edit `md_summarizer/config/model_config.yaml`:

```yaml
model:
  name: "Model"
  max_tokens: 
  temperature:

server:
  host: "0.0.0.0"
  port: 8000
```

### Mindmap Generator

Edit `mindmap/config.py`:

```python
class Config:
    WEAVIATE_URL = "http://localhost:8080"
    MODEL_NAME = "Model"
    MAX_SEGMENTS = 50
```

### Search Pipeline

Set environment variables or edit configuration:

```bash
export GOOGLE_API_KEY="your_api_key"
export GOOGLE_CX_ID="your_cx_id"
```

## 🎯 Key Features

### Document Summarizer
- **High-Performance Inference**: SGLang-based efficient model serving
- **Hierarchical Summarization**: Multi-level document summarization
- **Async Processing**: FastAPI with async/await support
- **Flexible Parsing**: Markdown document structure analysis

### Mindmap Generator
- **Automatic Structure**: AI-driven mindmap structure generation
- **Visual Enhancement**: Emoji-based node decoration
- **Knowledge Management**: Weaviate vector database integration
- **Segment Processing**: Intelligent document chunking

### Intelligent Search
- **Multi-Source Crawling**: Wikipedia, Namuwiki, Nate News support
- **Smart Filtering**: Duplicate removal and relevance ranking
- **AI Summarization**: Automatic content summarization
- **Configurable Pipeline**: Flexible search and processing workflow

## 📊 Performance

- **Summarizer**: Processes 10K tokens in ~2 seconds
- **Mindmap**: Generates complex mindmaps in ~5 seconds
- **Search**: Retrieves and summarizes 10 results in ~10 seconds

## 🧪 Testing

```bash
# Test document summarizer
cd md_summarizer
pytest tests/

# Test mindmap generator
cd mindmap
python -m pytest

# Test search pipeline
cd search
python -m pytest
```

## 🛠️ Development

### Requirements

- Python 3.11 or higher
- CUDA 11.0 or higher (for GPU usage)
- Sufficient memory (minimum 16GB recommended)

### Setting up Development Environment

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

## 📝 License

This project is distributed under the Apache 2.0 License. See the [LICENSE](./LICENSE) file for details.

## 🙏 Acknowledgments

This project was made possible with the help of the following open-source projects:

- **[SGLang](https://github.com/sgl-project/sglang)**: High-performance LLM serving framework
- **[Weaviate](https://github.com/weaviate/weaviate)**: Vector database for knowledge management

## 🎓 Citation

If you use this project in your research, please cite the following papers:

### SGLang
```bibtex
@misc{zheng2023sglang,
  title={SGLang: Efficient Execution of Structured Language Model Programs},
  author={Lianmin Zheng and Liangsheng Yin and Zhiqiang Xie and Jeff Huang and Chuyue Sun and Cody Hao Yu and Shiyi Cao and Christos Kozyrakis and Ion Stoica and Joseph E. Gonzalez and Clark Barrett and Ying Sheng},
  year={2023},
  url={https://github.com/sgl-project/sglang}
}
```

## 🌐 Demo Site

Try out our system at: [https://quantuss.hnextits.com/](https://quantuss.hnextits.com/)

## 👥 Contributors

This project was developed by the following team members:

- **Lim** - [junseung_lim@hnextits.com](mailto:junseung_lim@hnextits.com)
- **Jeong** - [jeongnext@hnextits.com](mailto:jeongnext@hnextits.com)
- **Ryu** - [fbgjungits@hnextits.com](mailto:fbgjungits@hnextits.com)

## 📧 Contact

If you have any questions or suggestions about the project, please open an issue.

## 🌟 Contributing

Contributions are welcome! Please send a Pull Request or open an issue.

---

<div align="center">
Made with 🩸💦😭 by Nextits Team
</div>
