"""
File: factory_pattern.py
Author: yourname
Email: yourname@email.com
Github: https://github.com/yourname
Description: Factory Pattern example.
"""

from abc import ABCMeta, abstractmethod


class Section(metaclass=ABCMeta):  # pylint: disable=too-few-public-methods
    """docstring for Section"""

    @abstractmethod
    def describe(self):
        """TODO: Docstring for describe.
        :returns: TODO

        """
        pass  # pylint: disable=unnecessary-pass


class PersonalSection(Section):  # pylint: disable=too-few-public-methods
    """docstring for PersonalSection"""

    def describe(self):
        """TODO: Docstring for describe.
        :returns: TODO

        """
        print("Personal Section")


class AlbumSection(Section):  # pylint: disable=too-few-public-methods
    """docstring for AlbumSection"""

    def describe(self):
        """TODO: Docstring for describe.
        :returns: TODO

        """
        print("Album Section")


class PatentSection(Section):  # pylint: disable=too-few-public-methods
    """docstring for PatentSection"""

    def describe(self):
        """TODO: Docstring for describe.
        :returns: TODO

        """
        print("Patent Section")


class PublicationSection(Section):  # pylint: disable=too-few-public-methods
    """docstring for PublicationSection"""

    def describe(self):
        """TODO: Docstring for describe.
        :returns: TODO

        """
        print("Publication Section")


class Profile(metaclass=ABCMeta):  # pylint: disable=too-few-public-methods
    """docstring for Profile"""
    def __init__(self):
        self.sections = []
        self.create_profile()

    @abstractmethod
    def create_profile(self):
        """TODO: Docstring for createProfile.
        :returns: TODO

        """
        pass  # pylint: disable=unnecessary-pass

    def get_sections(self):
        """TODO: Docstring for getSections.
        :returns: TODO

        """
        return self.sections

    def add_sections(self, section):
        """TODO: Docstring for addSections.

        :section: TODO
        :returns: TODO

        """
        self.sections.append(section)


class Linkedin(Profile):  # pylint: disable=too-few-public-methods
    """docstring for Linkedin"""
    def create_profile(self):
        self.add_sections(PersonalSection())
        self.add_sections(PatentSection())
        self.add_sections(PublicationSection())


class Facebook(Profile):  # pylint: disable=too-few-public-methods
    """docstring for Facebook"""
    def create_profile(self):
        self.add_sections(PersonalSection())
        self.add_sections(AlbumSection())


if __name__ == "__main__":
    profile_type = input("Which Profile you'd like to create?[LinkedIn or Facebook]")  # pylint:invalid-name
    profile = eval(profile_type.lower().title())()  # pylint:invalid-name
    print("Creating profile..", type(profile).__name__)
    print("Profile has sections --", profile.get_sections())
