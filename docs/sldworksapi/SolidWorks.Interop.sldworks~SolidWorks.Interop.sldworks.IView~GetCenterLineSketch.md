# GetCenterLineSketch Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCenterLineSketch`

Gets the sketch that contains all of the centerline information for this view.
Gets the sketch that contains all of the centerline information for this view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCenterLineSketch() As Sketch
```

```

Dim instance As IView
Dim value As Sketch
 
value = instance.GetCenterLineSketch()
```

```

Sketch GetCenterLineSketch()
```

```

Sketch^ GetCenterLineSketch(); 
```

#### Return Value

[Sketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md)

Remarks

All of the centerlines for a drawing view are stored on a sketch. This method returns that sketch. You can get information about the sketch entities, including the centerlines, in the sketch.

This method allows you to access properties of individual centerlines. DXF translation may use this method to get the centerline information in a SOLIDWORKS drawing.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetFirstCenterLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstCenterLine.md)
