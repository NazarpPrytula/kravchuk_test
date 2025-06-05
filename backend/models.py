from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

class Hero(Base):
    __tablename__ = 'heroes'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    primary_attr = Column(String)
    attack_type = Column(String)
    roles = Column(String)
    base_health = Column(Integer)
    base_mana = Column(Integer)
    base_armor = Column(Integer)
    base_str = Column(Integer)
    base_agi = Column(Integer)
    base_int = Column(Integer)
    str_gain = Column(Integer)
    agi_gain = Column(Integer)
    int_gain = Column(Integer)
    pickrate = Column(Integer)
    winrate = Column(Integer)

    
    builds = relationship("Builds", backref="hero")
    abilities = relationship("Abilities", backref="hero")
    matchups = relationship("Matchups", backref="hero", foreign_keys='Matchups.hero_id')
    countered_by = relationship("Matchups", backref="counter_hero", foreign_keys='Matchups.against_hero_id')

    def to_dict_hero(self):
        return {
            "id": self.id,
            "name": self.name,
            "primary_attr": self.primary_attr,
            "attack_type": self.attack_type,
            "roles": self.roles,
            "baseHealth": self.base_health,
            "baseMana": self.base_mana,
            "baseArmor": self.base_armor,
            "pickRate": self.pickrate,
            "winRate": self.winrate,
            "attributes": {
                "strength": self.base_str,
                "agility": self.base_agi,
                "intelligence": self.base_int,
                "strengthGain": self.str_gain,
                "agilityGain": self.agi_gain,
                "intelligenceGain": self.int_gain,
            }
        }

class Builds(Base):
    __tablename__ = 'builds'
    id = Column(Integer, primary_key=True, index=True)
    hero_id = Column(Integer, ForeignKey('heroes.id'))
    name = Column(String)
    winrate = Column(Integer)
    popularity = Column(Integer)

    
    items = relationship("BuildItems", backref="build")

    def to_dict_builds(self):
        return {
            "id": self.id,
            "hero_id": self.hero_id,
            "name": self.name,
            "winRate": self.winrate,
            "popularity": self.popularity
        }

class BuildItems(Base):
    __tablename__ = 'build_items'
    id = Column(Integer, primary_key=True, index=True)
    build_id = Column(Integer, ForeignKey('builds.id'))
    item_id = Column(Integer, ForeignKey('items.id'))
    position = Column(String)

  
    item = relationship("Items", backref="build_items")

    def to_dict(self):
        return {
            "id": self.id,
            "build_id": self.build_id,
            "item_id": self.item_id,
            "position": self.position
        }

class Abilities(Base):
    __tablename__ = 'abilities'
    id = Column(Integer, primary_key=True, index=True)
    hero_id = Column(Integer, ForeignKey('heroes.id'))
    name = Column(String)
    description = Column(String)
    ability_type = Column(String)

    def to_dict(self):
        return {
            "id": self.id,
            "hero_id": self.hero_id,
            "name": self.name,
            "description": self.description,
            "ability_type": self.ability_type
        }

class Matchups(Base):
    __tablename__ = 'matchups'
    id = Column(Integer, primary_key=True, index=True)
    hero_id = Column(Integer, ForeignKey('heroes.id'))
    against_hero_id = Column(Integer, ForeignKey('heroes.id'))
    advantage = Column(Integer)
    games_played = Column(Integer)

    def to_dict(self):
        return {
            "id": self.id,
            "hero_id": self.hero_id,
            "against_hero_id": self.against_hero_id,
            "advantage": self.advantage,
            "games_played": self.games_played
        }

class Items(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    cost = Column(Integer)
    description = Column(String)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "cost": self.cost,
            "description": self.description
        }
