# RotateAboutPoint Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~RotateAboutPoint`

Rotates the model view about the specified point by the specified angles in the directions of the screen X and Y axes.
Rotates the model view about the specified point by the specified angles in the directions of the screen X and Y axes.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub RotateAboutPoint( _
   ByVal XAngle As System.Double, _
   ByVal YAngle As System.Double, _
   ByVal Ptx As System.Double, _
   ByVal Pty As System.Double, _
   ByVal Ptz As System.Double _
) 
```

```

Dim instance As IModelView
Dim XAngle As System.Double
Dim YAngle As System.Double
Dim Ptx As System.Double
Dim Pty As System.Double
Dim Ptz As System.Double
 
instance.RotateAboutPoint(XAngle, YAngle, Ptx, Pty, Ptz)
```

```

void RotateAboutPoint( 
   System.double XAngle,
   System.double YAngle,
   System.double Ptx,
   System.double Pty,
   System.double Ptz
)
```

```

void RotateAboutPoint( 
   System.double XAngle,
   System.double YAngle,
   System.double Ptx,
   System.double Pty,
   System.double Ptz
) 
```

#### Parameters

*XAngle*
:   Rotation about the screen X axis

*YAngle*
:   Rotation about the screen Y axis

*Ptx*
:   Center of rotation

*Pty*
:   Center of rotation

*Ptz*
:   Center of rotation

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.md)  
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.md)  
[IModelView::RotateAboutAxis Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~RotateAboutAxis.md)  
[IModelView::RotateAboutCenter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~RotateAboutCenter.md)  
[IModelView::RotateAboutPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~RotateAboutPoint.md)
