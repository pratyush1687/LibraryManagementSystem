# import pickle
# arr=[1,2,3,4]
# p=[3,4,5,6]
# f=open("try.dat", mode="w+")
# pickle.dump(arr,f)
# pickle.dump(p,f)
# f.seek(0,0)
# while True:
#     try:
#         obj=pickle.load(f)
#         obj[0]="ab"
#         pickle.dump(obj, f)
#     except EOFError:
#         # f.close()
#         break
# f.seek(0,0)
# while True:
#     try:
#         obj=pickle.load(f)
#         # obj[0]="ab"
#         # pickle.dump(obj, f)
#         print obj
#     except EOFError:
#         f.close()
#         break
