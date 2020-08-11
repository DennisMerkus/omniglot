import unittest

import pytest
from bs4 import BeautifulSoup

from omniglot.mul.freedict import FreedictEntry, parse_freedict_entry


class TestFreedict(unittest.TestCase):
    @pytest.mark.asyncio
    async def test_por_merenda(self):
        entry = """
         <entry>
            <form>
               <orth>merenda</orth>
            </form>
            <sense>
               <cit type="trans">
                  <quote>lunch</quote>
               </cit>
               <cit type="trans">
                  <quote>snack</quote>
               </cit>
            </sense>
         </entry>
         """

        parsed_entry = parse_freedict_entry(BeautifulSoup(entry, "lxml-xml"))

        self.assertEqual(
            parsed_entry,
            FreedictEntry(orthography=["merenda"], senses=[["lunch", "snack"]]),
        )

    @pytest.mark.asyncio
    async def test_por_mostrar_se(self):
        entry = """
         <entry>
            <form>
               <orth>mostrar-se</orth>
            </form>
            <sense n="1">
               <cit type="trans">
                  <quote>point out to be</quote>
               </cit>
            </sense>
            <sense n="2">
               <cit type="trans">
                  <quote>appear</quote>
               </cit>
               <cit type="trans">
                  <quote>appear to be</quote>
               </cit>
               <cit type="trans">
                  <quote>seem</quote>
               </cit>
            </sense>
         </entry>
         """

        parsed_entry = parse_freedict_entry(BeautifulSoup(entry, "lxml-xml"))

        self.assertEqual(
            parsed_entry,
            FreedictEntry(
                orthography=["mostrar-se"],
                senses=[["point out to be"], ["appear", "appear to be", "seem"],],
            ),
        )

    @pytest.mark.asyncio
    async def test_fra_abords(self):
        entry = """
        <entry>
            <form>
                <orth>abords</orth>
                <pron>abɔʀ</pron>
            </form>
            <gramGrp>
                <pos>n</pos>
                <gen>masc</gen>
            </gramGrp>
            <sense>
                <cit type="trans">
                    <quote>environment</quote>
                </cit>
                <cit type="trans">
                    <quote>environs</quote>
                </cit>
                <cit type="trans">
                    <quote>surroundings</quote>
                </cit>
            </sense>
        </entry>
        """

        parsed_entry = parse_freedict_entry(BeautifulSoup(entry, "lxml-xml"))

        self.assertEqual(
            parsed_entry,
            FreedictEntry(
                orthography=["abords"],
                pronunciation="abɔʀ",
                pos="n",
                gender="masc",
                senses=[["environment", "environs", "surroundings"]],
            ),
        )
