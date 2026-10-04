# dicom-ct-analyzer
# DICOM CT Analyzer  CT画像（DICOM）を読み込み、表示・簡易解析するPythonツール  ## Features - DICOM file loading - CT slice display  ## Background Created by a radiological technologist. Reproducing image analysis workflows from ImageJ using Python.
print("Hello radtech-K")
# DICOM FFT Analysis

Pythonを用いてDICOM画像を検索・抽出し、2次元高速フーリエ変換（2D FFT）による周波数解析を行ったプロジェクトです。

## Overview

約18,031枚のDICOM画像群を対象に、DICOM metadataのInstance Numberを検索し、Instance Number 17519の画像を自動抽出しました。

抽出した画像に2D FFTを適用し、周波数領域におけるパワースペクトルを計算しました。

さらに、周波数中心からの半径ごとにパワーを平均化し、Radial Power Spectrumとして可視化しました。

## Processing Flow

DICOM image dataset

↓

PythonによるDICOM metadata検索

↓

Instance Number 17519を抽出

↓

2D FFT

↓

Power Spectrum calculation

↓

Radial Power calculation

↓

CSV / PNG output

## Output

* `instance_17519_radial_power.png`

  * Radial Power Spectrumの解析結果

* `instance_17519_radial_power.csv`

  * Radial Powerの数値データ

## Environment

* Python 3.8.10
* NumPy 1.24.4
* pydicom 2.4.4
* Matplotlib 3.7.5

## Methods

主に以下のPythonライブラリを使用しました。

* NumPy

  * 2次元FFT
  * パワースペクトル計算
  * Radial Power calculation

* pydicom

  * DICOMファイルの読み込み
  * Instance Numberによる画像検索

* Matplotlib

  * 解析結果のグラフ化

## Notes

元のDICOMデータは個人情報保護およびデータ容量の都合上、このリポジトリには含めていません。

本プロジェクトでは、DICOM画像を対象としたPythonによる画像処理・周波数解析の実践を目的としています。
