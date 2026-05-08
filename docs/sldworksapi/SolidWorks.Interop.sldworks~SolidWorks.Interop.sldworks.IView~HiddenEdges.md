# HiddenEdges Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~HiddenEdges`

Gets the hidden edges in the drawing view or sets the hidden edges in the drawing view to be visible.
Gets the hidden edges in the drawing view or sets the hidden edges in the drawing view to be visible.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property HiddenEdges As System.Object
```

```

Dim instance As IView
Dim value As System.Object
 
instance.HiddenEdges = value
 
value = instance.HiddenEdges
```

```

System.object HiddenEdges {get; set;}
```

```

property System.Object^ HiddenEdges {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of hidden [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)

Example

[Hide and Show All Edges in Drawing View (C#)](Hide_and_Show_All_Ediges_in_Drawing_View_Example_CSharp.htm)  
[Hide and Show All Edges in Drawing View (VB.NET)](Hide_and_Show_All_Ediges_in_Drawing_View_Example_VBNET.htm)  
[Hide and Show All Edges in Drawing View (VBA)](Hide_and_Show_All_Edges_in_Drawing_View_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IDrawingDoc::HideEdge Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~HideEdge.md)  
[IDrawingDoc::ShowEdge Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ShowEdge.md)
