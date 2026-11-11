-- Indholdet af ::: paahovedet ::: sættes på hovedet i PDF'en (løsninger, man skal vende papiret for at læse).
-- OBS: En løsning på hovedet kan ikke deles over to sider, og tabeller i en løsning virker ikke (longtable i minipage).
function Div(el)
  if not el.classes:includes('paahovedet') then return nil end
  local ud = { pandoc.RawBlock('latex', '\\par\\medskip\\noindent\\begin{center}\\begin{turn}{180}\\begin{minipage}{0.92\\linewidth}\\setlength{\\parskip}{4pt}') }
  for _, b in ipairs(el.content) do table.insert(ud, b) end
  table.insert(ud, pandoc.RawBlock('latex', '\\end{minipage}\\end{turn}\\end{center}\\medskip'))
  return ud
end
