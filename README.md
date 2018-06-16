# PZEM004T to EmonCMS with Raspberry Pi

**Table of Contents**   
1. [Intro](#id1)
2. [Hardware](#id2)
3. [Software](#id3)
5. [Example](#id4)

## Intro <a name="id1"></a>

Due to having spare parts at home, I decided to use one of my raspberry's to read the PZEM004t values and then post them to EmonCMS. It can be done in a different way, using a esp8266 shield but for this you would have to buy more pieces, you can see this alternative here: [https://github.com/apreb/eNode](https://github.com/apreb/eNode)

The worker will send for each second the Current (A) and the Power (W) to the EmonCMS. It will catch the errors and send it to the errbit ([airbrake](https://airbrake.io/)) service.

## Hardware <a name="id2"></a>

1. PZEM004t with serial usb cable
2. Raspberry Pi or similar 

## Software <a name="id3"></a>

1. EmonCMS service (it can be the emonpi)
2. Python Packages required for the worker.py
3. Optional [airbrake](https://airbrake.io/) or [errbit](https://github.com/errbit/errbit) service
4. Optional OPENVPN serice with [pivpn](http://www.pivpn.io/)

### Installation

$ pip3 install -r requirements.txt

$ clone the config_example.json to config.json and edit it

$ install the screen  (apt-get install -y screen) and create a session (screen -R emonpzem)

$ python3 worker.py

## Example <a name="id4"></a>

![](https://lh3.googleusercontent.com/2QtfA8QGjI7raH9-i-POiRhzQJlmA6fkcCajB3s7dmDfeVntMgdOb5xQXVHxI93NJUQjVJdXIKEYMRPYrsnOiLVVYcdG91dXQvCK2979sU962a00n5xj5SLCtwreNw6HtYLhK5yL03iWBhK1f3NyR_sE-8S0afXudHRJ64iiCBVXQYlwJcGP4AiO6Ts-EZgTyHWQOKCTDs_5bvpK0wPlR1ntgE0mV9g40pMqS0K9POxwbvg3mI99iR6lhCN--sTdkfgbvsVAFb3iLmYszBbPc1B0nH4n1ub-2BldhjTp61aSj2xpMYPtrAjqy3_15BYvVLj9aFuXYznrgbm6c7Ir5BrgCRlnbF8VO3ymi1_IZ2AbPCN2fhRqj0Yh9RC-04mo-1XwtlRa3k5_wQlMFD1dAZ8ONJfnzfGe3I9MXhaEBeqIjaJYBcXBkZEYrOalfRFFx9yx4vLJg4qJ20CRop7rrcFcmlWN0R_xtSn2kervoFu2clTBTzILjPccTxQ41MpAQBq0vqmFyNEC0wTNjAGA1AgOFlILu3V834iAaymgqJ8N_O4j6SH1ACkeSwF-UqfH=w1859-h873)

![](https://lh3.googleusercontent.com/NQ4EzJzcKXlewuS2qCZ-sh5yuBg0AJW35kGtbbkoXzk2Td5UHcGKbnp_n09WQ3iQc-RHrCneXHnSN91AFnmWfXiadLe66GRsJOCFSW1hEDoWGwHzAG8b8WML3cVWNPf1PQiGzqlBE2GgPcKJzeK_e6dBG7UaLdYEngNqMByvzwmVGWMt7hgY6GO6mVIElrRNOjQVulOXH02vGPJ7_OobXxKru4wZReL8pEDAMmNnTecCDKnNNUzP69clR2BdtngToh1eoXR_zxw5FCaotU5c-5mYMEzUm968PNGXOc8CEgfsGASVZssRlZLb5wllI0_WZaQNN01yoOOB2kc284PE1nD2SIuYLIOcBMijUnAtGBG6HObnjGZxhaR9deoTFBYVaABWKU37EFh8kaGeoOCqLnrWw_48N6TkxwUJj2r0e7Aqg2q-g-S7xI4wzjOYMFD40HEPKISrlmslDnn6-vZmwBT7Cbn-g9j-B9PtmxDF9FZbdr5PmgBZ0Fvw14Ax4OfGhIdNzrLVHgSfjRUW4RU62u5UwK7NFl2EwMxUKyaKAiUnmEozg-zIRBiWCqRRPSHp=w1859-h873)

![](https://lh3.googleusercontent.com/dYIppZz0nAtrU2xBlEfya2VtZXXdjWaQ12VhrjJXHyLPDE8IvAudhNbTNZysoDK-LQnYCQQ8s_P48gFn8vHcUu1U5KIK34JWCZIZsGa8vpwG4HWvvV75SNZyaQJWcQzCJxv3WOa35nO7amQTU5AeEdyN04b5awOKYJl7pgZiNSQOs1o2-KfWt99Wz5_ckd8v-2SHRaJiAtxRGDJDNzilmxr9dDgOzrD9Thi6R8JbfOp3RIq9PbrgfiK3-FTTT5EOpUr5Teqy5JiJRErn6SlXckGP6-ZFQ2tBJRvXQ3mdc22TTqrIZu3sHRig4A6fsD0IsKMXnz8qBaIx8GbIv64s1klvrQ6JOS7zEyvmXtWCbGPFQL3KN0dEhpoSMVNiraAK4z7NiNYDMkiN97eBVIrPuMtEVtSjoqmC0IFMfmbS70pZV5zLcTVSigOaElO1K_Ps5BXMVOanFVHaUmdJ-e-QVnGR6UX5Xb1jys0bbE30Pnqni3EXhNRBOI6MGti3I_sDFtBFeW15BToa-e5QJJe5ZAqdngbKEk-ARpLb2D_orSA37im3WNqqMaorrFKOn4gj=w1859-h873)

![](https://lh3.googleusercontent.com/6WWiY4uVX_Tk78dyukvAeOg2_rMjuB-3TlZbjzNSe_J15VgxDmpxWTe8XPka_Yx5qesDrt1DWQdR1NiKxuvlJGzv-6jp2guF3spv7luimEIOYrQQJp89I7CqwsM96bmM_s08gERVqmXBXiXS3NLEGjL2zEwMhI3a2QmuLIjOoFE51xahqz9KiidW8KjR3UtrdbP-mMJoO4Luow1iHZRDsgLcGGoLRRMCvV4WfuqXdeJPRfme-jo39DmfJOhsECiyTBvh2A330_ltvzxWeROSF_lA2zL6ONIJ8etMQ_HzB5WUsI3r7yW5MclE2roEiU2ugcODjpNdUbbZt42EHrwW9dpNsb4NDtClnxaxBu-HxTmETS6K0ZllYlfBz1tjHKMvfMmfHzEylYXwZVuFGbiZeRxBtaUiNv_VHzkx_mqd8exTbfKrX_If_Wt-GWTc4dEG9gnT1WVNqJN2yOmpiMOISsQO4XXj1OQ7sMUpUIS6d7NpCExI9atPcNcClOp720mfDUc3aXrGtUkPeJqnskhDbqCUBEEvP2lSLrp4OKbIUoaufSC8pu9XtR3_Rpaezhbe=w1859-h873)
