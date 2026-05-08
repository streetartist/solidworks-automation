# RotateAboutCenter Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~RotateAboutCenter`

Rotates the model view about the screen X and Y axes.
Rotates the model view about the screen X and Y axes.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub RotateAboutCenter( _
   ByVal XAngle As System.Double, _
   ByVal YAngle As System.Double _
) 
```

```

Dim instance As IModelView
Dim XAngle As System.Double
Dim YAngle As System.Double
 
instance.RotateAboutCenter(XAngle, YAngle)
```

```

void RotateAboutCenter( 
   System.double XAngle,
   System.double YAngle
)
```

```

void RotateAboutCenter( 
   System.double XAngle,
   System.double YAngle
) 
```

#### Parameters

*XAngle*
:   Rotation about the X axis

*YAngle*
:   Rotation about the Y axis

Example

[Change Wrap Feature Face (C#)](Change_Wrap_Feature_Face_Example_CSharp.htm)  
[Change Wrap Feature Face (VB.NET)](Change_Wrap_Feature_Face_Example_VBNET.htm)  
[Change Wrap Feature Face (VBA)](Change_Wrap_Feature_Face_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.md)  
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.md)  
[IModelView::RotateAboutAxis Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~RotateAboutAxis.md)  
[IModelView::RotateAboutPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~RotateAboutPoint.md)  
[IModelView::StartDynamics Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~StartDynamics.md)
