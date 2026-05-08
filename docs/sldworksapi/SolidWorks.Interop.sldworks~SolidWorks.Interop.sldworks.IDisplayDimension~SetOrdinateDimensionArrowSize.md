# SetOrdinateDimensionArrowSize Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetOrdinateDimensionArrowSize`

Sets the diameter of the circle for the arrow of the base ordinate dimension if the base ordinate dimension standard is set to DIN.
Sets the diameter of the circle for the arrow of the base ordinate dimension if the base ordinate dimension standard is set to DIN.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetOrdinateDimensionArrowSize( _
   ByVal UseDoc As System.Boolean, _
   ByVal ArrowSize As System.Double _
) 
```

```

Dim instance As IDisplayDimension
Dim UseDoc As System.Boolean
Dim ArrowSize As System.Double
 
instance.SetOrdinateDimensionArrowSize(UseDoc, ArrowSize)
```

```

void SetOrdinateDimensionArrowSize( 
   System.bool UseDoc,
   System.double ArrowSize
)
```

```

void SetOrdinateDimensionArrowSize( 
   System.bool UseDoc,
   System.double ArrowSize
) 
```

#### Parameters

*UseDoc*
:   True to use the document setting for the diameter of the circle for the arrow of the base ordinate dimension, false to use the diameter of the circle for the arrow of the base ordinate dimension set by this method if the base ordinate dimension standard is set to DIN

*ArrowSize*
:   Diameter of the circle for the arrow of the base ordinate dimension if the base ordinate dimension standard is set to DIN

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
[IDisplayDimension::GetOrdinateDimensionArrowSize Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetOrdinateDimensionArrowSize.md)  
[IDisplayDimension::AutoJogOrdinate Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~AutoJogOrdinate.md)  
[IDisplayDimension::DisplayAsChain Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~DisplayAsChain.md)  
[IDisplayDimension::Elevation Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~Elevation.md)  
[IDisplayDimension::EndSymbol Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~EndSymbol.md)  
[IDisplayDimension::GridBubble Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GridBubble.md)  
[IDisplayDimension::Jogged Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~Jogged.md)  
[IModelDocExtension::AddOrdinateDimension Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddOrdinateDimension.md)  
[IDrawingDoc::CreateOrdinateDim4 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateOrdinateDim4.md)  
[IDrawingDoc::InsertOrdinate Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertOrdinate.md)  
[IDrawingDoc::InsertHorizontalOrdinate Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertHorizontalOrdinate.md)  
[IDrawingDoc::InsertVerticalOrdinate Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertVerticalOrdinate.md)
