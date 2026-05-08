# SketchModifyRotate Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SketchModifyRotate`

Obsolete. Superseded by IModelDoc2::SketchModifyRotate.
Obsolete. Superseded by [IModelDoc2::SketchModifyRotate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchModifyRotate.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SketchModifyRotate( _
   ByVal CenterX As System.Double, _
   ByVal CenterY As System.Double, _
   ByVal Angle As System.Double _
) 
```

```

Dim instance As IModelDoc
Dim CenterX As System.Double
Dim CenterY As System.Double
Dim Angle As System.Double
 
instance.SketchModifyRotate(CenterX, CenterY, Angle)
```

```

void SketchModifyRotate( 
   System.double CenterX,
   System.double CenterY,
   System.double Angle
)
```

```

void SketchModifyRotate( 
   System.double CenterX,
   System.double CenterY,
   System.double Angle
) 
```

#### Parameters

*CenterX*

*CenterY*

*Angle*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
