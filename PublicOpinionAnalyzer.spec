# -*- mode: python ; coding: utf-8 -*-
# PyInstaller spec file for PublicOpinionAnalyzer
#
# Usage:
#   pyinstaller PublicOpinionAnalyzer.spec

from PyInstaller.utils.hooks import collect_data_files, collect_submodules

block_cipher = None

# Collect data files for gradio (templates, static files, types.json, etc.)
datas = []
datas += collect_data_files('gradio')
datas += collect_data_files('gradio_client')

# Collect hidden imports
hiddenimports = []
hiddenimports += collect_submodules('gradio')
hiddenimports += collect_submodules('gradio_client')

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='PublicOpinionAnalyzer',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,  # No console window
    disable_windowed_traceback=False,
    argv_emulation=True,  # Important for macOS
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='PublicOpinionAnalyzer',
)
