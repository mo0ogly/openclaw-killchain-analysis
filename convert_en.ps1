$word = New-Object -ComObject Word.Application
$doc = $word.Documents.Open("C:\Users\pizzif\Documents\GitHub\openclaw-killchain-analysis\S1-ISI5_AI_and_Cybersecurity_v6_EN.docx")
$path = "C:\Users\pizzif\Documents\GitHub\openclaw-killchain-analysis\S1-ISI5_IA_et_Cybersecurite v6_en.pdf"
$doc.SaveAs([ref] $path, [ref] 17)
$doc.Close()
$word.Quit()
