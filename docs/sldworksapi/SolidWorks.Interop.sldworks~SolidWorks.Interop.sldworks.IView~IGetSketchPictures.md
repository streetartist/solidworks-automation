# IGetSketchPictures Method (IView)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetSketchPictures`

Gets all of the sketch pictures imported to this view when a drawing is created from a part.
Gets all of the sketch pictures imported to this view when a drawing is created from a part.

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

Dim instance As IView
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
:   Number of sketch pictures in this view

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [ISketchPicture](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture.md)s
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_methods.htm) for details about this type of method.

Remarks

Use [IView::GetSketchPictureCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSketchPictureCount.md) to populate the Count parameter before calling this method. Only sketch pictures orthogonal to this view are returned.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetSketchPictures Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSketchPictures.md)
