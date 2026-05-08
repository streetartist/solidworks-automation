# CreateTrimmedSurface Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateTrimmedSurface`

Creates a trimmed surface from a base surface and a list of existing trimming curves.
Creates a trimmed surface from a base surface and a list of existing trimming curves.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateTrimmedSurface() As System.Boolean
```

```

Dim instance As IBody2
Dim value As System.Boolean
 
value = instance.CreateTrimmedSurface()
```

```

System.bool CreateTrimmedSurface()
```

```

System.bool CreateTrimmedSurface(); 
```

#### Return Value

True if trimmed surface creation is successful, false if not

Remarks

Before you call this method, you must call one of the base-surface creation methods (such as [IBody2::CreatePlanarSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreatePlanarSurface.md) or [IBody2::ICreatePlanarSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreatePlanarSurface.md)) and the trimming-curve creation method [ISurface::AddTrimmingLoop2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~AddTrimmingLoop2.md) or [ISurface::IAddTrimmingLoops](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IAddTrimmingLoop2.md).

This method serves as the final call in a set of related functions that are designed to construct a trimmed surface from a base surface (possibly infinite) and a set of trimming curves.

If you want to construct a solid body from trimmed surfaces, call [IPartDoc::CreateNewBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~CreateNewBody.md) or [IPartDoc::ICreateNewBody2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ICreateNewBody2.md) first, which arranges for a place-holder for this trimmed surface.

Example

[Create Body Using Trimmed Surfaces (VBA)](Create_Body_using_Trimmed_Surfaces_Example_VB.htm)  
[Create Imported Surface Body from Sketch (C#)](Create_Imported_Surface_Body_from_Sketch_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)
