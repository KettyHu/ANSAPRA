#!/usr/bin/env python3
"""
本地运行脚本 - 用于本地测试
使用：python run_local.py
"""

import os
import sys
import subprocess
import time

def check_dependencies():
    """检查并安装依赖"""
    print("📦 检查Python依赖...")
    
    try:
        import flask
        import werkzeug
        import requests
        import pypdf2
        print("✅ 所有依赖已安装")
    except ImportError:
        print("❌ 缺少依赖，正在安装...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def setup_environment():
    """设置环境变量"""
    print("🔧 设置环境变量...")
    
    # 创建 .env 文件如果不存在
    if not os.path.exists('.env'):
        with open('.env', 'w', encoding='utf-8') as f:
            f.write("""# ANSAPRA 本地开发环境配置
SECRET_KEY=dev-secret-key-local-test
DEEPSEEK_API_KEY=sk-99c89d4d5dd24a358eadcce927246a41
PORT=5000

# 开发模式设置
FLASK_ENV=development
FLASK_DEBUG=1
""")
        print("📝 已创建 .env 文件，API密钥已设置")
    
    # 加载环境变量
    if os.path.exists('.env'):
        with open('.env', 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    key, value = line.split('=', 1)
                    os.environ[key.strip()] = value.strip()
    
    print("✅ 环境变量设置完成")

def create_missing_dirs():
    """创建缺失的目录"""
    print("📁 创建项目目录结构...")
    
    dirs = [
        'data',
        'static/css',
        'static/js',
        'static/lang',
        'templates'
    ]
    
    for dir_path in dirs:
        if not os.path.exists(dir_path):
            os.makedirs(dir_path, exist_ok=True)
            print(f"  📂 创建目录: {dir_path}")
    
    print("✅ 目录结构创建完成")

def create_missing_files():
    """创建缺失的文件"""
    print("📄 检查并创建缺失文件...")
    
    # 1. 创建简单的 style.css（如果不存在）
    css_path = 'static/css/style.css'
    if not os.path.exists(css_path):
        with open(css_path, 'w', encoding='utf-8') as f:
            f.write("""
/* 基本样式 - 本地测试用 */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Microsoft YaHei', sans-serif;
}

body {
    background-color: #f8f9fa;
    color: #333;
    line-height: 1.6;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

/* 模态框样式 */
.modal {
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    z-index: 1000;
    justify-content: center;
    align-items: center;
}

.modal-content {
    background: white;
    padding: 30px;
    border-radius: 10px;
    max-width: 500px;
    width: 90%;
    max-height: 80vh;
    overflow-y: auto;
}

/* 按钮样式 */
.btn {
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 16px;
    transition: all 0.3s ease;
}

.btn-primary {
    background-color: #007bff;
    color: white;
}

.btn-primary:hover {
    background-color: #0056b3;
}

.btn-secondary {
    background-color: #6c757d;
    color: white;
}

.btn-secondary:hover {
    background-color: #545b62;
}

/* 表单样式 */
.form-group {
    margin-bottom: 20px;
}

.form-group label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
}

.form-group input,
.form-group textarea,
.form-group select {
    width: 100%;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 4px;
    font-size: 16px;
}

/* 导航栏 */
.header {
    background-color: #007bff;
    color: white;
    padding: 15px 0;
}

.header-content {
    display: flex;
    justify-content: space-between;
    align-items: center;
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}

.logo {
    font-size: 24px;
    font-weight: bold;
}

.main-nav ul {
    display: flex;
    list-style: none;
    gap: 20px;
}

.main-nav a {
    color: white;
    text-decoration: none;
    padding: 5px 10px;
    border-radius: 4px;
    transition: background-color 0.3s ease;
}

.main-nav a:hover,
.main-nav a.active {
    background-color: rgba(255, 255, 255, 0.1);
}

/* 页面样式 */
.page {
    display: none;
    padding: 30px 0;
}

.page.active {
    display: block;
}

.content-section {
    background: white;
    padding: 20px;
    border-radius: 8px;
    margin-bottom: 20px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

/* 上传区域 */
.upload-box {
    border: 2px dashed #007bff;
    border-radius: 10px;
    padding: 40px 20px;
    text-align: center;
    background-color: #f8f9fa;
    margin-bottom: 20px;
}

.upload-box i {
    color: #007bff;
    margin-bottom: 15px;
}

/* 搜索结果 */
.results-section {
    background: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

/* 搜索平台 */
.search-platforms {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 20px;
    margin-top: 20px;
}

.search-platform {
    background: white;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    border: 1px solid #e0e0e0;
}

.search-platform h5 {
    margin-bottom: 15px;
    font-size: 1.1rem;
    color: #333;
    display: flex;
    align-items: center;
    gap: 10px;
}

.search-input-group {
    display: flex;
    gap: 10px;
    margin-bottom: 10px;
}

.search-input {
    flex: 1;
    padding: 12px 15px;
    border: 2px solid #e0e0e0;
    border-radius: 6px;
    font-size: 14px;
    transition: all 0.3s ease;
}

.search-input:focus {
    outline: none;
    border-color: #007bff;
    box-shadow: 0 0 0 3px rgba(0, 123, 255, 0.1);
}

.search-btn {
    padding: 12px 20px;
    white-space: nowrap;
}

.search-hint {
    font-size: 12px;
    color: #666;
    margin-top: 8px;
}

/* 响应式设计 */
@media (max-width: 768px) {
    .header-content {
        flex-direction: column;
        gap: 15px;
    }
    
    .main-nav ul {
        flex-direction: column;
        align-items: center;
    }
    
    .search-platforms {
        grid-template-columns: 1fr;
    }
    
    .search-input-group {
        flex-direction: column;
    }
    
    .search-btn {
        width: 100%;
    }
}

/* 通知样式 */
.notification {
    position: fixed;
    top: 20px;
    right: 20px;
    padding: 15px 25px;
    border-radius: 8px;
    color: white;
    font-weight: 500;
    z-index: 1000;
    animation: slideInRight 0.3s ease;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}

.notification-success {
    background-color: #28a745;
}

.notification-error {
    background-color: #dc3545;
}

.notification-info {
    background-color: #17a2b8;
}

.notification-warning {
    background-color: #ffc107;
}

@keyframes slideInRight {
    from { transform: translateX(100%); opacity: 0; }
    to { transform: translateX(0); opacity: 1; }
}

@keyframes slideOutRight {
    from { transform: translateX(0); opacity: 1; }
    to { transform: translateX(100%); opacity: 0; }
}
""")
        print(f"  📝 创建 {css_path}")
    
    # 2. 创建 translations.json
    lang_path = 'static/lang/translations.json'
    if not os.path.exists(lang_path):
        with open(lang_path, 'w', encoding='utf-8') as f:
            f.write("""{
    "zh": {
        "appName": "ANSAPRA - 高中生自然科学论文自适应阅读智能体",
        "intro": "网站介绍",
        "instructions": "使用说明",
        "interpretation": "论文解读",
        "settings": "用户设置",
        "login": "登录",
        "register": "注册",
        "guest": "游客体验",
        "startInterpretation": "开始解读",
        "clear": "清空",
        "zh": "中文",
        "en": "English"
    },
    "en": {
        "appName": "ANSAPRA - Adaptive Natural Science Academic Paper Reading Agent",
        "intro": "Introduction",
        "instructions": "Instructions",
        "interpretation": "Paper Interpretation",
        "settings": "Settings",
        "login": "Login",
        "register": "Register",
        "guest": "Guest Experience",
        "startInterpretation": "Start Interpretation",
        "clear": "Clear",
        "zh": "中文",
        "en": "English"
    }
}""")
        print(f"  📝 创建 {lang_path}")
    
    # 3. 创建简化的 language.js（如果不存在）
    js_lang_path = 'static/js/language.js'
    if not os.path.exists(js_lang_path):
        with open(js_lang_path, 'w', encoding='utf-8') as f:
            f.write("""// 简化的语言切换功能 - 本地测试用
console.log("language.js loaded");

// 全局变量
if (typeof AppState === 'undefined') {
    window.AppState = {
        user: null,
        currentPage: 'intro',
        isProcessing: false,
        language: 'zh',
        translations: {}
    };
}

// 初始化语言功能
function initLanguage() {
    console.log("初始化语言功能");
    // 从localStorage加载语言设置
    const savedLang = localStorage.getItem('appLanguage') || 'zh';
    AppState.language = savedLang;
    
    // 更新UI
    updateLanguageUI();
}

// 更新语言UI
function updateLanguageUI() {
    const langRadios = document.querySelectorAll('input[name="language"]');
    langRadios.forEach(radio => {
        if (radio.value === AppState.language) {
            radio.checked = true;
        }
        
        // 添加change事件
        radio.addEventListener('change', function() {
            if (this.checked) {
                AppState.language = this.value;
                localStorage.setItem('appLanguage', this.value);
                alert(`语言已切换为: ${this.value === 'zh' ? '中文' : 'English'}`);
            }
        });
    });
}

// 语言切换函数
function changeLanguage(lang) {
    AppState.language = lang;
    localStorage.setItem('appLanguage', lang);
    updateLanguageUI();
    alert(`语言已切换为: ${lang === 'zh' ? '中文' : 'English'}`);
}

// 页面加载完成后初始化
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initLanguage);
} else {
    initLanguage();
}

// 暴露到全局
window.changeLanguage = changeLanguage;
window.initLanguage = initLanguage;
""")
        print(f"  📝 创建 {js_lang_path}")
    
    print("✅ 缺失文件创建完成")

def check_app_structure():
    """检查应用结构完整性"""
    print("🔍 检查应用结构...")
    
    required_files = [
        'app.py',
        'requirements.txt',
        'templates/index.html'
    ]
    
    missing_files = []
    for file_path in required_files:
        if not os.path.exists(file_path):
            missing_files.append(file_path)
    
    if missing_files:
        print(f"❌ 缺少必要文件: {', '.join(missing_files)}")
        print("请从原项目中复制这些文件到本地目录")
        return False
    
    print("✅ 应用结构完整")
    return True

def print_instructions():
    """打印使用说明"""
    print("\n" + "="*50)
    print("🚀 ANSAPRA 本地测试环境准备完成！")
    print("="*50)
    print("\n📋 后续步骤：")
    print("1. 编辑 .env 文件，添加你的 DeepSeek API 密钥")
    print("2. 安装依赖：pip install -r requirements.txt")
    print("3. 启动服务器：python app.py")
    print("\n🌐 访问地址：http://localhost:5000")
    print("\n📁 项目结构已创建，现在可以：")
    print("  - 复制原项目的 index.html 到 templates/ 目录")
    print("  - 复制原项目的 main.js 和 settings.js 到 static/js/ 目录")
    print("  - 测试上传论文功能")
    print("\n💡 提示：")
    print("  - 如果没有DeepSeek API密钥，可以注册获取")
    print("  - 或者使用模拟数据测试上传功能")
    print("  - 查看日志：python app.py 运行时会显示详细日志")
    print("="*50 + "\n")

def main():
    """主函数"""
    print("🔧 ANSAPRA 本地环境设置工具")
    print("="*50)
    
    # 创建目录结构
    create_missing_dirs()
    
    # 创建缺失文件
    create_missing_files()
    
    # 设置环境变量
    setup_environment()
    
    # 检查依赖
    check_dependencies()
    
    # 检查应用结构
    if check_app_structure():
        print_instructions()
        
        # 询问是否立即启动
        response = input("是否立即启动服务器？(y/n): ").strip().lower()
        if response == 'y':
            start_server()
    else:
        print("\n❌ 请先补齐缺失的核心文件，然后重新运行此脚本")

def start_server():
    """启动服务器"""
    print("\n🚀 启动本地服务器...")
    print("按 Ctrl+C 停止服务器\n")
    
    try:
        # 导入并运行app
        from app import app
        port = int(os.environ.get('PORT', 5000))
        app.run(
            host='0.0.0.0',
            port=port,
            debug=True,
            threaded=True
        )
    except ImportError as e:
        print(f"❌ 导入错误: {e}")
        print("请确保 app.py 文件存在且正确")
    except Exception as e:
        print(f"❌ 启动服务器失败: {e}")

if __name__ == '__main__':
    main()