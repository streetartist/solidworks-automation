# GetIntersectSurfaceCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~GetIntersectSurfaceCount`

Gets the number of curves for a surface-surface intersection.
Gets the number of curves for a surface-surface intersection.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetIntersectSurfaceCount( _
   ByVal OtherSurface As Surface _
) As System.Integer
```

```

Dim instance As ISurface
Dim OtherSurface As Surface
Dim value As System.Integer
 
value = instance.GetIntersectSurfaceCount(OtherSurface)
```

```

System.int GetIntersectSurfaceCount( 
   Surface OtherSurface
)
```

```

System.int GetIntersectSurfaceCount( 
   Surface^ OtherSurface
) 
```

#### Parameters

*OtherSurface*
:   Other [surface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)

#### Return Value

Number of curves

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)  
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.md)  
[ISurface::IntersectSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IntersectSurface.md)  
[ISurface::IIntersectSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IIntersectSurface.md)
