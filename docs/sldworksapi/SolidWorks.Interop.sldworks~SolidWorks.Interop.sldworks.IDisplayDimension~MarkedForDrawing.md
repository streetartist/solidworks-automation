# MarkedForDrawing Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~MarkedForDrawing`

Gets or sets whether this display dimension is marked to include in a drawing document.
Gets or sets whether this display dimension is marked to include in a drawing document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property MarkedForDrawing As System.Boolean
```

```

Dim instance As IDisplayDimension
Dim value As System.Boolean
 
instance.MarkedForDrawing = value
 
value = instance.MarkedForDrawing
```

```

System.bool MarkedForDrawing {get; set;}
```

```

property System.bool MarkedForDrawing {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if the display dimension is marked to include in the drawing document, false if not

Example

[Determine if Display Dimension Marked for Drawing (VBA)](Determine_if_Display_Dimension_Marked_for_Drawing_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)
