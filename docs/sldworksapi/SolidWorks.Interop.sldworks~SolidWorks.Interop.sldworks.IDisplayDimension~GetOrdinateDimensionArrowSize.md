# GetOrdinateDimensionArrowSize Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetOrdinateDimensionArrowSize`

Gets the diameter of the circle for the arrow of the base ordinate dimension.
Gets the diameter of the circle for the arrow of the base ordinate dimension.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub GetOrdinateDimensionArrowSize( _
   ByRef UseDoc As System.Boolean, _
   ByRef ArrowSize As System.Double _
) 
```

```

Dim instance As IDisplayDimension
Dim UseDoc As System.Boolean
Dim ArrowSize As System.Double
 
instance.GetOrdinateDimensionArrowSize(UseDoc, ArrowSize)
```

```

void GetOrdinateDimensionArrowSize( 
   out System.bool UseDoc,
   out System.double ArrowSize
)
```

```

void GetOrdinateDimensionArrowSize( 
   [Out] System.bool UseDoc,
   [Out] System.double ArrowSize
) 
```

#### Parameters

*UseDoc*
:   True to use the document setting for the diameter of the circle for the arrow of the base ordinate dimension, false to use the diameter of the circle for the arrow of the base ordinate dimension set by [IDisplayDimension::SetOrdinateDimensionArrowSize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetOrdinateDimensionArrowSize.md) if the base ordinate dimension standard is set to DIN

*ArrowSize*
:   Diameter of the circle for the arrow of the base ordinate dimension

Example

[Create Ordinate Dimensions (C#)](Create_Ordinate_Dimensions_Example_CSharp.htm)  
[Create Ordinate Dimensions (VB.NET)](Create_Ordinate_Dimensions_Example_VBNET.htm)  
[Create Ordinate Dimensions (VBA)](Create_Ordinate_Dimensions_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)  
[IDisplayDimension::AutoJogOrdinate Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~AutoJogOrdinate.md)  
[IDisplayDimension::DisplayAsChain Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~DisplayAsChain.md)  
[IDisplayDimension::Elevation Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~Elevation.md)  
[IDisplayDimension::Jogged Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~Jogged.md)  
[IDisplayDimension::EndSymbol Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~EndSymbol.md)  
[IDisplayDimension::GridBubble Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GridBubble.md)  
[IModelDocExtension::AddOrdinateDimension Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddOrdinateDimension.md)  
[IDrawingDoc::InsertOrdinate Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertOrdinate.md)  
[IDrawingDoc::InsertHorizontalOrdinate Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertHorizontalOrdinate.md)  
[IDrawingDoc::InsertVerticalOrdinate Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertVerticalOrdinate.md)  
[IDrawingDoc::CreateOrdinateDim4 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateOrdinateDim4.md)
