class CryptoCalculator:
    def __init__(self):
        # self.profitPercent = 1.27 / 3.47 # BB Bot
        self.profitPercent = float(input('Profit Percent: '))
        self.totalOrders = int(input('Total Orders: '))
        self.invest = int(input('Invest: '))
        self.leverage = int(input('Leverage: '))

    def netProfitDaily(self):
        if self.leverage:
            makeFees = .03
            closeFees = .05
        else:
            makeFees = .1
            closeFees = .1

        totalProfit = 0
        for i in range(self.totalOrders):
            netInvest = self.invest - (self.invest * makeFees)
            profit = netInvest * (self.profitPercent * self.leverage) / 100
            netProfit = profit - (profit * closeFees)
            totalProfit += netProfit

        return totalProfit

    def profitMonthly(self):
        return self.netProfitDaily() * 30

    # def asset(self):
    #     return self.invest + self.profit()

    def formatIt(self, number):
        return "{:,}".format(int(number))

    def outPut(self):
        print(f'Daily: {self.formatIt(self.netProfitDaily())}T Monthly: {self.formatIt(self.profitMonthly())}T ')


CryptoCalculatorApp = CryptoCalculator()
CryptoCalculatorApp.outPut()