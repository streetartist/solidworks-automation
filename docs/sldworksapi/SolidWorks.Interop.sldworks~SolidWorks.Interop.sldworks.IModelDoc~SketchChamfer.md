# SketchChamfer Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SketchChamfer`

Obsolete. Superseded by IModelDoc2::SketchChamfer.
Obsolete. Superseded by [IModelDoc2::SketchChamfer](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchChamfer.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SketchChamfer( _
   ByVal AngleORdist As System.Double, _
   ByVal Dist1 As System.Double, _
   ByVal Options As System.Integer _
) 
```

```

Dim instance As IModelDoc
Dim AngleORdist As System.Double
Dim Dist1 As System.Double
Dim Options As System.Integer
 
instance.SketchChamfer(AngleORdist, Dist1, Options)
```

```

void SketchChamfer( 
   System.double AngleORdist,
   System.double Dist1,
   System.int Options
)
```

```

void SketchChamfer( 
   System.double AngleORdist,
   System.double Dist1,
   System.int Options
) 
```

#### Parameters

*AngleORdist*

*Dist1*

*Options*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
