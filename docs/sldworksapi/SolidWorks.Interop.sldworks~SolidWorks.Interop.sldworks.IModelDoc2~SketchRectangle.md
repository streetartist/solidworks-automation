# SketchRectangle Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchRectangle`

Obsolete. Superseded by ISketchManager::CreateCornerRectangle.
Obsolete. Superseded by [ISketchManager::CreateCornerRectangle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateCornerRectangle.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SketchRectangle( _
   ByVal Val1 As System.Double, _
   ByVal Val2 As System.Double, _
   ByVal Z1 As System.Double, _
   ByVal Val3 As System.Double, _
   ByVal Val4 As System.Double, _
   ByVal Z2 As System.Double, _
   ByVal Val5 As System.Boolean _
) 
```

```

Dim instance As IModelDoc2
Dim Val1 As System.Double
Dim Val2 As System.Double
Dim Z1 As System.Double
Dim Val3 As System.Double
Dim Val4 As System.Double
Dim Z2 As System.Double
Dim Val5 As System.Boolean
 
instance.SketchRectangle(Val1, Val2, Z1, Val3, Val4, Z2, Val5)
```

```

void SketchRectangle( 
   System.double Val1,
   System.double Val2,
   System.double Z1,
   System.double Val3,
   System.double Val4,
   System.double Z2,
   System.bool Val5
)
```

```

void SketchRectangle( 
   System.double Val1,
   System.double Val2,
   System.double Z1,
   System.double Val3,
   System.double Val4,
   System.double Z2,
   System.bool Val5
) 
```

#### Parameters

*Val1*
:   Upper-left x value in meters

*Val2*
:   Upper-left y value in meters

*Z1*
:   Upper-left z value in meters

*Val3*
:   Lower-right x value in meters

*Val4*
:   Lower-right y value in meters

*Z2*
:   Lower-right z value in meters

*Val5*
:   Not used

Example

[Create Revolve Features (VBA)](Create_Revolve_Features_Example_VB.htm)  
[Connect to SOLIDWORKS Session (C#)](Connect_to_SOLIDWORKS_Session_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::SketchRectangleAtAnyAngle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchRectangleAtAnyAngle.md)
