import sys
# argv[0] is the compute command itself

if sys.argv[1] == None or sys.argv[2] == None:
    print("Arguments were not provided")

try:
    threshold = float(sys.argv[1])
    limit = float(sys.argv[2])
    cusum = 0.0

    for line in sys.stdin:
        line = line.replace("\n","")
        input  = float(line)
        # apply the threshold logic
        out_val = max(0.0,input-threshold)
        total = out_val + cusum
        # apply the limit
        if total > limit:
            out_val -= total - limit
        cusum += out_val
        sys.stdout.write(str(out_val)+"\n")

    sys.stdout.write(str(cusum))

except IOError:
    print("IO error, check the standard input and standard output access")
except Exception:
    print("Error ocurred during computation")
