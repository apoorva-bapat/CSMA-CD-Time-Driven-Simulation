# Apoorva Bapat
# CSMA CD Time Driven Simulation

import random


def main():
    S2 = random.randint(0,
                        100) % 8 + 16;# R5 total carrier length whose one end is at S0 pos 0 and S2 at pos at size-1 th position
    s0_pos = 0;
    s2_pos = S2;
    s0_frame_p = 8;  # length of s0
    s2_frame_p = 8;  # length of s2
    destS0 = 0; #destination s0
    destS1 = 0; #destination s1
    destS2 = 0; #destination s2
    count_delay_s0 = 0;
    count_delay_s1 = 0;
    count_delay_s2 = 0;
    tics_no_delay_s0 = 0;
    tics_no_delay_s1 = 0;
    tics_no_delay_s2 = 0;
    len_msg_s0 = 0;
    len_msg_s1 = 0;
    len_msg_s2 = 0;
    s0_trans_success = 0; #number of messages transmitted successfully
    s1_trans_success = 0;
    s2_trans_success = 0;
    s0_tics = 0; #tics required to send message from station
    s1_tics = 0;
    s2_tics = 0;
    tics_total_s0 = 0;
    tics_total_s1 = 0;
    tics_total_s2 = 0;
    transm_total = 0; #total messages transmitted
    jam_at_s0 = False; #Is there Jam in the station
    jam_at_s1 = False;
    jam_at_s2 = False;
    delay_S0 = False; #collision delay time
    delay_S1 = False;
    delay_S2 = False;
    curr_transmission_S0 = False; #checks if station is currently transmitting
    curr_transmission_S1 = False;
    curr_transmission_S2 = False;
    lastMessages_S0 = False;
    lastMessages_S1 = False;
    lastMessages_S2 = False;
    for i in range(1, 1501):  # Simulation runs over 1500 tics
        for j in range(0, 3):  # J = number of stations - s1, s2 and s3
            if (j == 0):  # Start from station 1 S0
                if (
                        s0_pos < 8 and s0_pos >= s0_frame_p):  # checks for collision between s1 and s2
                    jam_at_s0 = True;
                if (s0_pos >= s2_pos):  # checks for collision between s1 and s3
                    jam_at_s0 = True;
                if (
                        s0_pos == s0_frame_p or s0_pos == s2_frame_p):  # checks for collision between s 1,s 2 and s 3
                    jam_at_s0 = True;
                if (delay_S0 == True):  # checks if s0 station is introduced with time delay
                    jam_at_s0 = False;
                    if (count_delay_s0 == tics_no_delay_s0):  # if the delay of s0 equal to intended delay of s0
                        delay_S0 = False;
                        count_delay_s0 = 0;
                    if (count_delay_s0 < tics_no_delay_s0):
                        count_delay_s0 = count_delay_s0 + 1;  # if num of tics delay decreases, increments
                else:
                    if (jam_at_s0 != True and jam_at_s1 != True and jam_at_s2 != True):
                        if (curr_transmission_S0 != True):  # check if s1 is currently transmitting
                            if (
                                    lastMessages_S0 != True):#if last message not transmitted due to collision, assign tic value0
                                s0_tics = 0;
                            p1 = float(random.randint(0, 100)) / 100;  # Probability p1
                            destS0 = random.randint(0, 100) % 2 + 1;  # check the destination s0
                            len_msg_s0 = random.randint(0, 100) % 3 + 1;  # check the message length
                            if (p1 > 0.9):
                                curr_transmission_S0 = True;
                                s0_pos = s0_pos + 1;  #Message position increases as S0 goes towards Stations S2 or S1
                                s0_tics = s0_tics + 1;
                                transm_total = transm_total + 1;

                        else:
                            s0_pos = s0_pos + 1;
                            s0_tics = s0_tics + 1;

                    else:
                        lastMessages_S0 = True;
                        curr_transmission_S0 = False;
                        s0_pos = 0;
                        tics_no_delay_s0 = random.randint(0,
                                                          100) % 24 + 1;  # random no generated for tics for time delay
                        delay_S0 = True;
                        count_delay_s0 = 1;

                if (destS0 == 1 and s0_pos == 8):  # Message succesfully propogated from S0 to S1
                    tics_total_s0 = tics_total_s0 + s0_tics;
                    s0_trans_success = s0_trans_success + 1;
                    lastMessages_S0 = False;
                    s0_tics = 0;
                    curr_transmission_S0 = False;
                    s0_pos = 0;
                    destS0 = 0;
                if (destS0 == 2 and s0_pos == S2):  # Message succesfully propogated from S0 to S2
                    tics_total_s0 = tics_total_s0 + s0_tics;
                    s0_trans_success = s0_trans_success + 1;
                    lastMessages_S0 = False;
                    s0_tics = 0;
                    curr_transmission_S0 = False;
                    s0_pos = 0;
                    destS0 = 0;
            if (j == 1):  # checks for 2nd Station
                if (s0_pos >= s0_frame_p and s0_pos < 8):  # checks for collision between s 1 and s2
                    jam_at_s1 = True;
                if (s2_frame_p >= s2_pos and s2_pos > 8):  # checks for collision between s2 and s3
                    jam_at_s1 = True;
                if (
                        s0_frame_p == s2_pos or s2_frame_p == s0_pos):  # checks for collision between s1,s2 and s3
                    jam_at_s1 = True;
                if (
                        s0_pos - len_msg_s0 > 0):# checks for message of station 2 is not equals to any part of message of station1
                    tempPos_S0 = s0_pos; #s0 position assigned to an int variable temporarily
                    tempLenght_S0 = len_msg_s0; #s0 length assigned to an int variable temporarily
                    while (tempLenght_S0 != 0):
                        tempPos_S0 = tempPos_S0 - 1;
                        if (tempPos_S0 == s2_frame_p or tempPos_S0 == s0_frame_p):
                            jam_at_s1 = True;
                        tempLenght_S0 = tempLenght_S0 - 1;
                    tempPos_S0 = 0;
                    tempLenght_S0 = 0;
                if (
                        s2_pos + len_msg_s0 > S2):# checks if message frame of s2 is not overlapping with message frame of s3
                    tempPos_S2 = s2_pos;
                    tempLenght_S2 = len_msg_s2;
                    while (tempLenght_S2 != 0):
                        tempPos_S2 = tempPos_S2 + 1;
                        if (tempPos_S2 == s2_frame_p or tempPos_S2 == s0_frame_p):
                            jam_at_s1 = True;
                        tempLenght_S2 = tempLenght_S2 - 1;
                    tempPos_S2 = 0;
                    tempLenght_S2 = 0;
                if (delay_S1 == True):  # checks for the station is under collision delay time
                    jam_at_s1 = False;
                    if (count_delay_s1 == tics_no_delay_s1):  # checks for collision time is complete
                        delay_S1 = False;
                        count_delay_s1 = 0;
                    if (count_delay_s1 < tics_no_delay_s1):  # checks for collision time is not complete
                        count_delay_s1 = count_delay_s1 + 1;
                else:
                    if (jam_at_s0 != True and jam_at_s1 != True and jam_at_s2 != True):
                        if (curr_transmission_S1 != True):  # checks for there is current transmission ongoing
                            if (
                                    lastMessages_S1 != True):
                                s1_tics = 0;
                            p2 = float(random.randint(0, 100)) / 100;  # Probabilitty p2
                            destS1 = random.randint(0, 100) % 2 + 1;  # checks  destination
                            len_msg_s1 = random.randint(0, 100) % 3 + 1;  # checks  message length
                            if (p2 > 0.9):
                                curr_transmission_S1 = True;
                                s0_frame_p = s0_frame_p - 1;  # positions of frames  decremented as S1 goes towards S0
                                s2_frame_p = s2_frame_p + 1;  # positions of frames  incremented as S1 goes towards S2
                                s1_tics = s1_tics + 1;
                                transm_total = transm_total + 1;

                        else:
                            s0_frame_p = s0_frame_p - 1;
                            s2_frame_p = s2_frame_p + 1;
                            s1_tics = s1_tics + 1;

                    else:
                        lastMessages_S1 = True;
                        curr_transmission_S1 = False;
                        s0_frame_p = 8;
                        s2_frame_p = 8;
                        tics_no_delay_s1 = random.randint(0, 100) % 24 + 1;
                        delay_S1 = True;
                        count_delay_s1 = 1;
                if (destS1 == 1 and s0_frame_p == 0):  # Message succesfully reached from S1 to  S0
                    tics_total_s1 = tics_total_s1 + s1_tics;
                    s1_trans_success = s1_trans_success + 1;
                    lastMessages_S1 = False;
                    s1_tics = 0;
                    curr_transmission_S1 = False;
                    s0_frame_p = 8;
                    destS1 = 0;
                if (destS1 == 2 and s2_frame_p == S2):  # Message succesfully reached from  S1 to  S2
                    tics_total_s1 = tics_total_s1 + s1_tics;
                    s1_trans_success = s1_trans_success + 1;
                    lastMessages_S1 = False;
                    s1_tics = 0;
                    curr_transmission_S1 = False;
                    s2_frame_p = 8;
                    destS1 = 0;
            if (j == 2):  # Check the station 3
                if (
                        s2_frame_p >= s2_pos and s2_pos > 8):  # Check collision between S3 and S2
                    jam_at_s2 = True;
                if (s0_pos >= s2_pos):  #checks for collision occurs between S1 and S3
                    jam_at_s2 = True;
                if (
                        s0_frame_p == s2_pos or s2_frame_p == s2_pos):  # checks collision between S 1,S 2 and S 3
                    jam_at_s2 = True;
                if (delay_S2 == True):
                    jam_at_s2 = False;
                    if (count_delay_s0 == tics_no_delay_s2):  # checks if the collision time is complete
                        delay_S2 = False;
                        count_delay_s2 = 0;
                    if (count_delay_s2 < tics_no_delay_s2):  # checks if collision time is not yet complete
                        count_delay_s2 = count_delay_s2 + 1;
                else:
                    if (jam_at_s0 != True and jam_at_s1 != True and jam_at_s2 != True):
                        if (curr_transmission_S2 != True):  # checks if there is any current transmission going on
                            if (lastMessages_S2 != True):
                                s2_tics = 0;
                            p3 = float(random.randint(0, 100)) / 100;  # Probability P3
                            destS2 = random.randint(0, 100) % 2 + 1;  # Verify the destination
                            len_msg_s2 = random.randint(0, 100) % 3 + 1;  # Verify the message length
                        if (p3 > 0.9):
                            curr_transmission_S2 = True;
                            s2_pos = s2_pos - 1;  # positions decrements as S2 goes towards Stations S0 or S1
                            s2_tics = s2_tics + 1;
                            transm_total = transm_total + 1; #transmitted messages increases by 1
                        else:
                            s2_pos = s2_pos - 1;
                            s2_tics = s2_tics + 1;
                    else:
                        lastMessages_S2 = True;
                        curr_transmission_S2 = False;
                        s2_pos = 16;
                        tics_no_delay_s2 = random.randint(0, 100) % 24 + 1;
                        delay_S2 = True;
                        count_delay_s2 = 1;
                if (destS2 == 1 and s2_pos == 8):  # Message succesfully sent from s2 to s1
                    tics_total_s2 = tics_total_s2 + s2_tics;
                    s2_trans_success = s2_trans_success + 1;
                    lastMessages_S2 = False;
                    s2_tics = 0;
                    curr_transmission_S2 = False;
                    s2_pos = 16;
                    destS2 = 0;
                if (destS2 == 2 and s2_pos == 0):  # Message succesfully sent from s2 to s0
                    tics_total_s2 = tics_total_s2 + s2_tics;
                    s2_trans_success = s2_trans_success + 1;
                    lastMessages_S2 = False;
                    s2_tics = 0;
                    curr_transmission_S2 = False;
                    s2_pos = 16;
                    destS2 = 0;


    print("Number of Successful Messages transmitted from Station 0: ", s0_trans_success);
    print("Number of Successful Messages transmitted from Station 1: ", s1_trans_success);
    print("Number of Successful Messages transmitted from Station 2: ", s2_trans_success);
    print("--------------------------------------------------------");


#calculating the latency of each station
    if (s0_trans_success != 0):
        latency_stat_0 = (tics_total_s0 / s0_trans_success);
        print("Latency of Station 0 = ", "{:.3f}".format(latency_stat_0));
    if (s1_trans_success != 0):
        latency_stat_1 = (tics_total_s1 / s1_trans_success);
        print("Latency of Station 1 = ", "{:.3f}".format(latency_stat_1));
    if (s2_trans_success != 0):
        latency_stat_2 = (tics_total_s2 / s2_trans_success);
        print("Latency of Station 2 = ", "{:.3f}".format(latency_stat_2));
    print("--------------------------------------------------------");
    total_throughput = float(
        s0_trans_success + s1_trans_success + s2_trans_success) / float(transm_total);
    if (total_throughput > 0.0):
        print("Total Throughput : ", "{:.3f}".format(total_throughput));

main()
