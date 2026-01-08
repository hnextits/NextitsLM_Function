<div align="center">
  <p>
      <img width="100%" src="" alt="Nextits Function Banner">
  </p>

[English](../README.md) | [한국어](./README_ko.md) | 简体中文

<!-- icon -->
![python](https://img.shields.io/badge/python-3.11~3.12-aff.svg)
![os](https://img.shields.io/badge/os-linux%2C%20win%2C%20mac-pink.svg)
[![License](https://img.shields.io/badge/license-Apache_2.0-green)](../LICENSE)



**Nextits Function 是一个集成的AI功能系统，提供文档摘要、思维导图生成和智能搜索功能**

</div>

# Nextits Function
[![Framework](https://img.shields.io/badge/Python-3.11+-blue)](#)
[![AI](https://img.shields.io/badge/AI-SGLang-orange)](#)
[![Features](https://img.shields.io/badge/Features-Summarizer%20%7C%20Mindmap%20%7C%20Search-green)](#)

> [!TIP]
> Nextits Function 为文档处理、知识可视化和智能信息检索提供强大的AI驱动功能。
>
> 它高效处理文档摘要、思维导图生成和带摘要的网络搜索。


**Nextits Function** 是一个综合性AI功能系统，提供**智能文档处理和知识管理**能力。它为摘要、可视化和搜索提供三个核心模块。

### 核心功能

- **文档摘要器 (md_summarizer/)**  
  基于SGLang的文档摘要系统，支持FastAPI服务器、Markdown解析和分层摘要。

- **思维导图生成器 (mindmap/)**  
  从文档自动生成思维导图，支持表情符号、段落处理和Weaviate集成的知识管理。

- **智能搜索 (search/)**  
  集成搜索管道，包含Google Search API、网络爬虫（Wikipedia、Namuwiki、Nate News）和AI驱动的摘要。

## 📣 最近更新

### 2026.01: AI功能系统发布

- **文档摘要器**:
  - 基于SGLang的高性能推理
  - Markdown文档解析和分块
  - 分层摘要生成
  - 支持异步的FastAPI服务器

- **思维导图生成器**:
  - 自动思维导图结构生成
  - 表情符号增强可视化
  - 文档段落处理
  - Weaviate向量数据库集成

- **智能搜索**:
  - Google Custom Search集成
  - 多源网络爬虫
  - AI驱动的内容摘要
  - 重复过滤和结果排序

## 🚀 快速开始

### 安装

```bash
# 克隆仓库
git clone https://github.com/hnextits/NextitsLM_Function.git
cd NextitsLM_Function

# 安装各模块依赖
cd md_summarizer
pip install -r requirements.txt

cd ../mindmap
pip install -r requirements.txt

cd ../search
pip install -r requirements.txt
```

### 文档摘要器使用

```bash
# 启动SGLang服务器
cd md_summarizer/scripts
./start_sglang_single.sh

# 运行API服务器
cd ../src
python api_server.py

# 示例使用
python examples/usage_example.py
```

### 思维导图生成器使用

```python
from mindmap.mindmap_generator import MindmapGenerator

# 初始化生成器
generator = MindmapGenerator()

# 从文档生成思维导图
mindmap = await generator.generate_mindmap(document_text)
```

### 搜索管道使用

```python
from search.pipeline import search_and_summarize

# 搜索和摘要
results = search_and_summarize(
    query="搜索查询",
    num_results=10
)
```

## 📦 模块结构

```
skill/
├── md_summarizer/          # 文档摘要模块
│   ├── src/
│   │   ├── api_server.py   # FastAPI服务器
│   │   ├── sglang_client.py # SGLang客户端
│   │   ├── md_parser.py    # Markdown解析器
│   │   └── summary_index.py # 摘要索引
│   ├── scripts/            # 服务器管理脚本
│   ├── config/             # 配置文件
│   └── tests/              # 单元测试
│
├── mindmap/                # 思维导图生成模块
│   ├── mindmap_generator.py # 主生成器
│   ├── segment_processor.py # 文档分段
│   ├── weaviate_service.py  # 向量数据库服务
│   └── config.py           # 配置
│
└── search/                 # 搜索管道模块
    ├── pipeline.py         # 主搜索管道
    ├── google_search.py    # Google Search客户端
    ├── summarizer.py       # 内容摘要器
    ├── util.py             # 工具函数
    └── crawler/            # 网络爬虫
        ├── wikipedia.py
        ├── namuwiki.py
        └── natenews.py
```

## 🔧 配置

### 文档摘要器

编辑 `md_summarizer/config/model_config.yaml`:

```yaml
model:
  name: "Model"
  max_tokens: 4096
  temperature: 0.7

server:
  host: "0.0.0.0"
  port: 8000
```

### 思维导图生成器

编辑 `mindmap/config.py`:

```python
class Config:
    WEAVIATE_URL = "http://localhost:8080"
    MODEL_NAME = "Model"
    MAX_SEGMENTS = 50
```

### 搜索管道

设置环境变量或编辑配置:

```bash
export GOOGLE_API_KEY="your_api_key"
export GOOGLE_CX_ID="your_cx_id"
```

## 🎯 主要特性

### 文档摘要器
- **高性能推理**: 基于SGLang的高效模型服务
- **分层摘要**: 多级文档摘要
- **异步处理**: 支持async/await的FastAPI
- **灵活解析**: Markdown文档结构分析

### 思维导图生成器
- **自动结构**: AI驱动的思维导图结构生成
- **视觉增强**: 基于表情符号的节点装饰
- **知识管理**: Weaviate向量数据库集成
- **段落处理**: 智能文档分块

### 智能搜索
- **多源爬虫**: 支持Wikipedia、Namuwiki、Nate News
- **智能过滤**: 重复删除和相关性排序
- **AI摘要**: 自动内容摘要
- **可配置管道**: 灵活的搜索和处理工作流

## 📊 性能

- **摘要器**: 约2秒处理10K tokens
- **思维导图**: 约5秒生成复杂思维导图
- **搜索**: 约10秒检索和摘要10个结果

## 🧪 测试

```bash
# 测试文档摘要器
cd md_summarizer
pytest tests/

# 测试思维导图生成器
cd mindmap
python -m pytest

# 测试搜索管道
cd search
python -m pytest
```

## 🛠️ 开发

### 要求

- Python 3.11 或更高版本
- CUDA 11.0 或更高版本（用于 GPU）
- 充足的内存（建议至少 16GB）

### 设置开发环境

```bash
# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 安装开发依赖
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

## 📝 许可证

本项目根据 Apache 2.0 许可证分发。详情请参阅 [LICENSE](../LICENSE) 文件。

## 🙏 致谢

本项目得益于以下开源项目的帮助：

- **[SGLang](https://github.com/sgl-project/sglang)**: 高性能LLM服务框架
- **[Weaviate](https://github.com/weaviate/weaviate)**: 用于知识管理的向量数据库

## 🎓 引用

如果您在研究中使用本项目，请引用以下论文：

### SGLang
```bibtex
@misc{zheng2023sglang,
  title={SGLang: Efficient Execution of Structured Language Model Programs},
  author={Lianmin Zheng and Liangsheng Yin and Zhiqiang Xie and Jeff Huang and Chuyue Sun and Cody Hao Yu and Shiyi Cao and Christos Kozyrakis and Ion Stoica and Joseph E. Gonzalez and Clark Barrett and Ying Sheng},
  year={2023},
  url={https://github.com/sgl-project/sglang}
}
```

## 🌐 演示网站

在线试用我们的系统：[https://quantuss.hnextits.com/](https://quantuss.hnextits.com/)

## 👥 开发者

本项目由以下团队成员开发：

- **Lim** - [junseung_lim@hnextits.com](mailto:junseung_lim@hnextits.com)
- **Jeong** - [jeongnext@hnextits.com](mailto:jeongnext@hnextits.com)
- **Ryu** - [fbgjungits@hnextits.com](mailto:fbgjungits@hnextits.com)

## 📧 联系方式

如果您对项目有任何问题或建议，请提交 issue。

## 🌟 贡献

欢迎贡献！请发送 Pull Request 或提交 issue。

---

<div align="center">
Made with 🩸💦😭 by Nextits Team
</div>
