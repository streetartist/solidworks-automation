# GetTrimCurves2 Method (IFace)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace~GetTrimCurves2`

Obsolete. Superseded by IFace2::GetTrimCurves2.
Obsolete. Superseded by [IFace2::GetTrimCurves2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTrimCurves2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTrimCurves2( _
   ByVal WantCubic As System.Boolean, _
   ByVal WantNRational As System.Boolean _
) As System.Object
```

```

Dim instance As IFace
Dim WantCubic As System.Boolean
Dim WantNRational As System.Boolean
Dim value As System.Object
 
value = instance.GetTrimCurves2(WantCubic, WantNRational)
```

```

System.object GetTrimCurves2( 
   System.bool WantCubic,
   System.bool WantNRational
)
```

```

System.Object^ GetTrimCurves2( 
   System.bool WantCubic,
   System.bool WantNRational
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
