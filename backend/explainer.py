def explain_result(intent, result):

    # -------------------------------
    # MARKS EXPLANATION
    # -------------------------------
    if intent == "marks":

        maths, science, english = result[0]

        avg = (maths + science + english) / 3

        if avg >= 90:
            return "Excellent academic performance."

        elif avg >= 75:
            return "Good academic performance."

        elif avg >= 50:
            return "Average academic performance."

        else:
            return "Needs improvement in academics."

    # -------------------------------
    # ATTENDANCE EXPLANATION
    # -------------------------------
    elif intent == "attendance":

        attendance = result[0][0]

        if attendance >= 90:
            return "Attendance is very good."

        elif attendance >= 75:
            return "Attendance is satisfactory."

        else:
            return "Attendance is low."

    # -------------------------------
    # TOPPER EXPLANATION
    # -------------------------------
    elif intent == "topper":

        return "This student has the highest total marks in the class."

    return "No explanation available."