# ICreateSheetFromSurface2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateSheetFromSurface2`

Creates a sheet (surface) body from a surface.
Creates a sheet (surface) body from a surface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateSheetFromSurface2( _
   ByVal SurfaceIn As Surface, _
   ByRef UvRange As System.Double _
) As Body2
```

```

Dim instance As IModeler
Dim SurfaceIn As Surface
Dim UvRange As System.Double
Dim value As Body2
 
value = instance.ICreateSheetFromSurface2(SurfaceIn, UvRange)
```

```

Body2 ICreateSheetFromSurface2( 
   Surface SurfaceIn,
   ref System.double UvRange
)
```

```

Body2^ ICreateSheetFromSurface2( 
   Surface^ SurfaceIn,
   System.double% UvRange
) 
```

#### Parameters

*SurfaceIn*
:   [Surface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md) from which you want to create this sheet body

*UvRange*
:   Array of UV values for this surface

#### Return Value

Newly created [body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)  
[IModeler::CreateSheetFromSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateSheetFromSurface.md)  
[IModeler::ICreateSheetFromFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateSheetFromFaces.md)  
[ISurface::CreateTrimmedSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~CreateTrimmedSheet.md)  
[IModeler::CreateSheetFromFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateSheetFromFaces.md)
