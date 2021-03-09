class Time:
    def __init__(self):
        self._seconds = 0

    def _get_hours(self):
        return self._hours

    def _set_hours(self, time):
        if time > 23:
            self._hours = 23
        elif time < 0:
            self._hours = 0
        else:
            self._hours = time

    @property
    def hours_simple(self):
        if self._get_hours() > 12:
            return self._get_hours() - 12

        elif self._get_hours() == 0:
            return 12

        return self._get_hours()

    @property
    def period(self):
        if self._get_hours() >= 12:
            return "PM"
        else:
            return "AM"

    def _get_minutes(self):
        return self._minutes

    def _set_minutes(self, time):
        if time > 59:
            self._minutes = 59
        elif time < 0:
            self._minutes = 0
        else:
            self._minutes = time

    def _get_seconds(self):
        return self._seconds

    def _set_seconds(self, time):
        if time > 59:
            self._seconds = 59
        elif time < 0:
            self._seconds = 0
        else:
            self._seconds = time

    hours = property(_get_hours, _set_hours)
    minutes = property(_get_minutes, _set_minutes)
    seconds = property(_get_seconds, _set_seconds)


def main():
    time = Time()

    hours = int(input("Hours: "))
    time.hours = hours
    print()

    minutes = int(input("Minutes: "))
    time.minutes = minutes
    print()

    seconds = int(input("Seconds: "))
    time.seconds = seconds
    print()

    print(f'The time is {time.hours}:{time.minutes}:{time.seconds}')
    print(
        f'Simple time is {time.hours_simple}:{time.minutes}:{time.seconds} {time.period}')


if __name__ == "__main__":
    main()
