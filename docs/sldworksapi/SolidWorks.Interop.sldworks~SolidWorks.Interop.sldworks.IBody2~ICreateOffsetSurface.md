# ICreateOffsetSurface Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateOffsetSurface`

Creates a new surface offset from an existing surface.
Creates a new surface offset from an existing surface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateOffsetSurface( _
   ByVal SurfaceIn As Surface, _
   ByVal Distance As System.Double _
) As Surface
```

```

Dim instance As IBody2
Dim SurfaceIn As Surface
Dim Distance As System.Double
Dim value As Surface
 
value = instance.ICreateOffsetSurface(SurfaceIn, Distance)
```

```

Surface ICreateOffsetSurface( 
   Surface SurfaceIn,
   System.double Distance
)
```

```

Surface^ ICreateOffsetSurface( 
   Surface^ SurfaceIn,
   System.double Distance
) 
```

#### Parameters

*SurfaceIn*
:   [Surface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md) from which to offset the new surface

*Distance*
:   Offset distance

#### Return Value

Newly created offset [surface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)  
[IBody2::CreateOffsetSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateOffsetSurface.md)
