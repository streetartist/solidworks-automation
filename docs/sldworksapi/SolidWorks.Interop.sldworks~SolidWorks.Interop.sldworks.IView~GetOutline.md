# GetOutline Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetOutline`

Gets the bounding box for a view (sheet or drawing) in meters on the drawing page.
Gets the bounding box for a view (sheet or drawing) in meters on the drawing page.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetOutline() As System.Object
```

```

Dim instance As IView
Dim value As System.Object
 
value = instance.GetOutline()
```

```

System.object GetOutline()
```

```

System.Object^ GetOutline(); 
```

#### Return Value

Array of doubles (see **Remarks**)

Remarks

The return value is an array of 4 doubles with the following format:

- 0, X min
- 1, Y min
- 2, X max
- 3, Y max

Example

[Reposition Drawing Views to Avoid Overlap (VBA)](Reposition_Drawing_Views_to_Avoid_Overlap_Example_VB.htm)  
[Select Entity in Drawing View (VBA)](Select_Entity_in_Drawing_View_Example_VB.htm)  
[Get View Bounding Box and Position (C#)](Get_View_Bounding_Box_and_Position_Example_CSharp.htm)  
[Get View Bounding Box and Position (C#)](Get_View_Bounding_Box_and_Position_Example_VBNET.htm)  
[Get View Bounding Box and Position (VBA)](Get_View_Bounding_Box_and_Position_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::IGetOutline Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetOutline.md)
