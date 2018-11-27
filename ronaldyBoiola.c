#include<stdio.h>
#include<stdlib.h>

typedef struct{
  int chave;
  struct noh* dir;
  struct noh* esq;
}noh;

typedef struct noh arvore;

void adicionaNoh(arvore *a,int num){
  if(a->chave == null){
    noh *no = (noh*) malloc(sizeof(noh));
    no->chave = num;
    no->dir = null;
    no->esq = null;
    a = no;
  }else if(a->chave > num){
    if(a->esq == null){
      noh *no = (noh*) malloc(sizeof(noh));
      no->chave = num;
      no->dir = null;
      no->esq = null;
      a->esq = no;
    }else{
      adicionaNoh(a->esq,num);
    }
  }else if(a->chave < num){
    if(a->dir == null){
      noh *no = (noh*) malloc(sizeof(noh));
      no->chave = num;
      no->dir = null;
      no->esq = null;
      a->dir = no;
    }else{
      adicionaNoh(a->dir,num);
    }
  }
}

int contarChave(arvore *a){
  int dir,esq,ch;
  dir=0;
  esq=0;
  if(a->dir != null){
    dir = contarChave(a->dir);
  }
  if(a->esq !=null){
    esq = contarChave(a->esq);
  }
  ch = dir + esq + a->chave;
  return ch;
}


void main(){
  arvore *a;

  a = null;
  adicionaNoh(a,10);
}
