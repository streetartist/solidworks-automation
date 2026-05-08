# GridBubble Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GridBubble`

Gets or sets whether to display a grid bubble at the end of ordinate dimension extension lines.
Gets or sets whether to display a grid bubble at the end of ordinate dimension extension lines.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property GridBubble As System.Boolean
```

```

Dim instance As IDisplayDimension
Dim value As System.Boolean
 
instance.GridBubble = value
 
value = instance.GridBubble
```

```

System.bool GridBubble {get; set;}
```

```

property System.bool GridBubble {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to display a grid bubble at the end of ordinate dimension extension lines, false to not

Example

[Display Grid Bubble (VBA)](Display_Grid_Bubble_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)  
[IDisplayDimension::AutoJogOrdinate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~AutoJogOrdinate.md)  
[IDisplayDimension::DisplayAsChain Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~DisplayAsChain.md)  
[IDisplayDimension::Elevation Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~Elevation.md)  
[IDisplayDimension::EndSymbol Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~EndSymbol.md)  
[IDisplayDimension::Jogged Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~Jogged.md)  
[IDisplayDimension::GetOrdinateDimensionArrowSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetOrdinateDimensionArrowSize.md)  
[IDisplayDimension::SetOrdinateDimensionArrowSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetOrdinateDimensionArrowSize.md)
