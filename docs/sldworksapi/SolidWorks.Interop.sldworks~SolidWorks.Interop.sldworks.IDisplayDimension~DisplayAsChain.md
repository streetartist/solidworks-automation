# DisplayAsChain Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~DisplayAsChain`

Gets or sets whether the extension lines of every dimension in this set of angular running or ordinate dimensions are chained together.
Gets or sets whether the extension lines of every dimension in this set of angular running or ordinate dimensions are chained together.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DisplayAsChain As System.Boolean
```

```

Dim instance As IDisplayDimension
Dim value As System.Boolean
 
instance.DisplayAsChain = value
 
value = instance.DisplayAsChain
```

```

System.bool DisplayAsChain {get; set;}
```

```

property System.bool DisplayAsChain {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if extension lines are chained together, false if not

Remarks

This property applies only to ordinate and angular running dimensions. This method does not affect other types of dimensions.

This property corresponds to:

- **Display as chain dimension** check box in the **Witness/Leader Display** panel of the **Leaders** tab of the **Dimension** PropertyManager page that appears when you right-click in a drawing and select **More Dimensions > Angular Running Dimension**.
- **Ordinate chain** check box in the **Witness/Leader Display** panel of the **Leaders** tab of the **Dimension** PropertyManager page that appears when you right-click in a drawing and select **More Dimensions > Ordinate**.

After using this property, use [IModelView::GraphicsRedraw](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GraphicsRedraw.md) to redraw the graphics window to see your changes.

Example

[Insert Angular Running Dimension (VBA)](Set_Properties_of_Angular_Running_Dimension_Example_VB.htm)  
[Insert Angular Running Dimension (VB.NET)](Set_Properties_of_Angular_Running_Dimension_Example_VBNET.htm)  
[Insert Angular Running Dimension (C#)](Set_Properties_of_Angular_Running_Dimension_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)  
[IDisplayDimension::AutoJogOrdinate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~AutoJogOrdinate.md)  
[IDisplayDimension::Elevation Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~Elevation.md)  
[IDisplayDimension::EndSymbol Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~EndSymbol.md)  
[IDisplayDimension::GridBubble Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GridBubble.md)  
[IDisplayDimension::Jogged Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~Jogged.md)  
[IDisplayDimension::ExtensionLineExtendsFromCenterOfSet Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ExtensionLineExtendsFromCenterOfSet.md)  
[IDisplayDimension::RunBidirectionally Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~RunBidirectionally.md)  
[IDisplayDimension::ExtensionLineSameAsLeaderStyle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ExtensionLineSameAsLeaderStyle.md)  
[IDisplayDimension::ExtensionLineUseDocumentDisplay Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ExtensionLineUseDocumentDisplay.md)  
[IDisplayDimension::ResetExtensionLineStyle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ResetExtensionLineStyle.md)  
[IModelDocExtension::AddOrdinateDimension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddOrdinateDimension.md)  
[IDisplayDimension::SetOrdinateDimensionArrowSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetOrdinateDimensionArrowSize.md)  
[IDisplayDimension::GetOrdinateDimensionArrowSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetOrdinateDimensionArrowSize.md)
