
@.str = private unnamed_addr constant [3 x i8] c"%d ", align 1

; Function Attrs: noinline nounwind uwtable
define i32 @main() #0 {
%1 = alloca i32, align 4
%2 = alloca i32, align 4
%3 = alloca i32, align 4
%4 = alloca i32, align 4
store i32 0, i32* %1, align 4
store i32 20, i32* %2, align 4
store i32 200, i32* %3, align 4
store i32 10, i32* %4, align 4
%5 = load i32, i32* %2, align 4
%6 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 %5)
%7 = load i32, i32* %4, align 4
%8 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 %7)
%9 = load i32, i32* %3, align 4
%10 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str, i32 0, i32 0), i32 %9)
ret i32 0
}

declare i32 @printf(i8*, ...) #1

