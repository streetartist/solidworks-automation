# GetPixelmap Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture~GetPixelmap`

Gets the picture pixels.
Gets the picture pixels.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetPixelmap() As System.Object
```

```

Dim instance As ISketchPicture
Dim value As System.Object
 
value = instance.GetPixelmap()
```

```

System.object GetPixelmap()
```

```

System.Object^ GetPixelmap(); 
```

#### Return Value

Array containing groups of three or four values (see Remarks)

Remarks

The array contains groups of three, the Red, Green, Blue (RGB) components of pixel color, and optionally a fourth value that indicates the transparency of the pixel, which can be a value from 0 (transparent) to 255 (opaque).

To determine the format of the data, you need the information returned by [ISketchPicture::GetPixelmapSize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture~IGetPixelmap.md):

Number of items per pixel = size / (rows \* columns)

Each group of three or four goes across each pixel in a row of the bitmap. The next row follows in the array.

This raw data does not include translation, scaling, rotation, and flipping. SOLIDWORKS applies these properties to the raw bitmap data to draw it in the sketch.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchPicture Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture.md)  
[ISketchPicture Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture_members.md)  
[ISketchPicture::IGetPixelmap Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture~IGetPixelmap.md)  
[ISketchPicture::GetPointOnSketchFromPixel Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture~GetPointOnSketchFromPixel.md)
