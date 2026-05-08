# IGetTrimCurveSize2 Method (IFace)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace~IGetTrimCurveSize2`

Obsolete. Superseded by IFace2::IGetTrimCurveSize2.
Obsolete. Superseded by [IFace2::IGetTrimCurveSize2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTrimCurveSize2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetTrimCurveSize2( _
   ByVal WantCubic As System.Integer, _
   ByVal WantNRational As System.Integer _
) As System.Integer
```

```

Dim instance As IFace
Dim WantCubic As System.Integer
Dim WantNRational As System.Integer
Dim value As System.Integer
 
value = instance.IGetTrimCurveSize2(WantCubic, WantNRational)
```

```

System.int IGetTrimCurveSize2( 
   System.int WantCubic,
   System.int WantNRational
)
```

```

System.int IGetTrimCurveSize2( 
   System.int WantCubic,
   System.int WantNRational
) 
```

#### Parameters

*WantCubic*

*WantNRational*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFace Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace.md)  
[IFace Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace_members.md)
