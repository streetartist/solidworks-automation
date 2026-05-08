# IGetOutline Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetOutline`

Gets the bounding box for a view (sheet or drawing) in meters on the drawing page.
Gets the bounding box for a view (sheet or drawing) in meters on the drawing page.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetOutline() As System.Double
```

```

Dim instance As IView
Dim value As System.Double
 
value = instance.IGetOutline()
```

```

System.double IGetOutline()
```

```

System.double IGetOutline(); 
```

#### Return Value

Array of doubles (see **Remarks**)

Remarks

The return value is an array of 4 doubles with the following format:

- 0, X min
- 1, Y min
- 2, X max
- 3, Y max

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetOutline Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetOutline.md)
