# FeatureCutThicken Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~FeatureCutThicken`

Obsolete. Superseded by IModelDoc2::FeatureCutThicken.
Obsolete. Superseded by [IModelDoc2::FeatureCutThicken](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FeatureCutThicken.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub FeatureCutThicken( _
   ByVal Thickness As System.Double, _
   ByVal Direction As System.Integer, _
   ByVal FaceIndex As System.Integer _
) 
```

```

Dim instance As IModelDoc
Dim Thickness As System.Double
Dim Direction As System.Integer
Dim FaceIndex As System.Integer
 
instance.FeatureCutThicken(Thickness, Direction, FaceIndex)
```

```

void FeatureCutThicken( 
   System.double Thickness,
   System.int Direction,
   System.int FaceIndex
)
```

```

void FeatureCutThicken( 
   System.double Thickness,
   System.int Direction,
   System.int FaceIndex
) 
```

#### Parameters

*Thickness*

*Direction*

*FaceIndex*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
