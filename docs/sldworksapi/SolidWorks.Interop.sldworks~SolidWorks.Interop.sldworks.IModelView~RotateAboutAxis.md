# RotateAboutAxis Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~RotateAboutAxis`

Rotates the model view about a point, by an angle in the specified direction.
Rotates the model view about a point, by an angle in the specified direction.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub RotateAboutAxis( _
   ByVal Angle As System.Double, _
   ByVal Ptx As System.Double, _
   ByVal Pty As System.Double, _
   ByVal Ptz As System.Double, _
   ByVal AxisVecX As System.Double, _
   ByVal AxisVecY As System.Double, _
   ByVal AxisVecZ As System.Double _
) 
```

```

Dim instance As IModelView
Dim Angle As System.Double
Dim Ptx As System.Double
Dim Pty As System.Double
Dim Ptz As System.Double
Dim AxisVecX As System.Double
Dim AxisVecY As System.Double
Dim AxisVecZ As System.Double
 
instance.RotateAboutAxis(Angle, Ptx, Pty, Ptz, AxisVecX, AxisVecY, AxisVecZ)
```

```

void RotateAboutAxis( 
   System.double Angle,
   System.double Ptx,
   System.double Pty,
   System.double Ptz,
   System.double AxisVecX,
   System.double AxisVecY,
   System.double AxisVecZ
)
```

```

void RotateAboutAxis( 
   System.double Angle,
   System.double Ptx,
   System.double Pty,
   System.double Ptz,
   System.double AxisVecX,
   System.double AxisVecY,
   System.double AxisVecZ
) 
```

#### Parameters

*Angle*
:   Angle of rotation

*Ptx*
:   Center of rotation

*Pty*
:   Center of rotation

*Ptz*
:   Center of rotation

*AxisVecX*
:   Direction of axis of rotation

*AxisVecY*
:   Direction of axis of rotation

*AxisVecZ*
:   Direction of axis of rotation

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.md)  
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.md)  
[IModelView::RotateAboutCenter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~RotateAboutCenter.md)  
[IModelView::RotateAboutPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~RotateAboutPoint.md)  
[IModelView::StartDynamics Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~StartDynamics.md)
