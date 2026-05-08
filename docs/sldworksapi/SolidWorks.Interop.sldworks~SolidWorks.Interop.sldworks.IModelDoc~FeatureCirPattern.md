# FeatureCirPattern Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~FeatureCirPattern`

Obsolete. Superseded by IModelDoc2::FeatureCirPattern.
Obsolete. Superseded by [IModelDoc2::FeatureCirPattern](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FeatureCirPattern.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub FeatureCirPattern( _
   ByVal Num As System.Integer, _
   ByVal Spacing As System.Double, _
   ByVal FlipDir As System.Boolean, _
   ByVal DName As System.String _
) 
```

```

Dim instance As IModelDoc
Dim Num As System.Integer
Dim Spacing As System.Double
Dim FlipDir As System.Boolean
Dim DName As System.String
 
instance.FeatureCirPattern(Num, Spacing, FlipDir, DName)
```

```

void FeatureCirPattern( 
   System.int Num,
   System.double Spacing,
   System.bool FlipDir,
   System.string DName
)
```

```

void FeatureCirPattern( 
   System.int Num,
   System.double Spacing,
   System.bool FlipDir,
   System.String^ DName
) 
```

#### Parameters

*Num*

*Spacing*

*FlipDir*

*DName*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
