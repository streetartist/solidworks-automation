# SketchTrim Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchTrim`

Obsolete. Superseded by ISketchManager::SketchExtend and ISketchManager::SketchTrim.
Obsolete. Superseded by [ISketchManager::SketchExtend](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SketchExtend.md) and [ISketchManager::SketchTrim](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SketchTrim.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SketchTrim( _
   ByVal Op As System.Integer, _
   ByVal SelEnd As System.Integer, _
   ByVal X As System.Double, _
   ByVal Y As System.Double _
) 
```

```

Dim instance As IModelDoc2
Dim Op As System.Integer
Dim SelEnd As System.Integer
Dim X As System.Double
Dim Y As System.Double
 
instance.SketchTrim(Op, SelEnd, X, Y)
```

```

void SketchTrim( 
   System.int Op,
   System.int SelEnd,
   System.double X,
   System.double Y
)
```

```

void SketchTrim( 
   System.int Op,
   System.int SelEnd,
   System.double X,
   System.double Y
) 
```

#### Parameters

*Op*

*SelEnd*

*X*

*Y*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
