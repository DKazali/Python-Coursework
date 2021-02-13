from engine import *

E = Engine()
E.start()

#  Понеже програмата ми е с графичен интерфейс, не мога да имам 3 функции в main.py. Просто няма какво друго да добавя.
#  Пробвах няколко варианта да имам 3 функции, но нито един от тях не се получи.
#   Първо питах се да добавя boolean променлива в engine.py, наречена to_ms (to mode selection) и в "раздела" със
#  статистиката да имам бутон To Mode Selection който изтрива всички widget-и и променя стойността на to_ms на true
#  след това в main имах следния код if E.to_ms: E.Start() /n E.to_ms = False, като така се започва от начало,
#  но след като програмата изпълнеше кода на метода to_mode_selection() (в този метод се задаваше стойността на to_ms
#  да е true), тя зацикляше. Тоест в main.py всичко след командата на 7-ми ред - E.start() неможеше да се изпълни.
#   Другото нещо което пробвах е в engine.py, в метода to_mode_selection да унищожа целия прозорец чрез следния
#  код self.window.destroy() и в метода start() да го създам на ново. Това позволи изпълнението на командите след
#  E.Start() в main.py и така чрез if E.to_ms: E.Start() /n E.to_ms = False стартирах отначало програмата.
#  Проблема беше, че ми излезе следната грешка:
#  invalid command name ".!button 2"
#  while executing "$wget -state"
#  (procedure "tk::Button Down" line 12)
#  invoked from within "tk::Button Down .!button2"
#  (command bound to event)
#  Като така след натискането на бутона To Mode Selection програмата се изключваше. За това от main се стартира
#  програмата чрез метода start(), а всички останали методи в engine.py се повикват от други методи в същия клас.


