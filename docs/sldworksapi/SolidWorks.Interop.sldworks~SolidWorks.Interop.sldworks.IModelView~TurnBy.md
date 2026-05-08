# TurnBy Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~TurnBy`

Rotates the camera by the specified angles about the camera's x and y axes.
Rotates the camera by the specified angles about the camera's x and y axes.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub TurnBy( _
   ByVal XAngle As System.Double, _
   ByVal YAngle As System.Double _
) 
```

```

Dim instance As IModelView
Dim XAngle As System.Double
Dim YAngle As System.Double
 
instance.TurnBy(XAngle, YAngle)
```

```

void TurnBy( 
   System.double XAngle,
   System.double YAngle
)
```

```

void TurnBy( 
   System.double XAngle,
   System.double YAngle
) 
```

#### Parameters

*XAngle*
:   Angle by which to rotate the camera about its x axis

*YAngle*
:   Angle by which to rotate the camera about its y axis

Remarks

The model view must have an active camera.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.md)  
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.md)  
[IModelView::Camera Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~Camera.md)
