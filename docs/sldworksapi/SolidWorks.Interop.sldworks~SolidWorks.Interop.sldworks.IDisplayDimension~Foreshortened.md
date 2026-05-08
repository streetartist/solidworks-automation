# Foreshortened Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~Foreshortened`

Gets or sets whether a linear dimension is foreshortened in a drawing.
Gets or sets whether a linear dimension is foreshortened in a drawing.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Foreshortened As System.Boolean
```

```

Dim instance As IDisplayDimension
Dim value As System.Boolean
 
instance.Foreshortened = value
 
value = instance.Foreshortened
```

```

System.bool Foreshortened {get; set;}
```

```

property System.bool Foreshortened {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if the linear dimension is foreshortened, false if not

Remarks

This property is only valid for linear dimensions and only when the detailing standard is ANSI.

Example

[Get Whether Linear Dimension Is Foreshortened (C#)](Get_Whether_Linear_Dimension_Is_Foreshortened_Example_CSharp.htm)  
[Get Whether Linear Dimension Is Foreshortened (VB.NET)](Get_Whether_Linear_Dimension_Is_Foreshortened_Example_VBNET.htm)  
[Get Whether Linear Dimension Is Foreshortened (VBA)](Get_Whether_Linear_Dimension_Is_Foreshortened_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)  
[IDisplayDimension::DisplayAsLinear Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~DisplayAsLinear.md)  
[IModelDoc2::AddDimension2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddDimension2.md)
