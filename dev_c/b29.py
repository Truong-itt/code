#include "stdio.h"
#include "string.h"
#include "time.h"
#include "conio.h"
struct date{
	int ngay;
	int thang;
	int nam;
};

struct SinhVien{
	int id;
	char ten[50];
	char gioiTinh[5];
	date ngaySinh;
	int tuoi;
	float diemMon1;
	float diemMon2;
	float diemMon3;
	float diemTrungBinh;
	char hocLuc[10];
	char maLop[30];
};
typedef SinhVien SV;



//void nhapSinhVien(SV &sv);
//void inSinhVien(SV sv);
//void tinhTuoi(SV &sv);
//void tinhDiemTrungBinh(SV *sv);
//void xepLoai(SV &sv);
//void capNhatSinhVien(SV &sv);
//void nhapDanhSachSinhVien(SV ds[], int &n);
//void xuatDanhSachSinhVien(SV ds[], int n);
//float timMax_DiemTrungBinh(SV ds[], int n);
//int timMin_Tuoi(SV ds[], int n);
//xuatDanhSachSinhVienXepLoai(SV ds[],int n,char xepLoai[]);
//void xuatDanhSachSinhVienTheoLop(SV ds[], int n, char lop[]);
//int timSinhVienTheoTen(SV ds[], int n, char ten[]);
//void xoaSinhVienTheoId(SV ds[], int &n, int id);
//void sapXepDanhSachSinhVienTheoDTB(SV ds[], int n);
//void sapXepDanhSachSinhVienTheoTen(SV ds[], int n);

void xoaXuongDong(char x[]){
	size_t len = strlen(x);
	if(x[len-1]=='\n'){
		x[len-1]='\0';
	}
}

void nhapSinhVien(SV &sv){
	printf("\nID: "); scanf("%d", &sv.id);
	printf("\nTen: "); fflush(stdin); fgets(sv.ten, sizeof(sv.ten), stdin); xoaXuongDong(sv.ten);
	printf("\nGioi tinh: "); fflush(stdin); fgets(sv.gioiTinh, sizeof(sv.gioiTinh), stdin); xoaXuongDong(sv.gioiTinh);
	printf("\nNgay sinh"); scanf("%d%d%d", &sv.ngaySinh.ngay, &sv.ngaySinh.thang, &sv.ngaySinh.nam);
	printf("\nDiem Mon 1: "); scanf("%f", &sv.diemMon1);
	printf("\nDiem Mon 2: "); scanf("%f", &sv.diemMon2);
	printf("\nDiem Mon 3: "); scanf("%f", &sv.diemMon3);
	printf("\nMa Lop: "); fflush(stdin); fgets(sv.maLop, sizeof(sv.maLop), stdin); xoaXuongDong(sv.maLop);
}

void inSinhVien(SV sv){
	printf("%5d \t %20s \t %10s \t %2d/%d/%d \t %10d \t %6.2f \t %6.2f \t %6.2f \t %6.2f \t\t %5s \t\t %10s", sv.id, sv.ten, sv.gioiTinh, sv.ngaySinh.ngay, sv.ngaySinh.thang, sv.ngaySinh.nam, sv.tuoi, sv.diemMon1, sv.diemMon2, sv.diemMon3, sv.diemTrungBinh, sv.hocLuc, sv.maLop);
}

void tinhTuoi(SV &sv){
	time_t TTIME = time(0);
	tm* NOW = localtime(&TTIME);
	int namHienTai = NOW->tm_year+1900;
	sv.tuoi = namHienTai - sv.ngaySinh.nam; 
}


void tinhDiemTrungBinh(SV *sv){
	sv->diemTrungBinh = (sv->diemMon1+sv->diemMon2+sv->diemMon3)/3;
}

void xepLoai(SV &sv){
	if(sv.diemTrungBinh>9){
		strcpy(sv.hocLuc, "XUAT SAC");
	}else if(sv.diemTrungBinh>8){
		strcpy(sv.hocLuc, "GIOI");
	}else if(sv.diemTrungBinh>7){
		strcpy(sv.hocLuc, "KHA");
	}else if(sv.diemTrungBinh>5){
		strcpy(sv.hocLuc, "TRUNG BINH");
	}else{
		strcpy(sv.hocLuc, "YEU");
	}
	
}

void capNhatSinhVien(SV &sv){
	nhapSinhVien(sv);
	tinhTuoi(sv);
	tinhDiemTrungBinh(&sv);
	xepLoai(sv);
}
void nhapDanhSachSinhVien(SV ds[], int &n){
	do{
		printf("\n nhap so sinh vien:");
		scanf("%d", &n);
	}while (n<=0);
	for (int i=0;i<n;i++){
		printf("\n nhap vao sinh vien thu %d:",i);
		capNhatSinhVien(ds[i]);
	}
}
void xuatDanhSachSinhVien(SV ds[], int n){
	printf("%5s \t %20s \t %10s \t %10s \t %10s \t %6s \t %6s \t %6s \t %6s \t %5s \t %10s", "ID", "Ten", "Gioi Tinh", "Ngay Sinh", "Tuoi", "Diem 1", "Diem 2", "Diem 3", "Diem TB", "XepLoai", "Ma Lop");
	printf("\n");
	for (int i=0;i<n;i++){
		inSinhVien(ds[i]);
		printf("\n");
	}
}
float timMax_DiemTrungBinh(SV ds[], int n){
	float max=ds[0].diemTrungBinh;
	for (int i=0;i<n;i++){
		if(max<ds[i].diemTrungBinh){
			max=ds[i].diemTrungBinh;
		}
	}
	return max;
}
int timMin_Tuoi(SV ds[], int n){
	int min=ds[0].tuoi;
	for (int i=0;i<n;i++){
		if(min>ds[i].tuoi){
			min=ds[i].tuoi;
		}
	}
	return min;
}
void xuatDanhSachSinhVienXepLoai(SV ds[], int n,char xepLoai[]){
	printf("\n\t\t\t\tDanh sach sinh vien loai gioi:\n");
	printf("%5s \t %20s \t %10s \t %10s \t %10s \t %6s \t %6s \t %6s \t %6s \t %5s \t %10s", "ID", "Ten", "Gioi Tinh", "Ngay Sinh", "Tuoi", "Diem 1", "Diem 2", "Diem 3", "Diem TB", "XepLoai", "Ma Lop");
	printf("\n");
	for (int i=0;i<n;i++){
		if(strcmp(strupr(ds[i].hocLuc),strupr(xepLoai))==0){
			inSinhVien(ds[i]);
		}
		printf("\n");
	}
}
void xuatDanhSachSinhVienTheoLop(SV ds[], int n, char lop[]){
	printf("\n\t\t\t\tDanh sach sinh vien theo lop %s:\n",lop);
	printf("%5s \t %20s \t %10s \t %10s \t %10s \t %6s \t %6s \t %6s \t %6s \t %5s \t %10s", "ID", "Ten", "Gioi Tinh", "Ngay Sinh", "Tuoi", "Diem 1", "Diem 2", "Diem 3", "Diem TB", "XepLoai", "Ma Lop");
	printf("\n");
	for (int i=0;i<n;i++){
		if(strcmp(strupr(ds[i].maLop),strupr(lop))==0){
			inSinhVien(ds[i]);
			printf("\n");
		}
	}
}
int timSinhVienTheoTen(SV ds[], int n, char ten[]){
	// 0 la false 1 la true
	// ham search strstr
	for (int i=0;i<n;i++){
		if(strstr(strupr(ds[i].ten),strupr(ten))>0){
			return 1;
		}
	}
	return 0;
}
void xoaSinhVienTheoId(SV ds[], int &n, int id){
	for (int i=0;i<n;i++){
		if(ds[i].id==id){
			for(int j=i;j<n;j++){// don cac sinh vien len
				ds[j]=ds[j+1];
			}
			n-=1;
			return;
		}
	}
}
void sapXepDanhSachSinhVienTheoDTB(SV ds[], int n){
	for(int i=0;i<n-1;i++){
		for(int j=i+1;j<n;j++){
			if(ds[i].diemTrungBinh>ds[j].diemTrungBinh){
				SV bien;
				bien=ds[i];
				ds[i]=ds[j];
				ds[j]=bien;
			}
		}
	}
}
void sapXepDanhSachSinhVienTheoTen(SV ds[], int n){
	for(int i=0;i<n-1;i++){
		for(int j=i+1;j<n;j++){// khi nhap vao no tu bt phan biet chu hoa va chu thiuong ta dung strupr
			if(strcmp(strupr(ds[i].ten),strupr(ds[j].ten))>0){
				SV bien;
				bien=ds[i];
				ds[i]=ds[j];
				ds[j]=bien;
			}
		}
	}
}
void nhapbatki(){
	printf("nhap bat ki de tiep tuc:");
	getch();
}
void nhapdanhsachsvtifile(SV ds[],int &n){
	char tenfile[30];
	printf("\nNHAP TEN FILE MUON NHAP VAO MANG:"); fflush(stdin); 
	fgets(tenfile, sizeof(tenfile), stdin); xoaXuongDong(tenfile);
	FILE *f;
	f=fopen(tenfile,"rb");
	if(f==NULL){
		printf("error file");
		return ;
	}
	fread(&n,sizeof(n),1,f);
	for (int i=0;i<n;i++){
		fread(&ds[i],sizeof(SV),1,f);
	}
	fclose(f);
}
void xuatdanhsachsvtufile(SV ds[],int n){
	char tenfile[30];
	printf("\nNHAP VAO TEN FILE DE TRUYEN VAO:"); fflush(stdin); 
	fgets(tenfile, sizeof(tenfile), stdin); xoaXuongDong(tenfile);
	FILE *f;
	f=fopen(tenfile,"wb");
	if(f==NULL){
		printf("error file");
		return ;
	}
	fwrite(&n,sizeof(n),1,f);
	for (int i=0;i<n;i++){
		fwrite(&ds[i],sizeof(SV),1,f);
	}
	fclose(f);
}
int main(){
//	SV sv1;
//	capNhatSinhVien(sv1);
//	printf("%5s \t %20s \t %10s \t %10s \t %10s \t %6s \t %6s \t %6s \t %6s \t %5s \t %10s", "ID", "Ten", "Gioi Tinh", "Ngay Sinh", "Tuoi", "Diem 1", "Diem 2", "Diem 3", "Diem TB", "XepLoai", "Ma Lop");
//	printf("\n");
//	inSinhVien(sv1);
	SV ds[100]; int n;
	int chon;
	do{
		printf("\nmenu:");
		printf("\nneu muon thuc hien cac yeu cau tu 2 tro di thi phai thuc hien buoc 1 truoc:");
		printf("\n1-nhap danh sach sinh vien:");
		printf("\n2-xuat danh sach sinh vien:");
		printf("\n3-tim max diemtb:");
		printf("\n4-tim min tuoi:");
		printf("\n5-xuat danh sach sinh vien theo lop:");
		printf("\n6-xuat danh sach sinh vien loai :");
		printf("\n7-sap sep sinh vien theo diem trung binh:");
		printf("\n8-sap sep sinh vien theo ten:");
		printf("\n9-tim sinh vien theo ten:");
		printf("\n10-xoa sinh vien theo id:");
		printf("\n11-NHAP DANH SACH SINH VIEN TU FILE:");
		printf("\n12-XUAT DANH SACH SINH VIEN TU FILE:");
		printf("\n0-thoat\n");
		printf("lua chon cua ban la:");
		scanf("%d",&chon);
		switch(chon){
			case 1:
				nhapDanhSachSinhVien(ds,n); 
				nhapbatki();
				break;
			case 2:
				xuatDanhSachSinhVien(ds, n); 
				nhapbatki();
				break;
			case 3:
				printf("\nDiem trung binh cao nhat :%.2f ",timMax_DiemTrungBinh(ds,n));
				nhapbatki(); 
				break;
			case 4:
				printf("\nSinh vien nho tuoi nhat la:%d ",timMin_Tuoi(ds,n)); 
				nhapbatki();
				break;
			case 5:
				char lop[20];
				printf("\n nhap ten lop:"); fflush(stdin); 
				fgets(lop, sizeof(lop), stdin); xoaXuongDong(lop);
				xuatDanhSachSinhVienTheoLop(ds,n,lop);
				nhapbatki();
				break;	
			case 6:
				char xepLoai[20];
				printf("\n nhap loai can hien thi:"); fflush(stdin); 
				fgets(xepLoai, sizeof(xepLoai), stdin); xoaXuongDong(xepLoai);
				xuatDanhSachSinhVienXepLoai(ds,n,xepLoai);
				nhapbatki();
				break;	
			case 7:
				sapXepDanhSachSinhVienTheoDTB(ds,n);
				printf("\n\t\t\tDanh sach sinh vien theo diem trung binh\n");
				xuatDanhSachSinhVien(ds, n);
				nhapbatki();
				break;
			case 8:
				sapXepDanhSachSinhVienTheoTen(ds,n);
				printf("\n\t\t\tDanh sach sinh vien theo ten\n");
				xuatDanhSachSinhVien(ds, n);
				nhapbatki();
				break;
			case 9:
				char tensv[15];
				printf("\n nhap ten sinh vien can tim:"); fflush(stdin); 
				fgets(tensv, sizeof(tensv), stdin); xoaXuongDong(tensv);
				printf("\nket qua tim sinh vien:%s", timSinhVienTheoTen(ds,n,tensv)==1? "co trong danh sach":"khong co trong danh sach");
				nhapbatki();
				break;
			case 10:
				int id; printf("\n nhap id can xoa:");
				scanf("%d",&id);
				xoaSinhVienTheoId(ds,n,id);
				printf("\nDanh sach sinh vien sau khi xoa\n");
				xuatDanhSachSinhVien(ds, n);
				nhapbatki();
				break;
			case 11:
				nhapdanhsachsvtifile(ds,n);
				nhapbatki();
				break;
			case 12:
				xuatdanhsachsvtufile(ds,n);
				nhapbatki();
				break;
		}
	}while (chon!=0);
//	nhapDanhSachSinhVien(ds, n);
//	xuatDanhSachSinhVien(ds, n);
//	printf("\nDiem trung binh cao nhat :%.2f ",timMax_DiemTrungBinh(ds,n));
//	printf("\nSinh vien nho tuoi nhat la:%d ",timMin_Tuoi(ds,n));
//	xuatDanhSachSinhVienTheoLop(ds,n,"DH01");
////	xuatDanhSachSinhVienXepLoaiGioi(ds,n);
//	printf("\nket qua tim sinh vien:%d", timSinhVienTheoTen(ds,n,"AN"));
//	sapXepDanhSachSinhVienTheoDTB(ds,n);
//	printf("\n\t\t\tDanh sach sinh vien theo diem trung binh\n");
//	xuatDanhSachSinhVien(ds, n);
//	sapXepDanhSachSinhVienTheoTen(ds,n);
//	printf("\n\t\t\tDanh sach sinh vien theo ten\n");
//	xuatDanhSachSinhVien(ds, n);
//	xoaSinhVienTheoId(ds,n,1);
//	printf("\nDanh sach sinh vien sau khi xoa\n");
//	xuatDanhSachSinhVien(ds, n);
}
