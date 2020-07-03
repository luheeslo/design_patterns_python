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


class Profile():  # pylint: disable=too-few-public-methods
    """docstring for Profile"""
    def __init__(self, sections=None):
        self.sections = tuple(section() for section in (sections or []))


def create_facebook_profile():
    """TODO: Docstring for create_facebook_profiles.
    :returns: TODO

    """
    return (PersonalSection, AlbumSection)


def create_linkedin_profile():
    """TODO: Docstring for create_facebook_profiles.
    :returns: TODO

    """
    return (PersonalSection, PatentSection, PublicationSection)


if __name__ == "__main__":
    chooses = {'facebook': create_facebook_profile,
               'linkedin': create_linkedin_profile}
    profile_type = input("Which Profile you'd like to create?[LinkedIn or Facebook]")  # pylint:invalid-name

    create_profile = chooses[profile_type.lower()]
    profile = Profile(sections=create_profile())  # pylint:invalid-name

    print("Profile has sections --", profile.sections)
