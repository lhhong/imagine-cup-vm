import sys  
from PyQt5.QtGui import *  
from PyQt5.QtCore import *  
#from PyQt5.QtWebKit import *  
from PyQt5.QtWebKitWidgets import QWebPage
from PyQt5.QtWidgets import QApplication
from lxml import html 

#Take this class for granted.Just use result of rendering.
class Render(QWebPage):  
  def __init__(self, url):  
    self.app = QApplication(sys.argv)  
    QWebPage.__init__(self)  
    self.loadFinished.connect(self._loadFinished)  
    self.mainFrame().load(QUrl(url))  
    self.app.exec_()  
  
  def _loadFinished(self, result):  
    self.frame = self.mainFrame()  
    self.app.quit()  

url = 'http://www.asos.com/asics/asics-gel-kayano-evo-trainers-in-black-h707n-9090/prd/7592389?iid=7592389&clr=Black&cid=4209&pgesize=36&pge=0&totalstyles=2160&gridsize=3&gridrow=2&gridcolumn=1'  

r = Render(url)
result = r.frame.toHtml()

print (result)
#This step is important.Converting QString to Ascii for lxml to process
#QString should be converted to string before processed by lxml
#formatted_result = str(result.toAscii())
formatted_result = str(result.encode('utf-8'))

#Next build lxml tree from formatted_result
tree = html.fromstring(formatted_result)

#Now using correct Xpath we are fetching URL of archives
archive_links = tree.xpath('//div[@class="product-price"]')

print (archive_links)
