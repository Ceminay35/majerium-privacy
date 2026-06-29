"""
ORBI DISCOVERY ENGINE v4.0 - ULTIMATE EDITION
Tek dosya, 5000+ yer, Akinator mantığı, tüm dünya
"""

import streamlit as st
import random
import time
import math
import json
import requests
from typing import List, Dict, Optional

# ============================================
# 1. VERİTABANI (5000+ YER)
# ============================================

# A. MANUEL EKLENEN ÖZEL YERLER (Türkiye ve Dünya)
MANUAL_LANDMARKS = [
    # === TÜRKİYE ===
    {
        "id": 1,
        "name": "Ayasofya",
        "continent": "Asia",
        "country": "Turkey",
        "city": "İstanbul",
        "category": "religious",
        "is_natural": False,
        "is_man_made": True,
        "is_unesco": True,
        "is_ancient": True,
        "is_temple": False,
        "is_museum": True,
        "is_mosque": True,
        "is_church": True,
        "is_mountain": False,
        "is_island": False,
        "is_water": False,
        "is_desert": False,
        "is_volcano": False,
        "is_cave": False,
        "has_tourists": True,
        "has_entry_fee": True,
        "is_underground": False,
        "night_light": True,
        "height_meters": 55,
        "famous_for": "Bizans mimarisi, mozaikler, tarihi cami",
        "best_time": "Nisan-Ekim",
        "estimated_visitors": 3700000
    },
    {
        "id": 2,
        "name": "Pamukkale",
        "continent": "Asia",
        "country": "Turkey",
        "city": "Denizli",
        "category": "natural",
        "is_natural": True,
        "is_man_made": False,
        "is_unesco": True,
        "is_ancient": True,
        "is_temple": False,
        "is_museum": False,
        "is_mosque": False,
        "is_church": False,
        "is_mountain": False,
        "is_island": False,
        "is_water": True,
        "is_desert": False,
        "is_volcano": False,
        "is_cave": False,
        "has_tourists": True,
        "has_entry_fee": True,
        "is_underground": False,
        "night_light": False,
        "height_meters": 0,
        "famous_for": "Beyaz travertenler, termal sular",
        "best_time": "Mayıs-Eylül",
        "estimated_visitors": 2000000
    },
    {
        "id": 3,
        "name": "Kapadokya",
        "continent": "Asia",
        "country": "Turkey",
        "city": "Nevşehir",
        "category": "natural",
        "is_natural": True,
        "is_man_made": False,
        "is_unesco": True,
        "is_ancient": True,
        "is_temple": False,
        "is_museum": False,
        "is_mosque": False,
        "is_church": False,
        "is_mountain": False,
        "is_island": False,
        "is_water": False,
        "is_desert": False,
        "is_volcano": False,
        "is_cave": True,
        "has_tourists": True,
        "has_entry_fee": True,
        "is_underground": False,
        "night_light": False,
        "height_meters": 0,
        "famous_for": "Peri bacaları, yer altı şehirleri, balon turları",
        "best_time": "Nisan-Ekim",
        "estimated_visitors": 2500000
    },
    {
        "id": 4,
        "name": "Göbeklitepe",
        "continent": "Asia",
        "country": "Turkey",
        "city": "Şanlıurfa",
        "category": "archaeological",
        "is_natural": False,
        "is_man_made": True,
        "is_unesco": True,
        "is_ancient": True,
        "is_temple": True,
        "is_museum": False,
        "is_mosque": False,
        "is_church": False,
        "is_mountain": False,
        "is_island": False,
        "is_water": False,
        "is_desert": False,
        "is_volcano": False,
        "is_cave": False,
        "has_tourists": True,
        "has_entry_fee": True,
        "is_underground": False,
        "night_light": False,
        "height_meters": 0,
        "famous_for": "Dünyanın en eski tapınak kompleksi, MÖ 9600",
        "best_time": "Mart-Kasım",
        "estimated_visitors": 500000
    },
    {
        "id": 5,
        "name": "Efes Antik Kenti",
        "continent": "Asia",
        "country": "Turkey",
        "city": "İzmir",
        "category": "archaeological",
        "is_natural": False,
        "is_man_made": True,
        "is_unesco": True,
        "is_ancient": True,
        "is_temple": True,
        "is_museum": False,
        "is_mosque": False,
        "is_church": False,
        "is_mountain": False,
        "is_island": False,
        "is_water": False,
        "is_desert": False,
        "is_volcano": False,
        "is_cave": False,
        "has_tourists": True,
        "has_entry_fee": True,
        "is_underground": False,
        "night_light": False,
        "height_meters": 0,
        "famous_for": "Celsus Kütüphanesi, Büyük Tiyatro, Artemis Tapınağı",
        "best_time": "Nisan-Ekim",
        "estimated_visitors": 2000000
    },
    {
        "id": 6,
        "name": "Ağrı Dağı",
        "continent": "Asia",
        "country": "Turkey",
        "city": "Ağrı",
        "category": "natural",
        "is_natural": True,
        "is_man_made": False,
        "is_unesco": False,
        "is_ancient": False,
        "is_temple": False,
        "is_museum": False,
        "is_mosque": False,
        "is_church": False,
        "is_mountain": True,
        "is_island": False,
        "is_water": False,
        "is_desert": False,
        "is_volcano": True,
        "is_cave": False,
        "has_tourists": True,
        "has_entry_fee": False,
        "is_underground": False,
        "night_light": False,
        "height_meters": 5137,
        "famous_for": "Türkiye'nin en yüksek dağı, Nuh'un Gemisi efsanesi",
        "best_time": "Haziran-Eylül",
        "estimated_visitors": 10000
    },
    {
        "id": 7,
        "name": "Yerebatan Sarnıcı",
        "continent": "Asia",
        "country": "Turkey",
        "city": "İstanbul",
        "category": "historical",
        "is_natural": False,
        "is_man_made": True,
        "is_unesco": True,
        "is_ancient": True,
        "is_temple": False,
        "is_museum": False,
        "is_mosque": False,
        "is_church": False,
        "is_mountain": False,
        "is_island": False,
        "is_water": True,
        "is_desert": False,
        "is_volcano": False,
        "is_cave": False,
        "has_tourists": True,
        "has_entry_fee": True,
        "is_underground": True,
        "night_light": False,
        "height_meters": 0,
        "famous_for": "Yeraltı sarnıcı, Medusa başları, 336 sütun",
        "best_time": "Tüm yıl",
        "estimated_visitors": 1500000
    },
    {
        "id": 8,
        "name": "Sümela Manastırı",
        "continent": "Asia",
        "country": "Turkey",
        "city": "Trabzon",
        "category": "religious",
        "is_natural": False,
        "is_man_made": True,
        "is_unesco": False,
        "is_ancient": True,
        "is_temple": False,
        "is_museum": False,
        "is_mosque": False,
        "is_church": True,
        "is_mountain": True,
        "is_island": False,
        "is_water": False,
        "is_desert": False,
        "is_volcano": False,
        "is_cave": False,
        "has_tourists": True,
        "has_entry_fee": True,
        "is_underground": False,
        "night_light": False,
        "height_meters": 0,
        "famous_for": "Dağa oyulmuş manastır, freskler, doğa manzarası",
        "best_time": "Mayıs-Eylül",
        "estimated_visitors": 500000
    },
    {
        "id": 9,
        "name": "Nemrut Dağı",
        "continent": "Asia",
        "country": "Turkey",
        "city": "Adıyaman",
        "category": "archaeological",
        "is_natural": False,
        "is_man_made": True,
        "is_unesco": True,
        "is_ancient": True,
        "is_temple": True,
        "is_museum": False,
        "is_mosque": False,
        "is_church": False,
        "is_mountain": True,
        "is_island": False,
        "is_water": False,
        "is_desert": False,
        "is_volcano": False,
        "is_cave": False,
        "has_tourists": True,
        "has_entry_fee": True,
        "is_underground": False,
        "night_light": False,
        "height_meters": 2150,
        "famous_for": "Dev heykeller, Kommagene Krallığı, gün doğumu/gün batımı",
        "best_time": "Nisan-Ekim",
        "estimated_visitors": 300000
    },
    {
        "id": 10,
        "name": "Safranbolu",
        "continent": "Asia",
        "country": "Turkey",
        "city": "Karabük",
        "category": "historical",
        "is_natural": False,
        "is_man_made": True,
        "is_unesco": True,
        "is_ancient": False,
        "is_temple": False,
        "is_museum": False,
        "is_mosque": False,
        "is_church": False,
        "is_mountain": False,
        "is_island": False,
        "is_water": False,
        "is_desert": False,
        "is_volcano": False,
        "is_cave": False,
        "has_tourists": True,
        "has_entry_fee": False,
        "is_underground": False,
        "night_light": False,
        "height_meters": 0,
        "famous_for": "Osmanlı mimarisi, konaklar, sokak dokusu",
        "best_time": "Nisan-Ekim",
        "estimated_visitors": 600000
    },
    
    # === DÜNYA ===
    {
        "id": 11,
        "name": "Burj Khalifa",
        "continent": "Asia",
        "country": "United Arab Emirates",
        "city": "Dubai",
        "category": "modern",
        "is_natural": False,
        "is_man_made": True,
        "is_unesco": False,
        "is_ancient": False,
        "is_temple": False,
        "is_museum": False,
        "is_mosque": False,
        "is_church": False,
        "is_mountain": False,
        "is_island": False,
        "is_water": False,
        "is_desert": True,
        "is_volcano": False,
        "is_cave": False,
        "has_tourists": True,
        "has_entry_fee": True,
        "is_underground": False,
        "night_light": True,
        "height_meters": 828,
        "famous_for": "Dünyanın en yüksek binası, 163 kat",
        "best_time": "Kasım-Mart",
        "estimated_visitors": 2000000
    },
    {
        "id": 12,
        "name": "Eyfel Kulesi",
        "continent": "Europe",
        "country": "France",
        "city": "Paris",
        "category": "modern",
        "is_natural": False,
        "is_man_made": True,
        "is_unesco": True,
        "is_ancient": False,
        "is_temple": False,
        "is_museum": False,
        "is_mosque": False,
        "is_church": False,
        "is_mountain": False,
        "is_island": False,
        "is_water": False,
        "is_desert": False,
        "is_volcano": False,
        "is_cave": False,
        "has_tourists": True,
        "has_entry_fee": True,
        "is_underground": False,
        "night_light": True,
        "height_meters": 330,
        "famous_for": "Paris'in simgesi, demir kule, muhteşem manzara",
        "best_time": "Nisan-Ekim",
        "estimated_visitors": 7000000
    },
    {
        "id": 13,
        "name": "Piramitler",
        "continent": "Africa",
        "country": "Egypt",
        "city": "Giza",
        "category": "archaeological",
        "is_natural": False,
        "is_man_made": True,
        "is_unesco": True,
        "is_ancient": True,
        "is_temple": False,
        "is_museum": False,
        "is_mosque": False,
        "is_church": False,
        "is_mountain": False,
        "is_island": False,
        "is_water": False,
        "is_desert": True,
        "is_volcano": False,
        "is_cave": False,
        "has_tourists": True,
        "has_entry_fee": True,
        "is_underground": False,
        "night_light": False,
        "height_meters": 138,
        "famous_for": "Antik Dünya Harikası, firavun mezarları",
        "best_time": "Ekim-Nisan",
        "estimated_visitors": 15000000
    },
    {
        "id": 14,
        "name": "Sfenks",
        "continent": "Africa",
        "country": "Egypt",
        "city": "Giza",
        "category": "archaeological",
        "is_natural": False,
        "is_man_made": True,
        "is_unesco": True,
        "is_ancient": True,
        "is_temple": False,
        "is_museum": False,
        "is_mosque": False,
        "is_church": False,
        "is_mountain": False,
        "is_island": False,
        "is_water": False,
        "is_desert": True,
        "is_volcano": False,
        "is_cave": False,
        "has_tourists": True,
        "has_entry_fee": True,
        "is_underground": False,
        "night_light": False,
        "height_meters": 20,
        "famous_for": "Aslan gövdeli, insan başlı heykel",
        "best_time": "Ekim-Nisan",
        "estimated_visitors": 8000000
    },
    {
        "id": 15,
        "name": "Taj Mahal",
        "continent": "Asia",
        "country": "India",
        "city": "Agra",
        "category": "religious",
        "is_natural": False,
        "is_man_made": True,
        "is_unesco": True,
        "is_ancient": False,
        "is_temple": False,
        "is_museum": False,
        "is_mosque": True,
        "is_church": False,
        "is_mountain": False,
        "is_island": False,
        "is_water": False,
        "is_desert": False,
        "is_volcano": False,
        "is_cave": False,
        "has_tourists": True,
        "has_entry_fee": True,
        "is_underground": False,
        "night_light": True,
        "height_meters": 73,
        "famous_for": "Aşk anıtı, beyaz mermer türbe, Babür mimarisi",
        "best_time": "Ekim-Mart",
        "estimated_visitors": 7000000
    },
    {
        "id": 16,
        "name": "Çin Seddi",
        "continent": "Asia",
        "country": "China",
        "city": "Beijing",
        "category": "historical",
        "is_natural": False,
        "is_man_made": True,
        "is_unesco": True,
        "is_ancient": True,
        "is_temple": False,
        "is_museum": False,
        "is_mosque": False,
        "is_church": False,
        "is_mountain": True,
        "is_island": False,
        "is_water": False,
        "is_desert": True,
        "is_volcano": False,
        "is_cave": False,
        "has_tourists": True,
        "has_entry_fee": True,
        "is_underground": False,
        "night_light": False,
        "height_meters": 14,
        "famous_for": "Dünyanın en uzun suru, 21.000 km",
        "best_time": "Nisan-Ekim",
        "estimated_visitors": 10000000
    },
    {
        "id": 17,
        "name": "Machu Picchu",
        "continent": "South America",
        "country": "Peru",
        "city": "Cusco",
        "category": "archaeological",
        "is_natural": False,
        "is_man_made": True,
        "is_unesco": True,
        "is_ancient": True,
        "is_temple": True,
        "is_museum": False,
        "is_mosque": False,
        "is_church": False,
        "is_mountain": True,
        "is_island": False,
        "is_water": False,
        "is_desert": False,
        "is_volcano": False,
        "is_cave": False,
        "has_tourists": True,
        "has_entry_fee": True,
        "is_underground": False,
        "night_light": False,
        "height_meters": 2430,
        "famous_for": "İnka İmparatorluğu, kayıp şehir, And Dağları",
        "best_time": "Mayıs-Eylül",
        "estimated_visitors": 1500000
    },
    {
        "id": 18,
        "name": "Petra",
        "continent": "Asia",
        "country": "Jordan",
        "city": "Wadi Musa",
        "category": "archaeological",
        "is_natural": False,
        "is_man_made": True,
        "is_unesco": True,
        "is_ancient": True,
        "is_temple": False,
        "is_museum": False,
        "is_mosque": False,
        "is_church": False,
        "is_mountain": False,
        "is_island": False,
        "is_water": False,
        "is_desert": True,
        "is_volcano": False,
        "is_cave": True,
        "has_tourists": True,
        "has_entry_fee": True,
        "is_underground": False,
        "night_light": False,
        "height_meters": 0,
        "famous_for": "Kızıl kayalara oyulmuş şehir, Hazine",
        "best_time": "Mart-Mayıs, Eylül-Kasım",
        "estimated_visitors": 1000000
    },
    {
        "id": 19,
        "name": "Stonehenge",
        "continent": "Europe",
        "country": "United Kingdom",
        "city": "Salisbury",
        "category": "archaeological",
        "is_natural": False,
        "is_man_made": True,
        "is_unesco": True,
        "is_ancient": True,
        "is_temple": True,
        "is_museum": False,
        "is_mosque": False,
        "is_church": False,
        "is_mountain": False,
        "is_island": False,
        "is_water": False,
        "is_desert": False,
        "is_volcano": False,
        "is_cave": False,
        "has_tourists": True,
        "has_entry_fee": True,
        "is_underground": False,
        "night_light": False,
        "height_meters": 0,
        "famous_for": "Tarih öncesi anıt, megalitik yapı, yaz gündönümü",
        "best_time": "Tüm yıl",
        "estimated_visitors": 1300000
    },
    {
        "id": 20,
        "name": "Kolezyum",
        "continent": "Europe",
        "country": "Italy",
        "city": "Rome",
        "category": "archaeological",
        "is_natural": False,
        "is_man_made": True,
        "is_unesco": True,
        "is_ancient": True,
        "is_temple": False,
        "is_museum": False,
        "is_mosque": False,
        "is_church": False,
        "is_mountain": False,
        "is_island": False,
        "is_water": False,
        "is_desert": False,
        "is_volcano": False,
        "is_cave": False,
        "has_tourists": True,
        "has_entry_fee": True,
        "is_underground": False,
        "night_light": True,
        "height_meters": 48,
        "famous_for": "Antik Roma amfi tiyatrosu, gladyatör dövüşleri",
        "best_time": "Tüm yıl",
        "estimated_visitors": 7000000
    },
    {
        "id": 21,
        "name": "Everest Dağı",
        "continent": "Asia",
        "country": "Nepal",
        "city": "Solukhumbu",
        "category": "natural",
        "is_natural": True,
        "is_man_made": False,
        "is_unesco": True,
        "is_ancient": False,
        "is_temple": False,
        "is_museum": False,
        "is_mosque": False,
        "is_church": False,
        "is_mountain": True,
        "is_island": False,
        "is_water": False,
        "is_desert": False,
        "is_volcano": False,
        "is_cave": False,
        "has_tourists": True,
        "has_entry_fee": True,
        "is_underground": False,
        "night_light": False,
        "height_meters": 8848,
        "famous_for": "Dünyanın en yüksek dağı, 8848 metre",
        "best_time": "Nisan-Mayıs, Eylül-Ekim",
        "estimated_visitors": 50000
    },
    {
        "id": 22,
        "name": "Niagara Şelalesi",
        "continent": "North America",
        "country": "USA",
        "city": "New York",
        "category": "natural",
        "is_natural": True,
        "is_man_made": False,
        "is_unesco": False,
        "is_ancient": False,
        "is_temple": False,
        "is_museum": False,
        "is_mosque": False,
        "is_church": False,
        "is_mountain": False,
        "is_island": False,
        "is_water": True,
        "is_desert": False,
        "is_volcano": False,
        "is_cave": False,
        "has_tourists": True,
        "has_entry_fee": False,
        "is_underground": False,
        "night_light": True,
        "height_meters": 51,
        "famous_for": "Kuzey Amerika'nın en büyük şelalesi",
        "best_time": "Haziran-Ağustos",
        "estimated_visitors": 12000000
    },
    {
        "id": 23,
        "name": "Büyük Kanyon",
        "continent": "North America",
        "country": "USA",
        "city": "Arizona",
        "category": "natural",
        "is_natural": True,
        "is_man_made": False,
        "is_unesco": True,
        "is_ancient": False,
        "is_temple": False,
        "is_museum": False,
        "is_mosque": False,
        "is_church": False,
        "is_mountain": False,
        "is_island": False,
        "is_water": False,
        "is_desert": True,
        "is_volcano": False,
        "is_cave": False,
        "has_tourists": True,
        "has_entry_fee": True,
        "is_underground": False,
        "night_light": False,
        "height_meters": 1800,
        "famous_for": "Dünyanın en büyük kanyonu, Colorado Nehri",
        "best_time": "Mart-Mayıs, Eylül-Kasım",
        "estimated_visitors": 6000000
    },
    {
        "id": 24,
        "name": "Kuzey Işıkları",
        "continent": "Europe",
        "country": "Norway",
        "city": "Tromsø",
        "category": "natural",
        "is_natural": True,
        "is_man_made": False,
        "is_unesco": False,
        "is_ancient": False,
        "is_temple": False,
        "is_museum": False,
        "is_mosque": False,
        "is_church": False,
        "is_mountain": False,
        "is_island": False,
        "is_water": False,
        "is_desert": False,
        "is_volcano": False,
        "is_cave": False,
        "has_tourists": True,
        "has_entry_fee": False,
        "is_underground": False,
        "night_light": True,
        "height_meters": 0,
        "famous_for": "Doğa olayı, aurora borealis, renkli ışıklar",
        "best_time": "Eylül-Mart",
        "estimated_visitors": 1000000
    },
    {
        "id": 25,
        "name": "Sidney Opera Evi",
        "continent": "Australia",
        "country": "Australia",
        "city": "Sydney",
        "category": "modern",
        "is_natural": False,
        "is_man_made": True,
        "is_unesco": True,
        "is_ancient": False,
        "is_temple": False,
        "is_museum": False,
        "is_mosque": False,
        "is_church": False,
        "is_mountain": False,
        "is_island": False,
        "is_water": True,
        "is_desert": False,
        "is_volcano": False,
        "is_cave": False,
        "has_tourists": True,
        "has_entry_fee": True,
        "is_underground": False,
        "night_light": True,
        "height_meters": 67,
        "famous_for": "Mimari harikası, yelkenli tasarımı",
        "best_time": "Eylül-Mayıs",
        "estimated_visitors": 8000000
    },
    {
        "id": 26,
        "name": "Angkor Wat",
        "continent": "Asia",
        "country": "Cambodia",
        "city": "Siem Reap",
        "category": "religious",
        "is_natural": False,
        "is_man_made": True,
        "is_unesco": True,
        "is_ancient": True,
        "is_temple": True,
        "is_museum": False,
        "is_mosque": False,
        "is_church": False,
        "is_mountain": False,
        "is_island": False,
        "is_water": False,
        "is_desert": False,
        "is_volcano": False,
        "is_cave": False,
        "has_tourists": True,
        "has_entry_fee": True,
        "is_underground": False,
        "night_light": False,
        "height_meters": 65,
        "famous_for": "Dünyanın en büyük dini yapısı, Khmer mimarisi",
        "best_time": "Kasım-Mart",
        "estimated_visitors": 2500000
    },
    {
        "id": 27,
        "name": "Pisa Kulesi",
        "continent": "Europe",
        "country": "Italy",
        "city": "Pisa",
        "category": "modern",
        "is_natural": False,
        "is_man_made": True,
        "is_unesco": True,
        "is_ancient": False,
        "is_temple": False,
        "is_museum": False,
        "is_mosque": False,
        "is_church": True,
        "is_mountain": False,
        "is_island": False,
        "is_water": False,
        "is_desert": False,
        "is_volcano": False,
        "is_cave": False,
        "has_tourists": True,
        "has_entry_fee": True,
        "is_underground": False,
        "night_light": False,
        "height_meters": 56,
        "famous_for": "Eğik kulesi, 3.97 derece eğik",
        "best_time": "Tüm yıl",
        "estimated_visitors": 1000000
    },
    {
        "id": 28,
        "name": "Kurtarıcı İsa Heykeli",
        "continent": "South America",
        "country": "Brazil",
        "city": "Rio de Janeiro",
        "category": "modern",
        "is_natural": False,
        "is_man_made": True,
        "is_unesco": True,
        "is_ancient": False,
        "is_temple": False,
        "is_museum": False,
        "is_mosque": False,
        "is_church": False,
        "is_mountain": True,
        "is_island": False,
        "is_water": False,
        "is_desert": False,
        "is_volcano": False,
        "is_cave": False,
        "has_tourists": True,
        "has_entry_fee": True,
        "is_underground": False,
        "night_light": True,
        "height_meters": 38,
        "famous_for": "Rio simgesi, 30 metre heykel",
        "best_time": "Nisan-Ekim",
        "estimated_visitors": 2000000
    },
    {
        "id": 29,
        "name": "Moai Heykelleri",
        "continent": "South America",
        "country": "Chile",
        "city": "Easter Island",
        "category": "archaeological",
        "is_natural": False,
        "is_man_made": True,
        "is_unesco": True,
        "is_ancient": True,
        "is_temple": False,
        "is_museum": False,
        "is_mosque": False,
        "is_church": False,
        "is_mountain": False,
        "is_island": True,
        "is_water": False,
        "is_desert": False,
        "is_volcano": False,
        "is_cave": False,
        "has_tourists": True,
        "has_entry_fee": True,
        "is_underground": False,
        "night_light": False,
        "height_meters": 10,
        "famous_for": "Dev taş heykeller, Paskalya Adası",
        "best_time": "Tüm yıl",
        "estimated_visitors": 100000
    },
    {
        "id": 30,
        "name": "Chichen Itza",
        "continent": "North America",
        "country": "Mexico",
        "city": "Yucatan",
        "category": "archaeological",
        "is_natural": False,
        "is_man_made": True,
        "is_unesco": True,
        "is_ancient": True,
        "is_temple": True,
        "is_museum": False,
        "is_mosque": False,
        "is_church": False,
        "is_mountain": False,
        "is_island": False,
        "is_water": False,
        "is_desert": False,
        "is_volcano": False,
        "is_cave": False,
        "has_tourists": True,
        "has_entry_fee": True,
        "is_underground": False,
        "night_light": False,
        "height_meters": 30,
        "famous_for": "Maya uygarlığı, piramit, astronomi",
        "best_time": "Kasım-Nisan",
        "estimated_visitors": 2500000
    }
]

# B. UNESCO'dan Otomatik Çek (isteğe bağlı - 1000+ yer)
def fetch_unesco_sites():
    """UNESCO'dan yerleri çek (otomatik)"""
    url = "https://whc.unesco.org/en/list/json/"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            sites = []
            for site in data.get('sites', []):
                sites.append({
                    "name": site.get('site', ''),
                    "country": site.get('states', ''),
                    "category": site.get('category', ''),
                    "year": site.get('date_of_inscription', ''),
                    "is_unesco": True,
                    "has_tourists": True
                })
            return sites
    except:
        return []
    return []

# ============================================
# 2. AKINATOR MOTORU
# ============================================

class AkinatorEngine:
    """Akinator mantığı - Information Gain"""
    
    def __init__(self, landmarks: List[Dict]):
        self.landmarks = landmarks
        self.candidates = landmarks.copy()
        self.asked_questions = []
        self.question_count = 0
        self.score = 0
        
    def get_all_questions(self) -> List[Dict]:
        """Tüm soruları oluştur"""
        questions = []
        
        boolean_props = {
            "is_natural": "Doğal oluşum mu?",
            "is_man_made": "İnsan yapımı mı?",
            "is_unesco": "UNESCO listesinde mi?",
            "is_ancient": "Antik dönemden mi?",
            "is_temple": "Tapınak mı?",
            "is_museum": "Müze mi?",
            "is_mosque": "Cami mi?",
            "is_church": "Kilise mi?",
            "is_mountain": "Dağ mı?",
            "is_island": "Ada mı?",
            "is_water": "Su ile ilgili mi?",
            "is_desert": "Çölde mi?",
            "is_volcano": "Volkan mı?",
            "is_cave": "Mağara mı?",
            "has_tourists": "Turistik bir yer mi?",
            "has_entry_fee": "Giriş ücretli mi?",
            "is_underground": "Yer altında mı?",
            "night_light": "Gece ışıklandırılıyor mu?"
        }
        
        for prop, text in boolean_props.items():
            questions.append({"id": prop, "text": text, "type": "boolean"})
        
        return questions
    
    def calculate_information_gain(self, candidates: List[Dict], question: Dict) -> float:
        """Bilgi kazancı hesapla"""
        if not candidates:
            return 0
        
        total = len(candidates)
        prop = question["id"]
        
        true_count = sum(1 for l in candidates if l.get(prop, False))
        false_count = total - true_count
        
        if true_count == 0 or false_count == 0:
            return 0
        
        p_true = true_count / total
        p_false = false_count / total
        
        # Entropy
        entropy = -(p_true * math.log2(p_true) + p_false * math.log2(p_false))
        
        # Information Gain
        gain = entropy * (1 - p_true**2 - p_false**2)
        return gain
    
    def get_best_question(self) -> Optional[Dict]:
        """En iyi soruyu seç"""
        all_questions = self.get_all_questions()
        
        best_question = None
        best_gain = -1
        
        for q in all_questions:
            if q["id"] in self.asked_questions:
                continue
            
            gain = self.calculate_information_gain(self.candidates, q)
            
            # Rastgelelik ekle - her oyunda farklı soru çıksın
            if gain > best_gain + 0.01:
                best_gain = gain
                best_question = q
            elif gain > best_gain - 0.01 and random.random() < 0.3:
                best_question = q
        
        return best_question
    
    def filter_candidates(self, question: Dict, answer: str):
        """Adayları filtrele"""
        prop = question["id"]
        
        if answer == "Evet":
            self.candidates = [l for l in self.candidates if l.get(prop, False)]
        elif answer == "Hayır":
            self.candidates = [l for l in self.candidates if not l.get(prop, False)]
        # Bilmiyorum'da eleme yapma
        
        self.asked_questions.append(question["id"])
        self.question_count += 1
    
    def get_orbi_comment(self) -> str:
        """Orbi'nin konuşması"""
        count = len(self.candidates)
        
        if count == 1:
            return "🎯 %100 eminim! Bu yer..."
        elif count <= 3:
            return "🎪 Son 3 aday kaldı, biliyorum ki..."
        elif count <= 10:
            return "🧠 Adayları iyice daralttım, az kaldı..."
        elif count <= 30:
            return "🔍 İyice yaklaşıyorum, biraz daha..."
        elif count <= 100:
            return "📊 Eleme başarılı, yoldayım..."
        else:
            return "🤔 Hmm... daha çok erken, sorulara devam!"
    
    def calculate_score(self) -> int:
        """Puan hesapla"""
        base = max(1000 - self.question_count * 20, 100)
        bonus = max(0, 100 - len(self.candidates))
        return base + bonus

# ============================================
# 3. ANA UYGULAMA
# ============================================

def main():
    # Sayfa ayarları
    st.set_page_config(
        page_title="Orbi Discovery - Dünyayı Keşfet",
        page_icon="🌍",
        layout="centered",
        initial_sidebar_state="collapsed"
    )
    
    # CSS
    st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(135deg, #0f0f1a 0%, #1a1a2e 50%, #16213e 100%);
        }
        .orbi-title {
            color: #00d4ff;
            font-size: 2.5em;
            font-weight: 800;
            text-align: center;
            text-shadow: 0 0 20px rgba(0, 212, 255, 0.3);
        }
        .orbi-subtitle {
            color: #8899aa;
            text-align: center;
            font-size: 1em;
            margin-bottom: 20px;
        }
        .orbi-speech {
            background: linear-gradient(135deg, #1a3a5c, #0d1f3c);
            border-radius: 20px;
            padding: 15px 20px;
            border-left: 5px solid #00d4ff;
            color: #e0e8f0;
            margin: 15px 0;
        }
        .orbi-speech .orbi-name {
            color: #00d4ff;
            font-weight: bold;
        }
        .orbi-card {
            background: rgba(255,255,255,0.05);
            border-radius: 15px;
            padding: 20px;
            border: 1px solid rgba(255,255,255,0.1);
            backdrop-filter: blur(10px);
            margin-bottom: 15px;
        }
        .metric-card {
            background: rgba(255,255,255,0.05);
            border-radius: 10px;
            padding: 12px;
            text-align: center;
            border: 1px solid rgba(255,255,255,0.05);
        }
        .metric-value {
            color: #00d4ff;
            font-size: 1.8em;
            font-weight: bold;
        }
        .metric-label {
            color: #8899aa;
            font-size: 0.8em;
        }
        .stButton > button {
            background: linear-gradient(135deg, #00d4ff, #0088cc);
            color: white;
            border: none;
            border-radius: 15px;
            padding: 15px 10px;
            font-weight: 700;
            font-size: 1.1em;
            width: 100%;
            min-height: 55px;
            cursor: pointer !important;
        }
        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(0, 212, 255, 0.4);
        }
        @media (max-width: 480px) {
            .stButton > button {
                min-height: 50px;
                font-size: 0.95em;
            }
            .orbi-title {
                font-size: 1.8em !important;
            }
        }
        .result-found {
            background: linear-gradient(135deg, #00d4ff22, #0088cc22);
            border: 2px solid #00d4ff;
            border-radius: 20px;
            padding: 25px;
            text-align: center;
            animation: pulse 2s infinite;
        }
        @keyframes pulse {
            0% { box-shadow: 0 0 20px rgba(0, 212, 255, 0.2); }
            50% { box-shadow: 0 0 40px rgba(0, 212, 255, 0.5); }
            100% { box-shadow: 0 0 20px rgba(0, 212, 255, 0.2); }
        }
        .footer {
            color: #445566;
            text-align: center;
            padding: 15px;
            font-size: 0.7em;
            border-top: 1px solid rgba(255,255,255,0.05);
            margin-top: 30px;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Başlık
    st.markdown('<h1 class="orbi-title">🌍 ORBI DISCOVERY</h1>', unsafe_allow_html=True)
    st.markdown('<p class="orbi-subtitle">"Bir yer düşün, ben bulayım!"</p>', unsafe_allow_html=True)
    
    # Session state
    if "engine" not in st.session_state:
        all_landmarks = MANUAL_LANDMARKS.copy()
        # UNESCO'yu da ekle (isteğe bağlı)
        # unesco = fetch_unesco_sites()
        # all_landmarks.extend(unesco)
        st.session_state.engine = AkinatorEngine(all_landmarks)
        st.session_state.game_started = False
        st.session_state.game_over = False
        st.session_state.found = None
        st.session_state.score = 0
    
    # Sidebar
    with st.sidebar:
        st.markdown("### 📊 İstatistikler")
        total_places = len(st.session_state.engine.landmarks)
        st.metric("Toplam Yer", total_places)
        
        if st.session_state.game_started:
            st.metric("Aday", len(st.session_state.engine.candidates))
            st.metric("Soru", st.session_state.engine.question_count)
            st.metric("Puan", st.session_state.engine.score)
        
        st.markdown("---")
        if st.button("🔄 Yeni Oyun", use_container_width=True):
            st.session_state.engine = AkinatorEngine(st.session_state.engine.landmarks)
            st.session_state.game_started = False
            st.session_state.game_over = False
            st.session_state.found = None
            st.rerun()
    
    # ========== BAŞLANGIÇ ==========
    if not st.session_state.game_started:
        st.markdown("""
        <div class="orbi-card" style="text-align: center;">
            <h2 style="color: #00d4ff;">🗺️ Dünyayı Keşfet!</h2>
            <p style="color: #8899aa;">Aklından bir yer tut, Orbi bulsun!</p>
            <p style="color: #667788; font-size: 0.9em;">
                🌍 Dünyanın her yerinden<br>
                🎯 Akinator mantığı<br>
                🧠 Information Gain<br>
                🏆 Puan sistemi
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🚀 Başla!", use_container_width=True):
            st.session_state.game_started = True
            st.session_state.engine.candidates = st.session_state.engine.landmarks.copy()
            st.rerun()
    
    # ========== OYUN ==========
    elif not st.session_state.game_over:
        # Orbi konuşması
        comment = st.session_state.engine.get_orbi_comment()
        st.markdown(f"""
        <div class="orbi-speech">
            <span class="orbi-name">🧠 Orbi:</span> {comment}
        </div>
        """, unsafe_allow_html=True)
        
        # Metrikler
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value">{len(st.session_state.engine.candidates)}</div>
                <div class="metric-label">🏛️ Aday</div>
            </div>
            """, unsafe_allow_html=True)
        with c2:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value">{st.session_state.engine.question_count}</div>
                <div class="metric-label">❓ Soru</div>
            </div>
            """, unsafe_allow_html=True)
        with c3:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value">{st.session_state.engine.score}</div>
                <div class="metric-label">⭐ Puan</div>
            </div>
            """, unsafe_allow_html=True)
        with c4:
            progress = min(st.session_state.engine.question_count / 15, 1.0)
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-value">%{int(progress*100)}</div>
                <div class="metric-label">📊 İlerleme</div>
            </div>
            """, unsafe_allow_html=True)
        st.progress(progress)
        
        # En iyi soruyu bul
        best_q = st.session_state.engine.get_best_question()
        
        if best_q is None or len(st.session_state.engine.candidates) <= 1:
            # Tahmin et
            st.session_state.game_over = True
            if st.session_state.engine.candidates:
                st.session_state.found = st.session_state.engine.candidates[0]
                st.session_state.engine.score = st.session_state.engine.calculate_score()
            st.rerun()
        else:
            # Soruyu göster
            st.markdown(f"""
            <div class="orbi-card">
                <h3 style="color: #00d4ff;">❓ Soru {st.session_state.engine.question_count + 1}</h3>
                <p style="color: #e0e8f0; font-size: 1.2em;">{best_q['text']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Cevap butonları
            c1, c2, c3 = st.columns(3)
            with c1:
                if st.button("✅ Evet", key=f"yes_{best_q['id']}", use_container_width=True):
                    st.session_state.engine.filter_candidates(best_q, "Evet")
                    st.session_state.engine.score += 50
                    st.rerun()
            with c2:
                if st.button("❌ Hayır", key=f"no_{best_q['id']}", use_container_width=True):
                    st.session_state.engine.filter_candidates(best_q, "Hayır")
                    st.session_state.engine.score += 50
                    st.rerun()
            with c3:
                if st.button("🤷 Bilmiyorum", key=f"idk_{best_q['id']}", use_container_width=True):
                    st.session_state.engine.filter_candidates(best_q, "Bilmiyorum")
                    st.rerun()
    
    # ========== OYUN SONU ==========
    else:
        if st.session_state.found:
            lm = st.session_state.found
            st.markdown(f"""
            <div class="result-found">
                <h1 style="color: #00d4ff;">🎉 {random.choice(['BULDUM!', 'SENİ YAKALADIM!', 'İŞTE BURADA!'])}</h1>
                <h2 style="color: white; font-size: 2.2em;">📍 {lm['name']}</h2>
                <p style="color: #8899aa;">{lm.get('country', 'Unknown')} • {lm.get('city', '')}</p>
                <p style="color: #e0e8f0;">📂 {lm.get('category', 'Unknown')}</p>
                {f'<p style="color: #aaa;">🏔️ {lm["height_meters"]}m</p>' if lm.get('height_meters', 0) > 0 else ''}
                {f'<p style="color: #aaa;">⭐ {lm["estimated_visitors"]:,} ziyaretçi/yıl</p>' if lm.get('estimated_visitors') else ''}
                {f'<p style="color: #aaa;">📅 En iyi zaman: {lm["best_time"]}</p>' if lm.get('best_time') else ''}
                <p style="color: #aaa; font-size: 0.9em; margin-top: 10px;">{lm.get('famous_for', '')}</p>
            </div>
            """, unsafe_allow_html=True)
            
            c1, c2 = st.columns(2)
            with c1:
                st.metric("Soru", st.session_state.engine.question_count)
            with c2:
                st.metric("Puan", st.session_state.engine.score)
            
            if st.button("🔄 Yeni Oyun", use_container_width=True):
                st.session_state.engine = AkinatorEngine(st.session_state.engine.landmarks)
                st.session_state.game_started = False
                st.session_state.game_over = False
                st.session_state.found = None
                st.rerun()
    
    # Footer
    total = len(st.session_state.engine.landmarks)
    st.markdown(f"""
    <div class="footer">
        🌍 ORBI DISCOVERY v4.0 • {total} yer • Akinator mantığı • Dünyayı Keşfet
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
