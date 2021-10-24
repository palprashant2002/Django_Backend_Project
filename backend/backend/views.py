from django.http import HttpResponse
from django.shortcuts import render
def firstfunc(request):
    return render(request,'homepage.html')
def second(request):
    txt=request.POST.get('string','error')
    rmvp=request.POST.get('rmvpunc','error')
    rmvexw=request.POST.get('rmvexw','error')
    rmvnl=request.POST.get('rmvnl','error')
    chup=request.POST.get('upper','error')
    chlo=request.POST.get('lower','error')
    cnt=request.POST.get('count','error')
    punc='''!@#$%^&*()_+=-~`"}'}][{<>?/.,\|£¬'''
    work=""
    if(rmvp=='on'):
        ret=""
        for ch in txt:
            if ch not in punc:
                ret+=ch
        txt=ret
        work+="Removing Punctuation, "
    if(rmvexw=='on'):
        ret=""
        for ch in range(len(txt)-1):
            if not ((txt[ch]==" ")and(txt[ch+1]==" ")):
                ret+=txt[ch]
        txt=ret
        work+='Removing extra white spaces, '
    if(rmvnl=='on'):
        ret=""
        for ch in txt:
            if((ch!='\n')and(ch!='\r')):
                ret+=ch
        txt=ret
        work+="Removing newline, "
    if(chup=='on'):
        ret=""
        for ch in txt:
            ret+=ch.upper()
        txt=ret
        work+="Changing to UPPERCASE"
    if(chlo=='on'):
        ret=""
        for ch in txt:
            ret+=ch.lower()
        txt=ret
        work+="Changing to lowercase"
    diction={'oper':work,'comp_str':txt}
    if(cnt=='on'):
        s=0
        for ch in txt:
            if not((ch==' ')or(ch=='\n')):
                s+=1
        diction['quote']="Number of characters in string : "
        diction['char_count']=s
    if(rmvp==rmvexw==rmvnl==chup==chlo==cnt=='error'):
        return HttpResponse("<h1>Error!!!</h1><h4>No operation is chosen</h4>")
    else:
        return render(request,'secondpage.html',diction)