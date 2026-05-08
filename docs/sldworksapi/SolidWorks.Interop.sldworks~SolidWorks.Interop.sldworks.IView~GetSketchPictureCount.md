# GetSketchPictureCount Method (IView)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSketchPictureCount`

Gets the number of sketch pictures imported to this view when a drawing is created from a part.
Gets the number of sketch pictures imported to this view when a drawing is created from a part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSketchPictureCount() As System.Integer
```

```

Dim instance As IView
Dim value As System.Integer
 
value = instance.GetSketchPictureCount()
```

```

System.int GetSketchPictureCount()
```

```

System.int GetSketchPictureCount(); 
```

#### Return Value

Number of sketch pictures in the view

Remarks

Only sketch pictures orthogonal to this view are counted.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetSketchPictures Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSketchPictures.md)  
[IView::IGetSketchPictures Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetSketchPictures.md)
