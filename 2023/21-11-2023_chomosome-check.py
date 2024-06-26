"""The sperm cell determines the sex of an individual in this case. If a sperm cell containing an X 
chromosome fertilizes an egg, the resulting zygote will be XX
 or female. If the sperm cell contains a Y chromosome, then the resulting zygote will be XY or male.

Determine if the sex of the offspring will be male or female based on the X or Y chromosome present in the
 male's sperm.

If the sperm contains the X chromosome, return "Congratulations! You're going to have a daughter."; If the
 sperm contains the Y chromosome, return "Congratulations! You're going to have a son.";"""
def chromosome_check(chromosome):
    return {'XY': 'Congratulations! You\'re going to have a son.',
            'XX': 'Congratulations! You\'re going to have a daughter.'}.get(chromosome)
