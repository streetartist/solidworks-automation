# ExtensionLineUseDocumentDisplay Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ExtensionLineUseDocumentDisplay`

Gets or sets whether to use the document settings for extension lines.
Gets or sets whether to use the document settings for extension lines.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ExtensionLineUseDocumentDisplay As System.Boolean
```

```

Dim instance As IDisplayDimension
Dim value As System.Boolean
 
instance.ExtensionLineUseDocumentDisplay = value
 
value = instance.ExtensionLineUseDocumentDisplay
```

```

System.bool ExtensionLineUseDocumentDisplay {get; set;}
```

```

property System.bool ExtensionLineUseDocumentDisplay {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to use the document settings for extension lines, false to not

Remarks

This property is valid only if [IDisplayDimension::ExtensionLineSameAsLeaderStyle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ExtensionLineSameAsLeaderStyle.md) is set to false.

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
[IDisplayDimension::ExtensionLineExtendsFromCenterOfSet Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ExtensionLineExtendsFromCenterOfSet.md)  
[IDisplayDimension::ResetExtensionLineStyle Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ResetExtensionLineStyle.md)  
[IDisplayDimension::DisplayAsChain Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~DisplayAsChain.md)  
[IDisplayDimension::RunBidirectionally Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~RunBidirectionally.md)  
[IDisplayDimension::Jogged Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~Jogged.md)  
[IDisplayDimension::SetLineFontExtensionStyle Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetLineFontExtensionStyle.md)  
[IDisplayDimension::SetLineFontExtensionThickness Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetLineFontExtensionThickness.md)
