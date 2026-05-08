# GraphicsRedrawEnabled Property (IDragOperator)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~GraphicsRedrawEnabled`

Gets or sets whether or not to update the graphics display after moving components.
Gets or sets whether or not to update the graphics display after moving components.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property GraphicsRedrawEnabled As System.Boolean
```

```

Dim instance As IDragOperator
Dim value As System.Boolean
 
instance.GraphicsRedrawEnabled = value
 
value = instance.GraphicsRedrawEnabled
```

```

System.bool GraphicsRedrawEnabled {get; set;}
```

```

property System.bool GraphicsRedrawEnabled {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to update the graphics display after moving components, false to not

Remarks

If this property is set to false, call [IModelDoc2::GraphicsRedraw2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GraphicsRedraw2.md) when you want to update the graphics display. This property is set to True by default.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDragOperator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator.md)  
[IDragOperator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator_members.md)
