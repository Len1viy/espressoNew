import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QHBoxLayout, QVBoxLayout, QLayoutItem, QTableWidget, \
    QTableWidgetItem, QLabel, QMainWindow
import sqlite3
import io

temp = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="enabled">
   <bool>true</bool>
  </property>
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1361</width>
    <height>600</height>
   </rect>
  </property>
  <property name="cursor">
   <cursorShape>ArrowCursor</cursorShape>
  </property>
  <property name="mouseTracking">
   <bool>false</bool>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <property name="windowOpacity">
   <double>1.000000000000000</double>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QTableWidget" name="tableWidget">
    <property name="enabled">
     <bool>true</bool>
    </property>
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>1361</width>
      <height>551</height>
     </rect>
    </property>
    <property name="minimumSize">
     <size>
      <width>930</width>
      <height>260</height>
     </size>
    </property>
    <property name="maximumSize">
     <size>
      <width>16777215</width>
      <height>16777215</height>
     </size>
    </property>
    <property name="layoutDirection">
     <enum>Qt::LeftToRight</enum>
    </property>
    <property name="autoFillBackground">
     <bool>false</bool>
    </property>
    <property name="styleSheet">
     <string notr="true"/>
    </property>
    <property name="verticalScrollBarPolicy">
     <enum>Qt::ScrollBarAsNeeded</enum>
    </property>
    <property name="sizeAdjustPolicy">
     <enum>QAbstractScrollArea::AdjustIgnored</enum>
    </property>
    <property name="autoScroll">
     <bool>true</bool>
    </property>
    <property name="autoScrollMargin">
     <number>16</number>
    </property>
    <property name="tabKeyNavigation">
     <bool>true</bool>
    </property>
    <property name="showDropIndicator" stdset="0">
     <bool>true</bool>
    </property>
    <property name="dragDropOverwriteMode">
     <bool>true</bool>
    </property>
    <property name="horizontalScrollMode">
     <enum>QAbstractItemView::ScrollPerItem</enum>
    </property>
    <property name="showGrid">
     <bool>true</bool>
    </property>
    <property name="gridStyle">
     <enum>Qt::SolidLine</enum>
    </property>
    <property name="sortingEnabled">
     <bool>false</bool>
    </property>
    <property name="wordWrap">
     <bool>true</bool>
    </property>
    <property name="cornerButtonEnabled">
     <bool>true</bool>
    </property>
    <property name="rowCount">
     <number>0</number>
    </property>
    <property name="columnCount">
     <number>6</number>
    </property>
    <attribute name="horizontalHeaderVisible">
     <bool>true</bool>
    </attribute>
    <attribute name="horizontalHeaderCascadingSectionResizes">
     <bool>false</bool>
    </attribute>
    <attribute name="horizontalHeaderMinimumSectionSize">
     <number>20</number>
    </attribute>
    <attribute name="horizontalHeaderDefaultSectionSize">
     <number>234</number>
    </attribute>
    <attribute name="horizontalHeaderHighlightSections">
     <bool>false</bool>
    </attribute>
    <attribute name="verticalHeaderVisible">
     <bool>true</bool>
    </attribute>
    <attribute name="verticalHeaderMinimumSectionSize">
     <number>18</number>
    </attribute>
    <attribute name="verticalHeaderDefaultSectionSize">
     <number>35</number>
    </attribute>
    <attribute name="verticalHeaderHighlightSections">
     <bool>true</bool>
    </attribute>
    <column>
     <property name="text">
      <string>ID</string>
     </property>
    </column>
    <column>
     <property name="text">
      <string>Название сорта</string>
     </property>
    </column>
    <column>
     <property name="text">
      <string>Степень обжарки</string>
     </property>
    </column>
    <column>
     <property name="text">
      <string>Молотый (true)/в зернах(false)</string>
     </property>
    </column>
    <column>
     <property name="text">
      <string>Описание вкуса</string>
     </property>
    </column>
    <column>
     <property name="text">
      <string>Цена</string>
     </property>
    </column>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>1361</width>
     <height>22</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(temp)
        uic.loadUi(f, self)

        # self.buttons = [QPushButton(chr(i)) for i in range(1040, 1046)]
        # self.buttons += [QPushButton(chr(1025))]
        # self.buttons += [QPushButton(chr(i)) for i in range(1046, 1072)]

        self.con = sqlite3.connect("coffee.sqlite")
        self.cur = self.con.cursor()

        self.bar = QMainWindow.statusBar(self)
        self.bar.setGeometry(500, 500, 50, 50)
        self.initUI()

    def initUI(self):
        self.answer = self.cur.execute(f'SELECT * FROM "info_about_coffee"').fetchall()
        self.tableWidget.setRowCount(0)
        if not self.answer:
            self.bar.showMessage(f"Ничего не нашлось")
            return
        self.bar.showMessage(f"Нашлось {len(self.answer)} записей")
        for i in range(len(self.answer)):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j in range(len(self.answer[i])):
                # print(self.answer[i][j], end=" ")
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(self.answer[i][j])))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec_())
