# Scale2 Property (IDisplayDimension)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~Scale2`

Gets or sets the scale value that is applied to the dimension value of this non-associative distance dimension.
Gets or sets the scale value that is applied to the dimension value of this non-associative distance dimension.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Scale2 As System.Double
```

```

Dim instance As IDisplayDimension
Dim value As System.Double
 
instance.Scale2 = value
 
value = instance.Scale2
```

```

System.double Scale2 {get; set;}
```

```

property System.double Scale2 {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Scale applied to the dimension value

Remarks

This scale value applies only to non-associative distance dimensions, such as those created using [IDrawingDoc::CreateLinearDim4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateLinearDim4.md) or [IDrawingDoc::CreateDiamDim4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateDiamDim4.md). For these dimensions, SOLIDWORKS multiplies the actual dimension measurement by this scale value to get the dimension value that is displayed on the screen. For any other types of dimensions (such as associative dimensions or angular measurement dimensions), setting the scale factor has no effect and getting the scale factor will always return 1.

The scale value must be greater than 0. This has no effect in the OLE interface, and returns S\_false in the COM interface.

After using this property, use [IModelDoc2::GraphicsRedraw2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GraphicsRedraw2.md) to redraw the graphics window to see your changes.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)
