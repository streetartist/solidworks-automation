# AddOrdinateDimension Method (IModelDocExtension)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddOrdinateDimension`

Inserts an ordinate dimension.
Inserts an ordinate dimension.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddOrdinateDimension( _
   ByVal DimType As System.Integer, _
   ByVal LocX As System.Double, _
   ByVal LocY As System.Double, _
   ByVal LocZ As System.Double _
) As System.Integer
```

```

Dim instance As IModelDocExtension
Dim DimType As System.Integer
Dim LocX As System.Double
Dim LocY As System.Double
Dim LocZ As System.Double
Dim value As System.Integer
 
value = instance.AddOrdinateDimension(DimType, LocX, LocY, LocZ)
```

```

System.int AddOrdinateDimension( 
   System.int DimType,
   System.double LocX,
   System.double LocY,
   System.double LocZ
)
```

```

System.int AddOrdinateDimension( 
   System.int DimType,
   System.double LocX,
   System.double LocY,
   System.double LocZ
) 
```

#### Parameters

*DimType*
:   Dimension type as defined in [swAddOrdinateDims\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAddOrdinateDims_e.html)

*LocX*
:   X location for the dimension

*LocY*
:   Y location for the dimension

*LocZ*
:   Z location for the dimension

#### Return Value

Error as defined by [swCreateOrdDimError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCreateOrdDimError_e.html)

Remarks

Before using this method, select the base entity to act as the datum point for the ordinate dimension and any additional entities to include in the group of ordinate dimensions.

Selections made immediately after calling this method continue to add ordinate dimensions to the group of ordinate dimensions. When you finish adding ordinate dimensions to the group, use [IModelDoc2::SetPickMode](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetPickMode.md) to return to the default selection mode.

Use [IModelDoc2::EditOrdinate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditOrdinate.md) to add ordinate dimensions to an existing group of ordinate dimensions.

Example

[Display Grid Bubble (VBA)](Display_Grid_Bubble_Example_VB.htm)  
[Create Ordinate Dimensions (C#)](Create_Ordinate_Dimensions_Example_CSharp.htm)  
[Create Ordinate Dimensions (VB.NET)](Create_Ordinate_Dimensions_Example_VBNET.htm)  
[Create Ordinate Dimensions (VBA)](Create_Ordinate_Dimensions_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IModelDocExtension::JogDimension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~JogDimension.md)  
[IModelDoc2::AlignOrdinate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AlignOrdinate.md)  
[IModelDoc2::ReattachOrdinate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ReattachOrdinate.md)  
[IDrawingDoc::AlignOrdinate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AlignOrdinate.md)  
[IDrawingDoc::CreateOrdinateDim4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateOrdinateDim4.md)  
[IDrawingDoc::EditOrdinate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~EditOrdinate.md)  
[IDrawingDoc::InsertHorizontalOrdinate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertHorizontalOrdinate.md)  
[IDrawingDoc::InsertVerticalOrdinate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertVerticalOrdinate.md)
