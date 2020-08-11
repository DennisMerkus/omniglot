import unittest

import pytest
from bs4 import BeautifulSoup

from omniglot.haw.mamaka import HawaiianPOS, MamakaEntry, parse_entry


class TestMamaka(unittest.TestCase):
    @pytest.mark.asyncio
    async def test_aniani_paiki(self):
        entry = """
        <p align="Justify"><span class="head">ani·ani pāiki</span> <i>kik</i> Small mirror kept in a purse. Also <i>aniani liʻiliʻi.</i>\n</p>
        """

        parsed_entry = parse_entry(BeautifulSoup(entry).find("p"))

        self.assertEqual(
            parsed_entry,
            MamakaEntry(
                head="aniani pāiki",
                syllables="ani·ani pāiki",
                pos=HawaiianPOS.kikino,
                dictionary=False,
                definition="Small mirror kept in a purse",
                also=["aniani liʻiliʻi"],
            ),
        )

    @pytest.mark.asyncio
    async def test_kaohi_meaola(self):
        entry = """
        <p align="justify"><span class="head">kāohi  mea·ola</span> <i>ham</i> Biological control. <i>ʻO ke kāohi meaola kekahi mea e noʻonoʻo ʻia nei no ke kāohi ʻana i nā lāʻau a me nā holoholona malihini e hoʻopilikia nei i nā kaiapuni ʻōiwi o Hawaiʻi. </i> Biological control is one method being considered to control introduced plants and animals that are damaging native environments in Hawaiʻi. <i>Lit.,</i> control living things.\n</p>
        """

        parsed_entry = parse_entry(BeautifulSoup(entry).find("p"))

        self.assertEqual(
            parsed_entry,
            MamakaEntry(
                head="kāohi meaola",
                syllables="kāohi mea·ola",
                pos=HawaiianPOS.hamani,
                dictionary=False,
                literally="control living things",
                definition="Biological control",
                examples={
                    "ʻO ke kāohi meaola kekahi mea e noʻonoʻo ʻia nei no ke kāohi ʻana i nā lāʻau a me nā holoholona malihini e hoʻopilikia nei i nā kaiapuni ʻōiwi o Hawaiʻi": "Biological control is one method being considered to control introduced plants and animals that are damaging native environments in Hawaiʻi"
                },
            ),
        )

    @pytest.mark.asyncio
    async def test_aukahi(self):
        entry = """
        <p align="Justify"><span class="head">au·kahi</span>   <i>heh</i> Direct current (DC). <i>Dic., ext. mng.</i> Cf. <i>au māʻaloʻalo.  Uila aukahi.</i> Direct current electricity. <i>Mālamalama aukahi.</i> Coherent light, i.e. light in which all the waves vibrate in a single plane with the crests and troughs all aligned.\n</p>
        """

        parsed_entry = parse_entry(BeautifulSoup(entry).find("p"))

        self.assertEqual(
            parsed_entry,
            MamakaEntry(
                head="aukahi",
                syllables="au·kahi",
                pos=HawaiianPOS.hehele,
                dictionary=True,
                definition="Direct current (DC)",
                compare=["au māʻaloʻalo"],
                examples={
                    "Uila aukahi": "Direct current electricity",
                    "Mālamalama aukahi": "Coherent light, i.e. light in which all the waves vibrate in a single plane with the crests and troughs all aligned",
                },
            ),
        )

    @pytest.mark.asyncio
    async def test_pohoalo(self):
        entry = """
        <p align="justify"><span class="head">poho·alo</span> <i>ʻaʻ</i> Forehand, i.e. with palms facing forward. Comb. <i>poho + alo.</i> Cf. <i>pohokua.</i> See <i>hukialewa, kīpehi.</i>\n</p>
        """

        parsed_entry = parse_entry(BeautifulSoup(entry).find("p"))

        print(parsed_entry)

        self.assertEqual(
            parsed_entry,
            MamakaEntry(
                head="pohoalo",
                syllables="poho·alo",
                pos=HawaiianPOS.a,
                dictionary=False,
                definition="Forehand, i.e. with palms facing forward",
                compare=["pohokua"],
                combined=["poho", "alo"],
                see=["hukialewa", "kīpehi"],
            ),
        )
