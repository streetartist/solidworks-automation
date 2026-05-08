# SketchConvertIsoCurves Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SketchConvertIsoCurves`

Obsolete. Superseded by IModelDoc2::SketchConvertIsoCurves.
Obsolete. Superseded by [IModelDoc2::SketchConvertIsoCurves](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchConvertIsoCurves.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SketchConvertIsoCurves( _
   ByVal PercentRatio As System.Double, _
   ByVal VORuDir As System.Boolean, _
   ByVal DoConstrain As System.Boolean, _
   ByVal SkipHoles As System.Boolean _
) 
```

```

Dim instance As IModelDoc
Dim PercentRatio As System.Double
Dim VORuDir As System.Boolean
Dim DoConstrain As System.Boolean
Dim SkipHoles As System.Boolean
 
instance.SketchConvertIsoCurves(PercentRatio, VORuDir, DoConstrain, SkipHoles)
```

```

void SketchConvertIsoCurves( 
   System.double PercentRatio,
   System.bool VORuDir,
   System.bool DoConstrain,
   System.bool SkipHoles
)
```

```

void SketchConvertIsoCurves( 
   System.double PercentRatio,
   System.bool VORuDir,
   System.bool DoConstrain,
   System.bool SkipHoles
) 
```

#### Parameters

*PercentRatio*

*VORuDir*

*DoConstrain*

*SkipHoles*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
