
class AgeRating:
    """View all the age ratings at: https://developers.giphy.com/docs/optional-settings/#rating
    """
    @staticmethod
    def g():
        """Specifies the G rating: Completely clean content.
        """
        return "g"

    @staticmethod
    def pg():
        """Specifies the PG rating: Mild sexual content, Mild Profanities etc.
        """
        return "pg"
    
    @staticmethod
    def pg_13():
        """Specifies the PG-13 rating: Moderate Profanities. Moderate sexual content etc.
        """
        return "pg-13"
    
    @staticmethod
    def r():
        """Specifies the R rating: Severe Profanities. Severe sexual themes and content.
        """
        return "r"