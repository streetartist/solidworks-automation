# IGetSketchPictures Method (ISketch)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSketchPictures`

Gets the pictures on this sketch.
Gets the pictures on this sketch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetSketchPictures( _
   ByVal Count As System.Integer _
) As SketchPicture
```

```

Dim instance As ISketch
Dim Count As System.Integer
Dim value As SketchPicture
 
value = instance.IGetSketchPictures(Count)
```

```

SketchPicture IGetSketchPictures( 
   System.int Count
)
```

```

SketchPicture^ IGetSketchPictures( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of pictures on this sketch

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [pictures](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture.md) on this sketch

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Call [ISketch::GetSketchPictureCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchPictureCount.md) before calling this method to get the value of Count.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md)  
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.md)  
[ISketch::GetSketchPictures Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchPictures.md)
