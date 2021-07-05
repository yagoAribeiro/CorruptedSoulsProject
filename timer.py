class Timer:

    is_global_timer_paused = False

    def __init__(self):
        self.ticks = 0
        self.second_ticks = 0
        self.difference = 0
    
    def countdown(self, boolean, ticks, seconds):
        #quando não tiver em cooldown, incrementa ambos os contadores
        if boolean == False:
            self.ticks += ticks
            self.second_ticks = self.ticks

        #quanto tiver, pare um contador e incremente apenas o outro
        else: 
            self.second_ticks += ticks
            #descobre quanto tempo se passou através da diferença dos contadores e converte para segundos
            self.difference = self.second_ticks - self.ticks
            this_seconds = self.difference/1000
            if (this_seconds) >= seconds:
                #zera os contadores se o tempo em questão já atingiu o segundo desejado
                # e retorna a mesma váriavel de cooldown, mas agora como False
                    self.ticks = 0
                    self.second_ticks = 0 
                    self.difference = 0
                    boolean = False
                    return boolean
        #print (self.second_ticks)

    def clock(self, ticks, paused, actual_text):

        if paused == False:

            this_ticks = 0
            seconds = 0
            clock_seconds = 0
            clock_minutes = 0
            clock_hours = 0
            this_ticks = ticks
            seconds =  int(this_ticks/1000)
            #print(seconds)
            clock_hours = int(seconds/3600)
            clock_minutes = int((seconds-clock_hours*3600)/60)
            clock_seconds = int(seconds-((clock_hours*3600)+(clock_minutes*60)))

            format_1 = ""
            format_2 = ""
            format_3 = ""

            if clock_hours<10:
                format_1 = "0"
            if clock_minutes<10:
                format_2 = "0"
            if clock_seconds<10:
                format_3 = "0"

            return (format_1+str(clock_hours)+":"+format_2+str(clock_minutes)+":"+format_3+str(clock_seconds))
        else:
            return actual_text



            
                

