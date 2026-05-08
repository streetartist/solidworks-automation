# GetPointOnSketchFromPixel Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture~GetPointOnSketchFromPixel`

Gets the sketch coordinate for the specified pixel.
Gets the sketch coordinate for the specified pixel.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetPointOnSketchFromPixel( _
   ByVal Row As System.Integer, _
   ByVal Column As System.Integer _
) As MathPoint
```

```

Dim instance As ISketchPicture
Dim Row As System.Integer
Dim Column As System.Integer
Dim value As MathPoint
 
value = instance.GetPointOnSketchFromPixel(Row, Column)
```

```

MathPoint GetPointOnSketchFromPixel( 
   System.int Row,
   System.int Column
)
```

```

MathPoint^ GetPointOnSketchFromPixel( 
   System.int Row,
   System.int Column
) 
```

#### Parameters

*Row*
:   Row for this pixel

*Column*
:   Column for this pixel

#### Return Value

[Point](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md) in the sketch space

Remarks

This method gets a point in the sketch space for the specified 0-based row and column indices from the pixel map. Because the bitmap data is raw data, this method helps determine where a point on the sketch is for the pixel after all of the transformation information has been applied. This method helps connect the raw data to its sketch.

See [ISketchPicture::GetPixelmap](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture~GetPixelmap.md) or [ISketchPicture::IGetPixelmap](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture~IGetPixelmap.md) for more information about the pixel map.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchPicture Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture.md)  
[ISketchPicture Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture_members.md)  
[ISketchPicture::GetPixelmapSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture~GetPixelmapSize.md)
