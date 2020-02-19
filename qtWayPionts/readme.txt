if we set origin point by read the data feom yaml:

    def on_set_zero(self):
        self.lineEdit_zero_x.setEnabled(False)
        self.lineEdit_zero_y.setEnabled(False)
        self.zero_x = float(self.lineEdit_zero_x.text())*(-1)
        self.zero_y = float(float(self.lineEdit_zero_y.text())*(-1)-self.img_y)


if we set the origin point by double click :

      def on_set_zero(self):
        self.lineEdit_zero_x.setEnabled(False)
        self.lineEdit_zero_y.setEnabled(False)
        self.zero_x = float(self.lineEdit_zero_x.text())
        self.zero_y = float(float(self.lineEdit_zero_y.text()))
