# GetSketchPictures Method (IView)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSketchPictures`

Gets all of the sketch pictures imported to this view when a drawing is created from a part.
Gets all of the sketch pictures imported to this view when a drawing is created from a part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSketchPictures() As System.Object
```

```

Dim instance As IView
Dim value As System.Object
 
value = instance.GetSketchPictures()
```

```

System.object GetSketchPictures()
```

```

System.Object^ GetSketchPictures(); 
```

#### Return Value

Array of [ISketchPictures](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture.md)

Remarks

Only sketch pictures orthogonal to this view are returned.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::IGetSketchPictures Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetSketchPictures.md)  
[IView::GetSketchPictureCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSketchPictureCount.md)
