# GetPixelmapSize Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture~GetPixelmapSize`

Gets the size of the array for the picture pixels.
Gets the size of the array for the picture pixels.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetPixelmapSize( _
   ByRef Width As System.Integer, _
   ByRef Height As System.Integer _
) As System.Integer
```

```

Dim instance As ISketchPicture
Dim Width As System.Integer
Dim Height As System.Integer
Dim value As System.Integer
 
value = instance.GetPixelmapSize(Width, Height)
```

```

System.int GetPixelmapSize( 
   out System.int Width,
   out System.int Height
)
```

```

System.int GetPixelmapSize( 
   [Out] System.int Width,
   [Out] System.int Height
) 
```

#### Parameters

*Width*
:   Number of columns in the pixel map

*Height*
:   Number of rows in the pixel map

#### Return Value

Size of the array of the picture pixels

Remarks

Call this method before calling [ISketchPicture::IGetPixelmap](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture~IGetPixelmap.md) to get the size of the array for that method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchPicture Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture.md)  
[ISketchPicture Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture_members.md)  
[ISketchPicture::GetPixelmap Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture~GetPixelmap.md)  
[ISketchPicture::GetPointOnSketchFromPixel Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture~GetPointOnSketchFromPixel.md)
