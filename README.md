<img src="https://raw.githubusercontent.com/wandrewtischlerx/deviceinfo/main/IMAGENS/deviceinfo.PNG" alt="DeviceInfo">


<h1>DeviceInfo v1.0</h1>

---

DeviceInfo é uma ferramenta abrangente para coletar e exibir informações detalhadas sobre o sistema e a rede. Desenvolvida para administradores de sistemas e profissionais de TI, esta ferramenta fornece dados essenciais como configurações do hardware, estado da bateria, informações de disco, interfaces de rede e a rotação do cooler do dispositivo. Além disso, o DeviceInfo consulta uma API para obter dados de geolocalização com base no endereço IP, facilitando a análise e monitoramento remoto. Através de uma interface colorida e amigável, o DeviceInfo torna a coleta de dados do sistema rápida e eficiente, com relatórios claros e acessíveis.



<h2>Instalação:</h2>

```
git clone https://github.com/wandrewtischlerx/deviceinfo.git
cd deviceinfo
pip install -r requirements.txt
```

<h2>Retorna:</h2>

   - Nome do Dispositivo: Nome do computador ou dispositivo.
   - Sistema Operacional: Nome do sistema operacional em execução.
   - Versão do SO: Versão do sistema operacional.
   - Arquitetura do SO: Arquitetura do sistema operacional (32-bit ou 64-bit) e o tipo de arquitetura.
   - Usuário: Nome do usuário atualmente logado no sistema.
   - Processador: Nome e modelo do processador.
   - Número de Núcleos: Quantidade total de núcleos lógicos do processador.
   - Frequência do CPU: Frequência atual do processador em MHz.
   - Memória RAM Total: Quantidade total de memória RAM disponível.
   - Status da Bateria: Percentual de carga da bateria.
   - Carregando: Indica se a bateria está sendo carregada ou não.
   - Tempo Restante: Tempo estimado restante até a bateria esgotar ou carregar completamente.
   - Discos: Detalhes sobre tamanho total, espaço usado, espaço livre e sistema de arquivos.
   - Interfaces de Rede: Endereços IP e máscaras de sub-rede para cada interface de rede no sistema.
   - Data e Hora Local: Data e hora atuais do sistema.
   - RPM do Cooler: Rotação atual do cooler do sistema em RPM, se disponível.
   - Endereço IP: Endereço IP público do sistema.
   - País: País de origem do IP.
   - Estado: Estado ou região do IP.
   - Cidade: Cidade do IP.
   - Provedor de Internet: Provedor de serviços de internet associado ao IP.
   - Coordenadas: Latitude e longitude associadas ao IP.
   - Link do Google Maps: Se as coordenadas de geolocalização estiverem disponíveis, um link direto para o local no Google Maps.

<h2>Contribuições:</h2>

Contribuições são bem-vindas! Para sugerir melhorias ou reportar problemas, por favor abra uma issue ou envie um pull request.

<h2>Licença:</h2>

Este projeto está licenciado sob a MIT License (https://opensource.org/licenses/MIT).

---

Desenvolvido por Wandrew Tischler
