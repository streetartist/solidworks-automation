# IGetBSurfParamsSize2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IGetBSurfParamsSize2`

Obsolete. Superseded by ISurface::IGetBSurfParamsSize3.
Obsolete. Superseded by [ISurface::IGetBSurfParamsSize3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IGetBSurfParamsSize3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetBSurfParamsSize2( _
   ByVal WantCubic As System.Boolean, _
   ByVal WantNonRational As System.Boolean, _
   ByRef Range As System.Double _
) As System.Integer
```

```

Dim instance As ISurface
Dim WantCubic As System.Boolean
Dim WantNonRational As System.Boolean
Dim Range As System.Double
Dim value As System.Integer
 
value = instance.IGetBSurfParamsSize2(WantCubic, WantNonRational, Range)
```

```

System.int IGetBSurfParamsSize2( 
   System.bool WantCubic,
   System.bool WantNonRational,
   ref System.double Range
)
```

```

System.int IGetBSurfParamsSize2( 
   System.bool WantCubic,
   System.bool WantNonRational,
   System.double% Range
) 
```

#### Parameters

*WantCubic*

*WantNonRational*

*Range*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)  
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.md)
