from enum import Enum, unique


@unique
class JapaneseDialect(Enum):
    Kyoto = "#Kyoto-ben"
    Osaka = "#Osaka-ben"
    Kansai = "#Kansai-ben"
    Kantou = "#Kantou-ben"
    Tosa = "#Tosa-ben"
    Touhoku = "#Touhoku-ben"
    Tsugaru = "#Tsugaru-ben"
    Kyushu = "#Kyushu-ben"
    Ryukyu = "#Ryukyu-ben"
    Nagano = "#Nagano-ben"
    Hokkaido = "#Hokkaido-ben"
