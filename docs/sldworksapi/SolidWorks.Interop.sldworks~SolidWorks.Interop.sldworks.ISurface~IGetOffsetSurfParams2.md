# IGetOffsetSurfParams2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IGetOffsetSurfParams2`

Gets the overall offset distance of this offset surface.
Gets the overall offset distance of this offset surface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetOffsetSurfParams2( _
   ByRef BaseSurf As Surface, _
   ByRef Sense As System.Boolean _
) As System.Double
```

```

Dim instance As ISurface
Dim BaseSurf As Surface
Dim Sense As System.Boolean
Dim value As System.Double
 
value = instance.IGetOffsetSurfParams2(BaseSurf, Sense)
```

```

System.double IGetOffsetSurfParams2( 
   out Surface BaseSurf,
   out System.bool Sense
)
```

```

System.double IGetOffsetSurfParams2( 
   [Out] Surface^ BaseSurf,
   [Out] System.bool Sense
) 
```

#### Parameters

*BaseSurf*
:   Base [surface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md) used to generate the offset surface

*Sense*
:   If true, then the offset is in the direction of the original surface's normal; if false, then the offset is in the opposite direction of the original surface's normal

#### Return Value

Offset for the surface

Remarks

This method can get a pointer to the base surface and its sense. Both BaseSurf and Sense parameters can be a NULL pointer.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)  
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.md)  
[ISurface::GetOffsetSurfParams2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~GetOffsetSurfParams2.md)
