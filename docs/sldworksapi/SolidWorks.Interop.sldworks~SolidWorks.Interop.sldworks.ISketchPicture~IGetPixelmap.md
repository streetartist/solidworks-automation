# IGetPixelmap Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture~IGetPixelmap`

Gets the picture pixels.
Gets the picture pixels.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetPixelmap( _
   ByVal Count As System.Integer _
) As System.Short
```

```

Dim instance As ISketchPicture
Dim Count As System.Integer
Dim value As System.Short
 
value = instance.IGetPixelmap(Count)
```

```

System.short IGetPixelmap( 
   System.int Count
)
```

```

System.short IGetPixelmap( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Size of the array

#### Return Value

- in-process, unmanaged C++: Pointer to an array containing groups of 3 or 4 values (see **Remarks**)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

The array contains groups of three, the Red, Green, Blue (RGB) components of pixel color, and optionally, a fourth value that indicates the transparency of the pixel, which can be a value from 0 (transparent) to 255 (opaque).

Before calling this method, call [ISketchPicture::GetPixelmapSize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture~GetPixelmapSize.md) to get the value of Count.

To determine the format of the data, you need the information returned by ISketchPicture::GetPixelmapSize:

Number of items per pixel = size / (rows \* columns)

Each group of three or four goes across each pixel in a row of the bitmap. The next row follows in the array.

This raw data does not include translation, scaling, rotation, and flipping. SOLIDWORKS applies these properties to the raw bitmap data to draw it in the sketch.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchPicture Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture.md)  
[ISketchPicture Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture_members.md)  
[ISketchPicture::GetPixelmap Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture~GetPixelmap.md)
