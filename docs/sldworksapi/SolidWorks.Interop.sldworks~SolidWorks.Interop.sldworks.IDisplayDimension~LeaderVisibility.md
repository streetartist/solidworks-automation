# LeaderVisibility Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~LeaderVisibility`

Gets or sets which leader lines (dimension lines) are visible on a display dimension.
Gets or sets which leader lines (dimension lines) are visible on a display dimension.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property LeaderVisibility As System.Integer
```

```

Dim instance As IDisplayDimension
Dim value As System.Integer
 
instance.LeaderVisibility = value
 
value = instance.LeaderVisibility
```

```

System.int LeaderVisibility {get; set;}
```

```

property System.int LeaderVisibility {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Leader visibility state as defined in [swLeaderLineVisibility\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLeaderLineVisibility_e.html)

Remarks

After using this property, use [IModelDoc2::GraphicsRedraw2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GraphicsRedraw2.md) to redraw the graphics window to see your changes.

Example

[Get Display Dimension Properties (VBA)](Get_Display_Dimension_Properties_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)
