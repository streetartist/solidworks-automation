# ICreateOffsetSurface Method (IBody)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~ICreateOffsetSurface`

Obsolete. Superseded by IBody2::ICreateOffsetSurface.
Obsolete. Superseded by [IBody2::ICreateOffsetSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateOffsetSurface.md).

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

Dim instance As IBody
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

*Distance*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.md)  
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.md)
