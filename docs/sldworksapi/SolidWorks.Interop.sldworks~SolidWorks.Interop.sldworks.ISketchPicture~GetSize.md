# GetSize Method (ISketchPicture)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture~GetSize`

Gets the size of the picture on the sketch.
Gets the size of the picture on the sketch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub GetSize( _
   ByRef Width As System.Double, _
   ByRef Height As System.Double _
) 
```

```

Dim instance As ISketchPicture
Dim Width As System.Double
Dim Height As System.Double
 
instance.GetSize(Width, Height)
```

```

void GetSize( 
   out System.double Width,
   out System.double Height
)
```

```

void GetSize( 
   [Out] System.double Width,
   [Out] System.double Height
) 
```

#### Parameters

*Width*
:   Width of the picture in meters

*Height*
:   Height of the picture in meters

Example

See the [ISketchPicture](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchPicture Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture.md)  
[ISketchPicture Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture_members.md)  
[ISketchPicture::SetSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture~SetSize.md)
