from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional,Union

class Product(BaseModel):
    isim: str
    fiyat: float
    stok: int
    kategori : Union[str,None] = None
    stoktavar : Optional[bool] = None

app = FastAPI()

@app.get("/")  ##get veriyi çekerken
def read_root():
    return {"output":"Umutsuz Durum Yoktur Umutsuz insanlar vardır",
            "durum":True,
            "tarih":None
            }
@app.get("/soz/{kisi}")
def soz(kisi: str):
    sozler = {
        "ataturk" : "Umutsuz Durum Yoktur Umutsuz insanlar vardır",
        "mevlana" : "Düşünceleriniz szöleriniz davranaşlarınız",
        "nietszche" : "Beni öldürmeyen şey güçlendirir",
        "tesla" : "Hayl gücü her şeydir Hayal gücü geleceğin önizlemesidr"
    }

    cikti = sozler.get(kisi.lower())
    return {"output":cikti}


@app.post("/urun/")
def urun(urun: Product):
    urun_dict = urun.dict()
    urun.stok = max(0,urun.stok)
    urun_dict.update({"stok":urun.stok})
    urun_dict.update({"stoktavar":urun.stok > 0})
    return {"output":urun_dict}