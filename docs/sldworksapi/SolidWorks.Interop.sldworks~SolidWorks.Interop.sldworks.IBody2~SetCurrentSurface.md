# SetCurrentSurface Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetCurrentSurface`

Places an existing surface into a temporary body that is under construction.
Places an existing surface into a temporary body that is under construction.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetCurrentSurface( _
   ByVal SurfaceIn As System.Object _
) 
```

```

Dim instance As IBody2
Dim SurfaceIn As System.Object
 
instance.SetCurrentSurface(SurfaceIn)
```

```

void SetCurrentSurface( 
   System.object SurfaceIn
)
```

```

void SetCurrentSurface( 
   System.Object^ SurfaceIn
) 
```

#### Parameters

*SurfaceIn*
:   Surface, which might have been created using other surface creation routines, such as [IModeler::CreateCylindricalSurface2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateCylindricalSurface2.md)

Remarks

This method is used with a set of related methods that construct a body from trimmed surfaces. This method takes an ISurface object created elsewhere and adds it to the temporary body object, which acts as a placeholder for the trimmed surfaces.

Follow calls to this method with one or more calls to the trimming-curve creation methods, such as [ISurface::AddTrimmingLoop2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~AddTrimmingLoop2.md). Then, trim the surface using [IBody2::CreateTrimmedSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateTrimmedSurface.md). After you add all the surfaces to the body and trim appropriately, you can sew the body to create an imported SOLIDWORKS body feature using [IBody2::CreateBodyFromSurfaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateBodyFromSurfaces.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)  
[IBody2::ISetCurrentSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ISetCurrentSurface.md)
