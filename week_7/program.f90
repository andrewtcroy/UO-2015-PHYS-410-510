            character*8 aa
          real x(10),z(10)
          aa='CraigUP'
          do i = 1,10
          x(i) = 4*i + 13
          z(i) = x(i)/2
! this will write to the screen
          write(*,101)  i,aa,x(i),z(i)
! this will write to a file named fort.20
          write(20,101) i,aa,x(i),z(i)
          end do
          write(*,*)"""success fort.20 created"""
 101    format('number',1x,i2,1x,a8,1x,']];',"'Aa'",2x,f4.1,2x,f4.1)
          stop
          end
