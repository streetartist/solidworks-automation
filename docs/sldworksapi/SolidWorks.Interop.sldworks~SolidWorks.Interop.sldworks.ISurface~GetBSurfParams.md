# GetBSurfParams Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~GetBSurfParams`

Obsolete. Superseded by ISurface::GetBSurfParams2.
Obsolete. Superseded by [ISurface::GetBSurfParams2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~GetBSurfParams2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetBSurfParams( _
   ByVal WantCubicRational As System.Boolean, _
   ByVal VP0 As System.Object _
) As System.Object
```

```

Dim instance As ISurface
Dim WantCubicRational As System.Boolean
Dim VP0 As System.Object
Dim value As System.Object
 
value = instance.GetBSurfParams(WantCubicRational, VP0)
```

```

System.object GetBSurfParams( 
   System.bool WantCubicRational,
   System.object VP0
)
```

```

System.Object^ GetBSurfParams( 
   System.bool WantCubicRational,
   System.Object^ VP0
) 
```

#### Parameters

*WantCubicRational*

*VP0*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)  
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.md)
