document.addEventListener('DOMContentLoaded',function(){
    var si=document.getElementById('searchInput');
    var cb=document.getElementById('clearBtn');
    if(si){si.addEventListener('input',function(){if(cb)cb.style.display=this.value.length>0?'block':'none';})}
    var sf=document.getElementById('searchForm');
    if(sf){sf.addEventListener('submit',function(){
    var bt=document.querySelector('.btn-text');
    var bl=document.querySelector('.btn-loading');
    var sb=document.getElementById('searchBtn');
    if(bt)bt.style.display='none';
    if(bl)bl.style.display='inline';
    if(sb)sb.disabled=true;
    })}
    if('serviceWorker' in navigator){navigator.serviceWorker.register('/sw.js').catch(function(){});}
    });
    function clearSearch(){
    var si=document.getElementById('searchInput');
    var cb=document.getElementById('clearBtn');
    if(si){si.value='';si.focus();}
    if(cb)cb.style.display='none';
    }
    function setCategory(key){
    var ci=document.getElementById('categoryInput');
    if(ci)ci.value=key;
    document.querySelectorAll('.filter-btn').forEach(function(b){b.classList.remove('active');});
    var ab=document.querySelector('[data-category="'+key+'"]');
    if(ab)ab.classList.add('active');
    }
})