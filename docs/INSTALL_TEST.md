# LangParse 安装测试指南

## 从本地 Wheel 包安装

### 方法 1: 使用 uv (推荐)

```bash
# 安装基础版本
uv pip install dist/langparse-0.0.1-py3-none-any.whl

# 或安装带所有可选依赖的完整版本
uv pip install "dist/langparse-0.0.1-py3-none-any.whl[all]"

# 或只安装特定功能的依赖
uv pip install "dist/langparse-0.0.1-py3-none-any.whl[pdf,docx]"
```

### 方法 2: 使用标准 pip

```bash
# 安装基础版本
pip install dist/langparse-0.0.1-py3-none-any.whl

# 或安装完整版本
pip install "dist/langparse-0.0.1-py3-none-any.whl[all]"
```

## 可选依赖说明

- `pdf`: PDF 解析支持 (pdfplumber)
- `docx`: Word 文档解析支持 (python-docx)
- `excel`: Excel 解析支持 (pandas, openpyxl)
- `ocr`: OCR 支持 (rapidocr_onnxruntime)
- `all`: 安装所有可选依赖
- `dev`: 开发依赖 (pytest)

## 验证安装

运行测试脚本：

```bash
python test_installation.py
```

预期输出：
```
============================================================
LangParse Installation Test
============================================================
Testing basic imports...
✓ All imports successful

Testing Markdown parsing...
✓ Parsed document with 2 chunks
  First chunk header: Test Document

Testing AutoParser...
✓ AutoParser successfully routed .md file
  Metadata: {...}

============================================================
Test Summary
============================================================
✓ PASS: Basic Imports
✓ PASS: Markdown Parsing
✓ PASS: AutoParser

============================================================
✓ All tests passed! LangParse is working correctly.
============================================================
```

## 快速开始示例

```python
from langparse import AutoParser, SemanticChunker

# 解析任意文档
doc = AutoParser.parse("your_document.pdf")  # 或 .docx, .xlsx, .md

# 智能分块
chunker = SemanticChunker()
chunks = chunker.chunk(doc)

# 查看结果
for chunk in chunks:
    print(f"Header: {chunk.metadata.get('header_path')}")
    print(f"Pages: {chunk.metadata.get('page_numbers')}")
    print(f"Content: {chunk.content[:100]}...")
    print("-" * 60)
```

## 在新环境中测试

如果你想在一个干净的环境中测试：

```bash
# 创建新的虚拟环境
uv venv test-env
source test-env/bin/activate  # Linux/Mac
# 或 test-env\Scripts\activate  # Windows

# 安装包
uv pip install dist/langparse-0.0.1-py3-none-any.whl[all]

# 运行测试
python test_installation.py

# 退出环境
deactivate
```

## 卸载

```bash
uv pip uninstall langparse
# 或
pip uninstall langparse
```
