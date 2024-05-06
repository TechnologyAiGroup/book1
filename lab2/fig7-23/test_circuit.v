module test_circuit (
    I1, I2, I3, I4, I5, I6, I7, O1, O2 
);
    input I1, I2, I3, I4, I5, I6, I7;
    output O1, O2;
    wire w1, w2, w3, w4;

    and AND_1 (w1, I1, I2);
    or OR_1 (w2, I3, I4);
    nor NOR_1 (w3, w2, I5);
    nand NAND_1 (w4, I6, I7);
    and AND_2 (O1, w1, w2);
    or OR_2 (O2, w3, w4);

endmodule
