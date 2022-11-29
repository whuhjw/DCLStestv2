import numpy as np
import numpy as np
import os,time
import matplotlib.pylab as plt
from epics import caput,caget


class Algorithm_result():
    def Amp_display(self,list_number):
        # caget amp_get 0-1 VM1,REF,SSA1,KLY1,DEFL1,LOAD1,KLYRE1,VM2,SSA2,KLY2,DEFL2,LOAD2,KLYRE2
        amp_get = np.arange(12, dtype='f')
        amp_get[0] = 1
        amp_get[1] = 2
        amp_get[2] = 3
        amp_get[3] = 4
        amp_get[4] = 5
        amp_get[5] = 6
        amp_get[6] = 7
        amp_get[7] = 8
        amp_get[8] = 9
        amp_get[9] = 10
        amp_get[10] = 11
        amp_get[11] = 12
        list = np.arange(12, dtype='f')
        list[0] = amp_get[0] + list_number[0]
        list[1] = amp_get[1] + list_number[1]
        list[2] = amp_get[2] + list_number[2]
        list[3] = amp_get[3] + list_number[3]
        list[4] = amp_get[4] + list_number[4]
        list[5] = amp_get[5] + list_number[5]
        list[6] = amp_get[6] + list_number[6]

        list[7] = amp_get[7] + list_number[0]
        list[8] = amp_get[8] + list_number[2]
        list[9] = amp_get[9] + list_number[3]
        list[10] = amp_get[10] + list_number[4]
        list[11] = amp_get[11] + list_number[5]
        # print(list)
        return list
    def Pha_display(self,list_number):
        # caget pha_get,0-10,VM1,REF,SSA1,KLY1,DEFL1,LOAD1,VM2,SSA2,KLY2,DEFL2,LOAD2
        pha_get = np.arange(11, dtype='f')
        pha_get[0] = 1
        pha_get[1] = 2
        pha_get[2] = 3
        pha_get[3] = 4
        pha_get[4] = 5
        pha_get[5] = 6
        pha_get[6] = 7
        pha_get[7] = 8
        pha_get[8] = 9
        pha_get[9] = 10
        pha_get[10] = 11
        list = np.arange(11, dtype='f')
        list[0] = pha_get[0] + list_number[0]
        list[1] = pha_get[1] + list_number[1]
        list[2] = pha_get[2] + list_number[2]
        list[3] = pha_get[3] + list_number[3]
        list[4] = pha_get[4] + list_number[4]
        list[5] = pha_get[5] + list_number[5]

        list[6] = pha_get[6] + list_number[0]
        list[7] = pha_get[7] + list_number[2]
        list[8] = pha_get[8] + list_number[3]
        list[9] = pha_get[9] + list_number[4]
        list[10] = pha_get[10] + list_number[5]
        # print(list)
        return list
    def IQ_correct(self,point,range,left,right,times):
        list=np.arange(7,dtype='f')
        list[0] = 1+left
        list[1] = 2+left
        list[2] = 3+left
        list[3] = 4+left
        list[4] = 5+left
        list[5] = 6+left
        list[6] = 7+left
        return list

    # IQ矫正矩阵结果发布成pv量
    def siscorr(coff, *args):
        if len(args) == 0:
            caput(('SIS' + '.IOFFSET'), coff(0, 0));
            caput(('SIS' + '.QOFFSET'), coff(1, 0));
            caput(('SIS' + '.IQCOFFA'), coff(0, 1));
            caput(('SIS' + '.IQCOFFB'), coff(0, 2));
            caput(('SIS' + '.IQCOFFC'), coff(1, 1));
            caput(('SIS' + '.IQCOFFD'), coff(1, 2));
        else:
            caput(('SIS' + '.RMCOFFA'), coff(0, 0));
            caput(('SIS' + '.RMCOFFB'), coff(0, 1));
            caput(('SIS' + '.RMCOFFC'), coff(1, 0));
            caput(('SIS' + '.RMCOFFD'), coff(1, 1));
            caput(('SIS' + '.KGAIN'), args);

    def sisout(iout, qout, ch):
        if ch == 1:
            caput('SIS' + ':IOUT', iout)
            caput('SIS' + ':IOUT.RARM', 1)

            caput('SIS' + ':QOUT', qout)
            caput('SIS' + ':QOUT.RARM', 1)

            vec = iout + 1j * qout
            ampout = abs(vec)
            caput('SIS' + ':AMPOUT', ampout)
            caput('SIS' + ':AMPOUT.RARM', 1)

            caput('SIS' + '.UPDATE', 'YES');
        if ch == 2:
            caput('SIS' + ':IOUT2', iout)
            caput('SIS' + ':IOUT2.RARM', 1)

            caput('SIS' + ':QOUT2', qout)
            caput('SIS' + ':QOUT2.RARM', 1)

            vec = iout + 1j * qout
            ampout = abs(vec)
            caput('SIS' + ':AMPOUT2', ampout)
            caput('SIS' + ':AMPOUT2.RARM', 1)

            caput('SIS' + '.UPDATE', 'YES');
    def siscorr(coff, *args):
        if len(args) == 0:
            caput(('SIS' + '.IOFFSET'), coff(0, 0));
            caput(('SIS' + '.QOFFSET'), coff(1, 0));
            caput(('SIS' + '.IQCOFFA'), coff(0, 1));
            caput(('SIS' + '.IQCOFFB'), coff(0, 2));
            caput(('SIS' + '.IQCOFFC'), coff(1, 1));
            caput(('SIS' + '.IQCOFFD'), coff(1, 2));
        else:
            caput(('SIS' + '.RMCOFFA'), coff(0, 0));
            caput(('SIS' + '.RMCOFFB'), coff(0, 1));
            caput(('SIS' + '.RMCOFFC'), coff(1, 0));
            caput(('SIS' + '.RMCOFFD'), coff(1, 1));
            caput(('SIS' + '.KGAIN'), args);
    def sisin(self):
        out = np.zeros([11, 1023]);

        caput(('SIS' + '.TRIG'), 'YES');
        caput(('SIS' + '.ACQ'), 'YES');

        caput(('SIS' + ':Q1.RARM'), 1);
        tmp = caget('SIS' + ':Q1')
        qtmp = tmp[1:1024];
        caput(('SIS' + ':I1.RARM'), 1);
        tmp = caget(('SIS' + ':I1'));
        itmp = tmp[1:1024];
        out[0, :] = itmp + 1j * qtmp;

        caput(('SIS' + ':Q2.RARM'), 1);
        tmp = caget(('SIS' + ':Q2'));
        qtmp = tmp[1:1024];
        caput(('SIS' + ':I2.RARM'), 1);
        tmp = caget(('SIS' + ':I2'));
        itmp = tmp[1:1024];
        out[1, :] = itmp + 1j * qtmp;

        caput(('SIS' + ':Q3.RARM'), 1);
        tmp = caget(('SIS' + ':Q3'));
        qtmp = tmp[1:1024];
        caput(('SIS' + ':I3.RARM'), 1);
        tmp = caget(('SIS' + ':I3'));
        itmp = tmp[1:1024];
        out[2, :] = itmp + 1j * qtmp;

        caput(('SIS' + ':Q4.RARM'), 1);
        tmp = caget(('SIS' + ':Q4'));
        qtmp = tmp[1:1024];
        caput(('SIS' + ':I4.RARM'), 1);
        tmp = caget(('SIS' + ':I4'));
        itmp = tmp[1:1024];
        out[3, :] = itmp + 1j * qtmp;

        caput(('SIS' + ':Q5.RARM'), 1);
        tmp = caget(('SIS' + ':Q5'));
        qtmp = tmp[1:1024];
        caput(('SIS' + ':I5.RARM'), 1);
        tmp = caget(('SIS' + ':I5'));
        itmp = tmp[1:1024];
        out[4, :] = itmp + 1j * qtmp;

        caput(('SIS' + ':Q6.RARM'), 1);
        tmp = caget(('SIS' + ':Q6'));
        qtmp = tmp[1:1024];
        caput(('SIS' + ':I6.RARM'), 1);
        tmp = caget(('SIS' + ':I6'));
        itmp = tmp[1:1024];
        out[5, :] = itmp + 1j * qtmp;

        caput(('SIS' + ':QREF.RARM'), 1);
        tmp = caget(('SIS' + ':QREF'));
        qtmp = tmp[1:1024];
        caput(('SIS' + ':IREF.RARM'), 1);
        tmp = caget(('SIS' + ':IREF'));
        itmp = tmp[1:1024];
        out[6, :] = itmp + 1j * qtmp;

        caput(('SIS' + ':QVM.RARM'), 1);
        tmp = caget(('SIS' + ':QVM'));
        qtmp = tmp[1:1024];
        caput(('SIS' + ':IVM.RARM'), 1);
        tmp = caget(('SIS' + ':IVM'));
        itmp = tmp[1:1024];
        out[7, :] = itmp + 1j * qtmp;

        caput(('SIS' + ':DC0.RARM'), 1);
        tmp = caget(('SIS' + ':DC0'));
        out[8, :] = tmp[1:1024];

        caput(('SIS' + ':DC1.RARM'), 1);
        tmp = caget(('SIS' + ':DC1'));
        out[9, :] = tmp[1:1024];

        tmp = caget(('SIS' + '.DELTAIQ'));
        out[10, :] = tmp * np.ones(1023);
        return out
    def VM_correct(self):
        low = 1500;
        high = 7500;
        step = 300;
        res = 24;

        radius = np.arange(low, high + step, step);
        theta = np.arange(0, res, 1) / res * 2 * np.pi;

        iter_ = len(radius);
        gridnum = iter_ * res;

        iset = np.zeros([iter_, res]);
        qset = np.zeros([iter_, res]);
        imea = np.zeros([iter_, res]);
        qmea = np.zeros([iter_, res]);
        oset = np.ones(1024);
        bcoff = np.zeros([2, 3]);
        bcoff[0, 1] = 1;
        bcoff[1, 2] = 1;

        self.siscorr(bcoff);

        for n in range(1, iter_ + 1):
            iset[n - 1, :] = radius[n - 1] * np.cos(theta);
            qset[n - 1, :] = radius[n - 1] * np.sin(theta);

            for m in range(1, res + 1):
                self.sisout(iset[n - 1, m - 1] * oset, qset[n - 1, m - 1] * oset, 1);
                self.sisin();
                time.sleep(0.1);
                meas = self.sisin();

                vmtr = meas[7, :];
                imea[n, m] = np.real(np.mean(vmtr));
                qmea[n, m] = np.imag(np.mean(vmtr));

            plt.figure('1')
            plt.plot(iset[n - 1, :], qset[n - 1, :]);
            plt.figure('2')
            plt.plot(imea[n - 1, :], qmea[n - 1, :]);

        iset = np.reshape(iset, [1, gridnum])[0];
        qset = np.reshape(qset, [1, gridnum])[0];
        imea = np.reshape(imea, [1, gridnum])[0];
        qmea = np.reshape(qmea, [1, gridnum])[0];

        mm = np.array([list(np.ones(gridnum)), list(imea), list(qmea)]);
        u, s, v = np.linalg.svd(mm)
        coff = np.array(
            [list(iset.dot(v.dot(np.linalg.pinv(s).dot(u.T)))), list(qset.dot(v.dot(np.linalg.pinv(s).dot(u.T))))]);
        matrix = coff[:, 1:2];
        chi = matrix[0, 0] + 1j * matrix[0, 1];
        chq = matrix[1, 1] + 1j * matrix[1, 0];
        ampmis = abs(chi) / abs(chq);
        phimis = np.angle(chi * chq);
        bcoff = np.zeros([2, 3])
        bcoff[:, 0] = coff[:, 0];
        bcoff[:, 2:3] = [[ampmis, ampmis * np.sin(phimis) / np.cos(phimis)], [0, 1 / np.cos(phimis)]];

        self.siscorr(bcoff);
        print(' gain mismatch:' + '%s' % (round(1 / ampmis, 4)));
        print('phase mismatch:' + '%s' % (round(phimis / np.pi * 180, 4)));
        list=np.arange(6,dtype='f')
        list[0] = 1
        list[1] = 2
        list[2] = 3
        list[3] = 4
        list[4] = 5
        list[5] = 6
        return list

    def Steps(self,Amp1,Phase1,Amp2,Phase2,BW):
        print('hhhh')
        return list