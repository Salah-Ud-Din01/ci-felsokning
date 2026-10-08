# CI-felsökning: få pipelinen grön

Den här pipelinen är trasig på flera ställen. Ditt jobb är att få den grön, ett fel i taget, och skriva ner vad du lär dig. Övningen handlar om att *läsa* en misslyckad körning, inte om att gissa.

## Kom igång

1. Klicka på **Use this template** högst upp på den här sidan och välj **Create a new repository**.
   - Ge repot ett eget namn, till exempel `ci-felsokning`.
   - Välj **Public**. Actions är gratis att köra i publika repon.
2. Klona **ditt eget** repo, inte mallen:
   ```bash
   git clone https://github.com/<ditt-användarnamn>/ci-felsokning.git
   ```
3. Öppna fliken **Actions** i ditt repo och se vad som har hänt.

> Klona inte mallen direkt. Då blir mallen din `origin`, och dina ändringar kan inte pushas dit.

Lägg aldrig något hemligt i ett publikt repo. Den här övningen behöver inga lösenord eller nycklar.

## Så arbetar du

1. Läs loggen från den senaste körningen. Börja vid det första röda steget.
2. Rätta **ett** fel i taget. Gissa inte på flera saker samtidigt.
3. Committa och pusha till `main`. Vänta på nästa körning.
4. Skriv en rad i `FELLOGG.md` för varje fel.
5. Upprepa tills körningen är grön.

Du får köra samma kommandon lokalt som workflowet kör. De står i `.github/workflows/ci.yml`. Du behöver [uv](https://docs.astral.sh/uv/) installerat.

Fastnar du: läs [felsökningsguiden](docs/felsokningsguide.pdf) (finns också under Kursmaterial i portalen), och fråga oss på lektionen.

## Klar när

Fliken Actions visar en grön bock på din senaste commit på `main`, och `FELLOGG.md` har en rad för varje fel du hittade.
