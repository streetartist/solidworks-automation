# CreateSheetFromSurface Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateSheetFromSurface`

Creates a sheet (surface) body from a surface.
Creates a sheet (surface) body from a surface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateSheetFromSurface( _
   ByVal SurfaceIn As System.Object, _
   ByVal UvRange As System.Object _
) As System.Object
```

```

Dim instance As IModeler
Dim SurfaceIn As System.Object
Dim UvRange As System.Object
Dim value As System.Object
 
value = instance.CreateSheetFromSurface(SurfaceIn, UvRange)
```

```

System.object CreateSheetFromSurface( 
   System.object SurfaceIn,
   System.object UvRange
)
```

```

System.Object^ CreateSheetFromSurface( 
   System.Object^ SurfaceIn,
   System.Object^ UvRange
) 
```

#### Parameters

*SurfaceIn*
:   [Surface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md) from which you want to create this sheet body

*UvRange*
:   Array of UV values for this surface

#### Return Value

Newly created [body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

Example

[Cut Body in Half Using Macro Feature (VBA)](Cut_Body_in_Half_using_Macro_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)  
[IModeler::CreateSheetFromFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateSheetFromFaces.md)  
[IModeler::ICreateSheetFromFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateSheetFromFaces.md)  
[IModeler::ICreateSheetFromSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateSheetFromSurface2.md)  
[ISurface::CreateTrimmedSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~CreateTrimmedSheet.md)
