# AlignDimensions Method (IModelDocExtension)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AlignDimensions`

Aligns the selected dimensions in drawing documents.
Aligns the selected dimensions in drawing documents.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AlignDimensions( _
   ByVal AlignType As System.Integer, _
   ByVal SpaceValue As System.Double _
) As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim AlignType As System.Integer
Dim SpaceValue As System.Double
Dim value As System.Boolean
 
value = instance.AlignDimensions(AlignType, SpaceValue)
```

```

System.bool AlignDimensions( 
   System.int AlignType,
   System.double SpaceValue
)
```

```

System.bool AlignDimensions( 
   System.int AlignType,
   System.double SpaceValue
) 
```

#### Parameters

*AlignType*
:   Type of alignment as defined by [swAlignDimensionType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAlignDimensionType_e.html)

*SpaceValue*
:   Distance between dimensions

#### Return Value

True if the dimensions are aligned, false if not

Example

[Auto-arrange Dimensions (C#)](Auto-arrange_Dimensions_Example_CSharp.htm)  
[Auto-arrange Dimensions (VB.NET)](Auto-arrange_Dimensions_Example_VBNET.htm)  
[Auto-arrange Dimensions (VBA)](Auto-arrange_Dimensions_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDoc2::AlignParallelDimensions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AlignParallelDimensions.md)  
[IModelDoc2::AlignOrdinate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AlignOrdinate.md)  
[IModelDoc2::BreakDimensionAlignment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~BreakDimensionAlignment.md)
