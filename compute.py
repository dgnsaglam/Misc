import sys
import decimal
# argv[0] is the compute command itself

if sys.argv[1] == None or sys.argv[2] == None:
    print("Arguments were not provided")

try:
    threshold = decimal.Decimal(sys.argv[1])
    limit = decimal.Decimal(sys.argv[2])
    cusum = decimal.Decimal(0)

    for line in sys.stdin:
        line = line.replace("\n","")
        input  = decimal.Decimal(line)
        # apply the threshold logic
        out_val = max(0,input-threshold)
        total = out_val + cusum
        # apply the limit
        if total > limit:
            tp = "ov:" + str(out_val) + " t:"+ str(total) + " l:"+ str(limit)
            out_val -= total - limit
        cusum += out_val
        sys.stdout.write("{:.10g}".format(out_val) + "\n")

    sys.stdout.write("{:.10g}".format(cusum))
    

except IOError:
    print("IO error, check the standard input and standard output access")
except Exception:
    print("Error ocurred during computation")
