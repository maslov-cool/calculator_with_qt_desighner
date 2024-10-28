import io
import sys

from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QMainWindow

template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>371</width>
    <height>565</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Красивый калькулятор</string>
  </property>
  <widget class="QWidget" name="layoutWidget">
   <property name="geometry">
    <rect>
     <x>20</x>
     <y>20</y>
     <width>345</width>
     <height>481</height>
    </rect>
   </property>
   <layout class="QVBoxLayout" name="verticalLayout">
    <item>
     <widget class="QLCDNumber" name="table"/>
    </item>
    <item>
     <layout class="QGridLayout" name="gridLayout">
      <item row="2" column="1">
       <widget class="QPushButton" name="btn8">
        <property name="minimumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="font">
         <font>
          <family>Helvetica</family>
          <pointsize>36</pointsize>
         </font>
        </property>
        <property name="text">
         <string>8</string>
        </property>
        <attribute name="buttonGroup">
         <string notr="true">buttonGroup_digits</string>
        </attribute>
       </widget>
      </item>
      <item row="0" column="1">
       <widget class="QPushButton" name="btn2">
        <property name="minimumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="font">
         <font>
          <family>Helvetica</family>
          <pointsize>36</pointsize>
         </font>
        </property>
        <property name="text">
         <string>2</string>
        </property>
        <attribute name="buttonGroup">
         <string notr="true">buttonGroup_digits</string>
        </attribute>
       </widget>
      </item>
      <item row="0" column="3">
       <widget class="QPushButton" name="btn_plus">
        <property name="minimumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="font">
         <font>
          <family>Helvetica</family>
          <pointsize>36</pointsize>
         </font>
        </property>
        <property name="text">
         <string>+</string>
        </property>
        <attribute name="buttonGroup">
         <string notr="true">buttonGroup_binary</string>
        </attribute>
       </widget>
      </item>
      <item row="3" column="2">
       <widget class="QPushButton" name="btn_eq">
        <property name="minimumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="font">
         <font>
          <family>Helvetica</family>
          <pointsize>36</pointsize>
         </font>
        </property>
        <property name="text">
         <string>=</string>
        </property>
       </widget>
      </item>
      <item row="3" column="0">
       <widget class="QPushButton" name="btn0">
        <property name="minimumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="font">
         <font>
          <family>Helvetica</family>
          <pointsize>36</pointsize>
         </font>
        </property>
        <property name="text">
         <string>0</string>
        </property>
        <attribute name="buttonGroup">
         <string notr="true">buttonGroup_digits</string>
        </attribute>
       </widget>
      </item>
      <item row="3" column="3">
       <widget class="QPushButton" name="btn_div">
        <property name="minimumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="font">
         <font>
          <family>Helvetica</family>
          <pointsize>36</pointsize>
         </font>
        </property>
        <property name="text">
         <string>/</string>
        </property>
        <attribute name="buttonGroup">
         <string notr="true">buttonGroup_binary</string>
        </attribute>
       </widget>
      </item>
      <item row="0" column="0">
       <widget class="QPushButton" name="btn1">
        <property name="minimumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="font">
         <font>
          <family>Helvetica</family>
          <pointsize>36</pointsize>
         </font>
        </property>
        <property name="text">
         <string>1</string>
        </property>
        <attribute name="buttonGroup">
         <string notr="true">buttonGroup_digits</string>
        </attribute>
       </widget>
      </item>
      <item row="2" column="2">
       <widget class="QPushButton" name="btn9">
        <property name="minimumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="font">
         <font>
          <family>Helvetica</family>
          <pointsize>36</pointsize>
         </font>
        </property>
        <property name="text">
         <string>9</string>
        </property>
        <attribute name="buttonGroup">
         <string notr="true">buttonGroup_digits</string>
        </attribute>
       </widget>
      </item>
      <item row="3" column="1">
       <widget class="QPushButton" name="btn_dot">
        <property name="minimumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="font">
         <font>
          <family>Helvetica</family>
          <pointsize>36</pointsize>
         </font>
        </property>
        <property name="text">
         <string>.</string>
        </property>
       </widget>
      </item>
      <item row="0" column="2">
       <widget class="QPushButton" name="btn3">
        <property name="minimumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="font">
         <font>
          <family>Helvetica</family>
          <pointsize>36</pointsize>
         </font>
        </property>
        <property name="text">
         <string>3</string>
        </property>
        <attribute name="buttonGroup">
         <string notr="true">buttonGroup_digits</string>
        </attribute>
       </widget>
      </item>
      <item row="1" column="0">
       <widget class="QPushButton" name="btn4">
        <property name="minimumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="font">
         <font>
          <family>Helvetica</family>
          <pointsize>36</pointsize>
         </font>
        </property>
        <property name="text">
         <string>4</string>
        </property>
        <attribute name="buttonGroup">
         <string notr="true">buttonGroup_digits</string>
        </attribute>
       </widget>
      </item>
      <item row="1" column="1">
       <widget class="QPushButton" name="btn5">
        <property name="minimumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="font">
         <font>
          <family>Helvetica</family>
          <pointsize>36</pointsize>
         </font>
        </property>
        <property name="text">
         <string>5</string>
        </property>
        <attribute name="buttonGroup">
         <string notr="true">buttonGroup_digits</string>
        </attribute>
       </widget>
      </item>
      <item row="2" column="0">
       <widget class="QPushButton" name="btn7">
        <property name="minimumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="font">
         <font>
          <family>Helvetica</family>
          <pointsize>36</pointsize>
         </font>
        </property>
        <property name="text">
         <string>7</string>
        </property>
        <attribute name="buttonGroup">
         <string notr="true">buttonGroup_digits</string>
        </attribute>
       </widget>
      </item>
      <item row="1" column="2">
       <widget class="QPushButton" name="btn6">
        <property name="minimumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="font">
         <font>
          <family>Helvetica</family>
          <pointsize>36</pointsize>
         </font>
        </property>
        <property name="text">
         <string>6</string>
        </property>
        <attribute name="buttonGroup">
         <string notr="true">buttonGroup_digits</string>
        </attribute>
       </widget>
      </item>
      <item row="1" column="3">
       <widget class="QPushButton" name="btn_minus">
        <property name="minimumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="font">
         <font>
          <family>Helvetica</family>
          <pointsize>36</pointsize>
         </font>
        </property>
        <property name="text">
         <string>-</string>
        </property>
        <attribute name="buttonGroup">
         <string notr="true">buttonGroup_binary</string>
        </attribute>
       </widget>
      </item>
      <item row="2" column="3">
       <widget class="QPushButton" name="btn_mult">
        <property name="minimumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="font">
         <font>
          <family>Helvetica</family>
          <pointsize>36</pointsize>
         </font>
        </property>
        <property name="text">
         <string>*</string>
        </property>
        <attribute name="buttonGroup">
         <string notr="true">buttonGroup_binary</string>
        </attribute>
       </widget>
      </item>
      <item row="4" column="0">
       <widget class="QPushButton" name="btn_pow">
        <property name="minimumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="font">
         <font>
          <family>Helvetica</family>
          <pointsize>36</pointsize>
         </font>
        </property>
        <property name="text">
         <string>^</string>
        </property>
        <attribute name="buttonGroup">
         <string notr="true">buttonGroup_binary</string>
        </attribute>
       </widget>
      </item>
      <item row="4" column="1">
       <widget class="QPushButton" name="btn_sqrt">
        <property name="minimumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="font">
         <font>
          <family>Helvetica</family>
          <pointsize>36</pointsize>
         </font>
        </property>
        <property name="text">
         <string>√</string>
        </property>
       </widget>
      </item>
      <item row="4" column="2">
       <widget class="QPushButton" name="btn_fact">
        <property name="minimumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="font">
         <font>
          <family>Helvetica</family>
          <pointsize>36</pointsize>
         </font>
        </property>
        <property name="text">
         <string>!</string>
        </property>
       </widget>
      </item>
      <item row="4" column="3">
       <widget class="QPushButton" name="btn_clear">
        <property name="minimumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="maximumSize">
         <size>
          <width>80</width>
          <height>80</height>
         </size>
        </property>
        <property name="font">
         <font>
          <family>Helvetica</family>
          <pointsize>36</pointsize>
         </font>
        </property>
        <property name="styleSheet">
         <string notr="true">background-color: rgb(254, 166, 43);</string>
        </property>
        <property name="text">
         <string>C</string>
        </property>
       </widget>
      </item>
     </layout>
    </item>
   </layout>
  </widget>
 </widget>
 <resources/>
 <connections/>
 <buttongroups>
  <buttongroup name="buttonGroup_digits"/>
  <buttongroup name="buttonGroup_binary"/>
 </buttongroups>
</ui>'''


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)  # Загружаем дизайн
        self.setWindowTitle('Красивый калькулятор')

        # цифры
        for i in self.buttonGroup_digits.buttons():
            i.clicked.connect(self.add_char)

        # точка
        self.btn_dot.clicked.connect(self.add_char)

        # +-*/**
        for i in self.buttonGroup_binary.buttons():
            i.clicked.connect(self.add_action)

        # С
        self.btn_clear.clicked.connect(self.clear_all)

        # =
        self.btn_eq.clicked.connect(self.result)

        # **
        self.btn_pow.clicked.connect(self.add_action)

        # ** 0.5
        self.btn_sqrt.clicked.connect(self.sqrt)

        # !
        self.btn_fact.clicked.connect(self.fact)

        self.value = ''
        self.expression = ''

        self.table.display(self.value)

    def count_fact(self, n):
        if n < 0 or int(n) != float(n):
            return -1
        elif n == 0:
            return 1
        return n * self.count_fact(n - 1)

    def fact(self):
        if self.expression:
            self.expression = f'self.count_fact({self.expression})'
            self.result()

    def sqrt(self):
        if self.expression:
            self.expression = f'({self.expression})**0.5'
            self.result()

    def clear_all(self):
        self.value = ''
        self.expression = ''
        self.table.display('')

    def add_char(self):
        if not (self.sender().text() == '.' and '.' in self.expression):
            if self.value != '0' or (self.value == '0' and self.sender().text() == '.'):
                self.value = self.value + self.sender().text()
                self.expression = self.expression + self.sender().text()
                self.table.display(self.value)
            else:
                self.value = self.sender().text()
                self.expression = self.sender().text()
                self.table.display(self.value)

    def result(self):
        try:
            self.value = eval(self.expression)
            self.expression = str(self.value)
            self.table.display(self.value)
        except Exception as _:
            self.table.display('Error')
        self.value = ''

    def add_action(self):
        if self.expression and self.expression[-2:] != '**':
            self.result()
            if self.expression[-1] not in '*/+-':
                self.expression += self.sender().text()
            else:
                self.expression = self.expression[:-1] + self.sender().text()

            self.expression = self.expression.replace('^', '**')
            return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
    sys.exit(app.exec())

