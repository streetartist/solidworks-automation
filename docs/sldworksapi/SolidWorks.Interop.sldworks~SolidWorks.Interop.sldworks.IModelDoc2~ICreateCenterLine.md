# ICreateCenterLine Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreateCenterLine`

Creates a center line from P1 to P2.
Creates a center line from P1 to P2.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ICreateCenterLine( _
   ByRef P1 As System.Double, _
   ByRef P2 As System.Double _
) 
```

```

Dim instance As IModelDoc2
Dim P1 As System.Double
Dim P2 As System.Double
 
instance.ICreateCenterLine(P1, P2)
```

```

void ICreateCenterLine( 
   ref System.double P1,
   ref System.double P2
)
```

```

void ICreateCenterLine( 
   System.double% P1,
   System.double% P2
) 
```

#### Parameters

*P1*
:   Array of 3 doubles (x1, y1, z1) in meters that describe the first point of the line

*P2*
:   Array of 3 doubles (x2, y2, z2) in meters that describe the second point of the line

#### Return Value

True if success, false if not

Remarks

Use [IModelDoc2::CreateCenterLineVB](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateCenterLineVB.md) for Visual Basic for Applications (VBA) and other forms of Basic that do not support SafeArrays.

You can also create centerline construction geometry using [IModelDoc2::ICreateLine2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreateLine2.md) and [ISketchSegment::ConstructionGeometry](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~ConstructionGeometry.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::CreateCenterLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateCenterLine.md)
