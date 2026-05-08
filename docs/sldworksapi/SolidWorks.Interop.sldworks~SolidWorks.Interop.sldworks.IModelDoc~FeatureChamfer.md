# FeatureChamfer Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~FeatureChamfer`

Obsolete. Superseded by IModelDoc2::FeatureChamfer.
Obsolete. Superseded by [IModelDoc2::FeatureChamfer](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FeatureChamfer.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub FeatureChamfer( _
   ByVal Width As System.Double, _
   ByVal Angle As System.Double, _
   ByVal Flip As System.Boolean _
) 
```

```

Dim instance As IModelDoc
Dim Width As System.Double
Dim Angle As System.Double
Dim Flip As System.Boolean
 
instance.FeatureChamfer(Width, Angle, Flip)
```

```

void FeatureChamfer( 
   System.double Width,
   System.double Angle,
   System.bool Flip
)
```

```

void FeatureChamfer( 
   System.double Width,
   System.double Angle,
   System.bool Flip
) 
```

#### Parameters

*Width*

*Angle*

*Flip*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
