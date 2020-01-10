from datetime import datetime, timedelta
from itertools import accumulate

# The core code come from https://github.com/CutePandaSh/zhdate.git

class LunarDate():
    """
    从1900年到2100年的农历月份数据代码 20位二进制代码表示一个年份的数据，
    前四位0:表示闰月为29天，1:表示闰月为30天
    中间12位：从左起表示1-12月每月的大小，1为30天，0为29天
    最后四位：表示闰月的月份，0表示当年无闰月
    前四位和最后四位应该结合使用，如果最后四位为0，则不考虑前四位
    例：
    1901年代码为 19168，转成二进制为 0b100101011100000, 最后四位为0，当年无闰月，月份数据为 010010101110 分别代表12月的大小情况
    1903年代码为 21717，转成二进制为 0b101010011010101，最后四位为5，当年为闰五月，首四位为0，闰月为29天， 月份数据为 010101001101，分别代表12月的大小情况
    """
    CHINESEYEARCODE = [
        19416,
        19168, 42352, 21717, 53856, 55632, 91476, 22176, 39632,
        21970, 19168, 42422, 42192, 53840, 119381, 46400, 54944,
        44450, 38320, 84343, 18800, 42160, 46261, 27216, 27968,
        109396, 11104, 38256, 21234, 18800, 25958, 54432, 59984,
        92821, 23248, 11104, 100067, 37600, 116951, 51536, 54432,
        120998, 46416, 22176, 107956, 9680, 37584, 53938, 43344,
        46423, 27808, 46416, 86869, 19872, 42416, 83315, 21168,
        43432, 59728, 27296, 44710, 43856, 19296, 43748, 42352,
        21088, 62051, 55632, 23383, 22176, 38608, 19925, 19152,
        42192, 54484, 53840, 54616, 46400, 46752, 103846, 38320,
        18864, 43380, 42160, 45690, 27216, 27968, 44870, 43872,
        38256, 19189, 18800, 25776, 29859, 59984, 27480, 23232,
        43872, 38613, 37600, 51552, 55636, 54432, 55888, 30034,
        22176, 43959, 9680, 37584, 51893, 43344, 46240, 47780,
        44368, 21977, 19360, 42416, 86390, 21168, 43312, 31060,
        27296, 44368, 23378, 19296, 42726, 42208, 53856, 60005,
        54576, 23200, 30371, 38608, 19195, 19152, 42192, 118966,
        53840, 54560, 56645, 46496, 22224, 21938, 18864, 42359,
        42160, 43600, 111189, 27936, 44448, 84835, 37744, 18936,
        18800, 25776, 92326, 59984, 27296, 108228, 43744, 37600,
        53987, 51552, 54615, 54432, 55888, 23893, 22176, 42704,
        21972, 21200, 43448, 43344, 46240, 46758, 44368, 21920,
        43940, 42416, 21168, 45683, 26928, 29495, 27296, 44368,
        84821, 19296, 42352, 21732, 53600, 59752, 54560, 55968,
        92838, 22224, 19168, 43476, 41680, 53584, 62034, 54560
    ]

    '''
    从1900年，至2100年每年的农历春节的公历日期
    '''
    CHINESENEWYEAR = [
        '19000131',
        '19010219', '19020208', '19030129', '19040216', '19050204',
        '19060125', '19070213', '19080202', '19090122', '19100210',
        '19110130', '19120218', '19130206', '19140126', '19150214',
        '19160203', '19170123', '19180211', '19190201', '19200220',
        '19210208', '19220128', '19230216', '19240205', '19250124',
        '19260213', '19270202', '19280123', '19290210', '19300130',
        '19310217', '19320206', '19330126', '19340214', '19350204',
        '19360124', '19370211', '19380131', '19390219', '19400208',
        '19410127', '19420215', '19430205', '19440125', '19450213',
        '19460202', '19470122', '19480210', '19490129', '19500217',
        '19510206', '19520127', '19530214', '19540203', '19550124',
        '19560212', '19570131', '19580218', '19590208', '19600128',
        '19610215', '19620205', '19630125', '19640213', '19650202',
        '19660121', '19670209', '19680130', '19690217', '19700206',
        '19710127', '19720215', '19730203', '19740123', '19750211',
        '19760131', '19770218', '19780207', '19790128', '19800216',
        '19810205', '19820125', '19830213', '19840202', '19850220',
        '19860209', '19870129', '19880217', '19890206', '19900127',
        '19910215', '19920204', '19930123', '19940210', '19950131',
        '19960219', '19970207', '19980128', '19990216', '20000205',
        '20010124', '20020212', '20030201', '20040122', '20050209',
        '20060129', '20070218', '20080207', '20090126', '20100214',
        '20110203', '20120123', '20130210', '20140131', '20150219',
        '20160208', '20170128', '20180216', '20190205', '20200125',
        '20210212', '20220201', '20230122', '20240210', '20250129',
        '20260217', '20270206', '20280126', '20290213', '20300203',
        '20310123', '20320211', '20330131', '20340219', '20350208',
        '20360128', '20370215', '20380204', '20390124', '20400212',
        '20410201', '20420122', '20430210', '20440130', '20450217',
        '20460206', '20470126', '20480214', '20490202', '20500123',
        '20510211', '20520201', '20530219', '20540208', '20550128',
        '20560215', '20570204', '20580124', '20590212', '20600202',
        '20610121', '20620209', '20630129', '20640217', '20650205',
        '20660126', '20670214', '20680203', '20690123', '20700211',
        '20710131', '20720219', '20730207', '20740127', '20750215',
        '20760205', '20770124', '20780212', '20790202', '20800122',
        '20810209', '20820129', '20830217', '20840206', '20850126',
        '20860214', '20870203', '20880124', '20890210', '20900130',
        '20910218', '20920207', '20930127', '20940215', '20950205',
        '20960125', '20970212', '20980201', '20990121', '21000209'
    ]

    def __init__(self, lunar_year, lunar_month, lunar_day, leap_month=False):
        """初始化函数

        Arguments:
            lunar_year {int} -- 农历年
            lunar_month {int} -- 农历月份
            lunar_day {int} -- 农历日

        Keyword Arguments:
            leap_month {bool} -- 是否是在农历闰月中 (default: {False})

        """
        if not LunarDate.validate(lunar_year, lunar_month, lunar_day, leap_month):
            raise TypeError('农历日期不支持，超出农历1900年1月1日至2100年12月29日，或日期不存在')
        self.lunar_year = lunar_year
        self.lunar_month = lunar_month
        self.lunar_day = lunar_day
        self.leap_month = leap_month
        self.year_code = CHINESEYEARCODE[self.lunar_year - 1900]
        self.newyear = datetime.strptime(CHINESENEWYEAR[self.lunar_year - 1900], '%Y%m%d')

    def to_datetime(self):
        """农历日期转换称公历日期

        Returns:
            datetime -- 当前农历对应的公历日期
        """
        return self.newyear + timedelta(days=self.__days_passed())

    @staticmethod
    def from_datetime(dt):
        """静态方法，从公历日期生成农历日期

        Arguments:
            dt {datetime} -- 公历的日期

        Returns:
            LunarDate -- 生成的农历日期对象
        """
        lunar_year = dt.year
        if (datetime.strptime(CHINESENEWYEAR[lunar_year - 1900], '%Y%m%d') - dt).days > 0:
            lunar_year -= 1
        newyear_dt = datetime.strptime(CHINESENEWYEAR[lunar_year - 1900], '%Y%m%d')
        days_passed = (dt - newyear_dt).days
        year_code = CHINESEYEARCODE[lunar_year - 1900]
        month_days = LunarDate.decode(year_code)

        for pos, days in enumerate(accumulate(month_days)):
            if days_passed + 1 <= days:
                month = pos + 1
                lunar_day = month_days[pos] - (days - days_passed) + 1
                break

        leap_month = False
        if (year_code & 0xf) == 0 or month <= (year_code & 0xf):
            lunar_month = month
        else:
            lunar_month = month - 1

        if (year_code & 0xf) != 0 and month == (year_code & 0xf) + 1:
            leap_month = True

        return LunarDate(lunar_year, lunar_month, lunar_day, leap_month)

    @staticmethod
    def today():
        return LunarDate.from_datetime(datetime.now())

    def __days_passed(self):
        """私有方法，计算当前农历日期和当年农历新年之间的天数差值

        Returns:
            int -- 差值天数
        """
        month_days = LunarDate.decode(self.year_code)
        month_leap = self.year_code & 0xf  # 当前农历年的闰月，为0表示无润叶

        if (month_leap == 0) or (self.lunar_month < month_leap):  # 当年无闰月，或者有闰月但是当前月小于闰月
            days_passed_month = sum(month_days[:self.lunar_month - 1])
        elif (not self.leap_month) and (self.lunar_month == month_leap):  # 当前不是闰月，并且当前月份和闰月相同
            days_passed_month = sum(month_days[:self.lunar_month - 1])
        else:
            days_passed_month = sum(month_days[:self.lunar_month])

        return days_passed_month + self.lunar_day - 1

    def chinese(self):
        ZHNUMS = '零一二三四五六七八九十'
        zh_year = ''
        for i in range(0, 4):
            zh_year += ZHNUMS[int(str(self.lunar_year)[i])]
        zh_year += '年'

        if self.leap_month:
            zh_month = '闰'
        else:
            zh_month = ''

        if self.lunar_month == 1:
            zh_month += '正'
        elif self.lunar_month == 12:
            zh_month += '腊'
        elif self.lunar_month <= 10:
            zh_month += ZHNUMS[self.lunar_month]
        else:
            zh_month += f"十{ZHNUMS[self.lunar_month - 10]}"
        zh_month += '月'

        if self.lunar_day <= 10:
            zh_day = f'初{ZHNUMS[self.lunar_day]}'
        elif self.lunar_day < 20:
            zh_day = f'十{ZHNUMS[self.lunar_day - 10]}'
        elif self.lunar_day == 20:
            zh_day = '二十'
        elif self.lunar_day < 30:
            zh_day = f'二十{ZHNUMS[self.lunar_day - 20]}'
        else:
            zh_day = '三十'

        year_tiandi = LunarDate.__tiandi(self.lunar_year - 1900 + 36) + '年'

        shengxiao = "鼠牛虎兔龙蛇马羊猴鸡狗猪"

        return f"{zh_year}{zh_month}{zh_day} {year_tiandi} ({shengxiao[(self.lunar_year - 1900) % 12]}年)"

    def __str__(self):
        """打印字符串的方法

        Returns:
            str -- 标准格式农历日期字符串
        """
        if self.leap_month:
            return f"农历{self.lunar_year}年闰{self.lunar_month}月{self.lunar_day}日"
        else:
            return f"农历{self.lunar_year}年{self.lunar_month}月{self.lunar_day}日"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, another):
        if not isinstance(another, LunarDate):
            raise TypeError('比较必须都是LunarDate类型')
        cond1 = self.lunar_year == another.lunar_year
        cond2 = self.lunar_month == another.lunar_month
        cond3 = self.lunar_day == another.lunar_day
        cond4 = self.leap_month == another.leap_month
        return cond1 and cond2 and cond3 and cond4

    def __add__(self, another):
        if not isinstance(another, int):
            raise TypeError('加法只支持整数天数相加')
        return LunarDate.from_datetime(self.to_datetime() + timedelta(days=another))

    def __sub__(self, another):
        if isinstance(another, int):
            return LunarDate.from_datetime(self.to_datetime() - timedelta(days=another))
        elif isinstance(another, LunarDate):
            return (self.to_datetime() - another.to_datetime()).days
        elif isinstance(another, datetime):
            return (self.to_datetime() - another).days
        else:
            raise TypeError('减法只支持整数，LunarDate, Datetime类型')

    '''
    以下为帮助函数
    '''

    @staticmethod
    def __tiandi(anum):
        tian = '甲乙丙丁戊己庚辛壬癸'
        di = '子丑寅卯辰巳午未申酉戌亥'
        return f'{tian[anum % 10]}{di[anum % 12]}'

    @staticmethod
    def validate(year, month, day, leap):
        """农历日期校验

        Arguments:
            year {int} -- 农历年份
            month {int} -- 农历月份
            day {int} -- 农历日期
            leap {bool} -- 农历是否为闰月日期

        Returns:
            bool -- 校验是否通过
        """
        # 年份低于1900，大于2100，或者月份不属于 1-12，或者日期不属于 1-30，返回校验失败
        if not (1900 <= year <= 2100 and 1 <= month <= 12 and 1 <= day <= 30):
            return False

        year_code = CHINESEYEARCODE[year - 1900]

        # 有闰月标志
        if leap:
            if (year_code & 0xf) != month:  # 年度闰月和校验闰月不一致的话，返回校验失败
                return False
            elif day == 30:  # 如果日期是30的话，直接返回年度代码首位是否为1，即闰月是否为大月
                return (year_code >> 16) == 1
            else:  # 年度闰月和当前月份相同，日期不为30的情况，返回通过
                return True
        elif day <= 29:  # 非闰月，并且日期小于等于29，返回通过
            return True
        else:  # 非闰月日期为30，返回年度代码中的月份位是否为1，即是否为大月
            return ((year_code >> (12 - month) + 4) & 1) == 1

    @staticmethod
    def decode(year_code):
        """解析年度农历代码函数

        Arguments:
            year_code {int} -- 从年度代码数组中获取的代码整数

        Returns:
            [int] -- 当前年度代码解析以后形成的每月天数数组，已将闰月嵌入对应位置，即有闰月的年份返回长度为13，否则为12
        """
        month_days = list()
        for i in range(5, 17):
            if (year_code >> (i - 1)) & 1:
                month_days.insert(0, 30)
            else:
                month_days.insert(0, 29)
        if year_code & 0xf:
            if year_code >> 16:
                month_days.insert((year_code & 0xf), 30)
            else:
                month_days.insert((year_code & 0xf), 29)
        return month_days

    @staticmethod
    def month_days(year):
        """根据年份返回当前农历月份天数list

        Arguments:
            year {int} -- 1900到2100的之间的整数

        Returns:
            [int] -- 农历年份所对应的农历月份天数列表
        """
        return LunarDate.decode(
            CHINESEYEARCODE[year - 1900]
        )


    
"""the following code is copied from the network"""

import math
import ephem

def chinaCalendar(date): # 默认输入ut+8时间
    lunar_yue =["正月","二月","三月","四月","五月","六月","七月","八月","九月","十月","十一月","十二月"]
    nlrq = ["初一","初二","初三","初四","初五","初六","初七","初八","初九","初十","十一","十二","十三","十四","十五","十六","十七","十八","十九","二十","廿一","廿二","廿三","廿四","廿五","廿六","廿七","廿八","廿九","三十"]
    tiangan = ["甲","乙","丙","丁","戊","己","庚","辛","壬","癸"]
    dizhi = ["子","丑","寅","卯","辰","巳","午","未","申","酉","戌","亥"]
    gz = [''] * 60  # 六十甲子表
    for i in range(60):
        gz[i] = tiangan[i % 10] + dizhi[i % 12]

    def EquinoxSolsticeJD(year, angle):
        if 0 <= angle < 90:
            date = ephem.next_vernal_equinox(year)
        elif 90 <= angle < 180:
            date = ephem.next_summer_solstice(year)
        elif 180 <= angle < 270:
            date = ephem.next_autumn_equinox(year)
        else:
            date = ephem.next_winter_solstice(year)
        JD = ephem.julian_date(date)
        return JD

    # 计算二十四节气
    def SolarLongitube(JD):
        date = ephem.Date(JD - 2415020)
        s = ephem.Sun(date)  # date应为UT时间
        sa = ephem.Equatorial(s.ra, s.dec, epoch=date)
        se = ephem.Ecliptic(sa)
        L = se.lon / ephem.degree / 180 * math.pi
        return L

    def SolarTerms(year, angle):
        if angle > 270: year -= 1
        if year == 0: year -= 1  # 公元0改为公元前1
        JD = EquinoxSolsticeJD(str(year), angle)  # 初值
        JD1 = JD
        while True:
            JD2 = JD1
            L = SolarLongitube(JD2)
            JD1 += math.sin(angle * math.pi / 180 - L) / math.pi * 180
            if abs(JD1 - JD2) < 0.00001:
                break # 精度小于1 second
        return JD1 # UT

    def DateCompare(JD1, JD2): # 输入ut，返回ut+8的比较结果
        JD1 += 0.5 + 8/24
        JD2 += 0.5 + 8/24
        if int(JD1) >= int(JD2): return True
        else: return False

    def dzs_search(year): # 寻找年前冬至月朔日
        if year == 1: year -= 1  # 公元0改为公元前1
        dz = ephem.next_solstice(str(year-1) + '/12') # 年前冬至
        jd = ephem.julian_date(dz)
        # 可能的三种朔日
        date1 = ephem.next_new_moon(ephem.Date(jd - 2415020 - 0))
        jd1 = ephem.julian_date(date1)
        date2 = ephem.next_new_moon(ephem.Date(jd - 2415020 - 29))
        jd2 = ephem.julian_date(date2)
        date3 = ephem.next_new_moon(ephem.Date(jd - 2415020 - 31))
        jd3 = ephem.julian_date(date3)
        if DateCompare(jd, jd1): # 冬至合朔在同一日或下月
            return date1
        elif DateCompare(jd, jd2) and (not DateCompare(jd, jd1)):
            return date2
        elif DateCompare(jd, jd3): # 冬至在上月
            return date3
    
    
    JD = ephem.julian_date(date) - 8/24 # ut
    year = ephem.Date(JD + 8/24 - 2415020).triple()[0]
    shuo = []
    shuo.append(dzs_search(year))  # 冬至朔
    sJD1 = ephem.julian_date(shuo[0])
    next_dzs = dzs_search(year+1) # 次年冬至朔
    dzsJD = ephem.julian_date(next_dzs)
    if DateCompare(JD, dzsJD):
        shuo[0] = next_dzs
        next_dzs = dzs_search(year+2)
        dzsJD = ephem.julian_date(next_dzs)
    # 查找所在月及判断置闰
    run = ''
    szy = 0
    j = -1 # 计算连续两个冬至月中的合朔次数
    zry = 99 # 无效值
    flag = False
    while not DateCompare(sJD1, dzsJD): # 次年冬至朔前合朔即当年月份
        j += 1
        sJD1 = ephem.julian_date(shuo[j]) # 起冬至朔
        if DateCompare(JD, sJD1):
            szy += 1 # date所在月
            newmoon = int(sJD1 + 8/24 + 0.5)
        shuo.append(ephem.next_new_moon(shuo[j])) # i+1月朔
        if j == 0: continue # 冬至月一定含中气，从次月开始查找
        sJD2 = ephem.julian_date(shuo[j+1])  # 次月朔
        month = ephem.Date(sJD1 - 2415020).triple()[1] # 求某月的中气
        angle = (-90 + 30 * month) % 360 # 该月中气
        if j == 1:
            nian1 = ephem.Date(sJD1 - 2415020).triple()[0]
            qJD1 = SolarTerms(nian1, angle) # 每月中气
        else:
            qJD1 = qJD2 # 使用上次计算结果，节约计算
        nian2 = ephem.Date(sJD2 - 2415020).triple()[0]
        qJD2 = SolarTerms(nian2, (angle+30)%360) # 次月中气
        if not DateCompare(qJD1, sJD1) and DateCompare(qJD2, sJD2) and flag == False:
                zry = j + 1 # 置闰月
                flag = True # 仅第一个无中气月置闰
    rq = int(JD + 8/24 + 0.5) - newmoon # 日干支
    if j == 12 and zry != 99: # 连续两个冬至月间合朔12次则不闰
        zry = 99
    if szy % 12 == zry % 12 and zry != 99:
        run = '闰'
    if szy >= zry % 12 and zry != 99:
        szy -= 1
    # 判断节气月
    month = ephem.Date(date).triple()[1]
    angle = (-135 + 30 * month) % 360
    jJD2 = SolarTerms(year, (angle+30)%360) # 次月节气
    if angle == 225: # 再次月节气
        jJD3 = SolarTerms(year+1, (angle+60)%360)
    else:
        jJD3 = SolarTerms(year, (angle + 60) % 360)
    if angle == 255: # 每月节气
        jJD1 = SolarTerms(year-1, angle)
    else:
        jJD1 = SolarTerms(year, angle)
    daxue = False
    if DateCompare(JD, jJD3): # JD ≥ JD3
        jq = ephem.Date(jJD3 + 8/24 - 2415020)
        month2 = (angle + 15 - 210) // 30 % 12
        if angle == 225: daxue = True
    elif DateCompare(JD, jJD2): # JD2 ≤ JD ＜ JD3
        jq = ephem.Date(jJD2 + 8/24 - 2415020)
        month2 = (angle + 15 - 240) // 30 % 12
        if angle == 225 or (jq.triple()[1] == 12 and angle == 255): daxue = True  # 大雪或小寒
    else: # JD ＜ JD2
        jq = ephem.Date(jJD1 + 8/24 - 2415020)
        month2 = (angle + 15 - 270) // 30 % 12
        if angle == 255: daxue = True
    nian2 = jq.triple()[0]
    if nian2 < 0: nian2 += 1
    if daxue == True: nian2 += 1
    jqy = gz[(nian2 * 12 + month2 + 12) % 60] # 月干支
    if (szy - 3) % 12 >= 10 and ephem.Date(date).triple()[1] <= 3: year -= 1 # 年干支
    if year < 0: year += 1
        
    lunar_year = year
    lunar_month = (szy - 3) % 12 + 1
    lunar_day = rq + 1
    
    chinese_year = gz[(year - 4) % 60] + '年'
    chinese_month = jqy + '月'
    chinese_day = gz[int(JD + 8/24 + 0.5 + 49) % 60] + '日'
    return lunar_year, lunar_month, lunar_day, [chinese_year, chinese_month, chinese_day]