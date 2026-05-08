# IGetBSurfParamsSize Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IGetBSurfParamsSize`

Obsolete. Superseded by ISurface::IGetBSurfParamsSize3.
Obsolete. Superseded by [ISurface::IGetBSurfParamsSize3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IGetBSurfParamsSize3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetBSurfParamsSize( _
   ByVal WantCubicRational As System.Boolean, _
   ByRef Range As System.Double _
) As System.Integer
```

```

Dim instance As ISurface
Dim WantCubicRational As System.Boolean
Dim Range As System.Double
Dim value As System.Integer
 
value = instance.IGetBSurfParamsSize(WantCubicRational, Range)
```

```

System.int IGetBSurfParamsSize( 
   System.bool WantCubicRational,
   ref System.double Range
)
```

```

System.int IGetBSurfParamsSize( 
   System.bool WantCubicRational,
   System.double% Range
) 
```

#### Parameters

*WantCubicRational*

*Range*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)  
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.md)
