
class Ampel_Base():
    _phase = 1

    def get_num_lights(self):
        return self._num_lights


    def get_colors(self):
        return self._phase_table[self._phase]


    def cycle_phase(self):
        if self._phase < len(self._phase_table.keys()):
            self._phase += 1
        else:
            self._phase = 1


class Table_Fussgänger():
    _phase_table = {
        1: ["#19C819","#000000"],
        2: ["#000000","#C81919"]
    }


class Table_Auto():
    _phase_table = {
        1: ["#000000","#000000","#19C819"],
        2: ["#000000","#FAFA00","#000000"],
        3: ["#C81919","#000000","#000000"],
        4: ["#C81919","#FAFA00","#000000"]
    }


class Ampel_Fussgänger(Table_Fussgänger, Ampel_Base):
    def __init__(self):
        self._num_lights = len(self._phase_table[1])


class Ampel_Auto(Table_Auto, Ampel_Base):
    def __init__(self):
        self._num_lights = len(self._phase_table[1])
