# ResetExtensionLineStyle Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ResetExtensionLineStyle`

Resets the style of the specified extension line.
Resets the style of the specified extension line.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ResetExtensionLineStyle( _
   ByVal ExtIndex As System.Short _
) As System.Boolean
```

```

Dim instance As IDisplayDimension
Dim ExtIndex As System.Short
Dim value As System.Boolean
 
value = instance.ResetExtensionLineStyle(ExtIndex)
```

```

System.bool ResetExtensionLineStyle( 
   System.short ExtIndex
)
```

```

System.bool ResetExtensionLineStyle( 
   System.short ExtIndex
) 
```

#### Parameters

*ExtIndex*
:   Index of extension line

#### Return Value

True if successful, false if not

Remarks

Call this method to reset the extension line style if you previously called [IDisplayDimension::SetExtensionLineAsCenterline](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetExtensionLineAsCenterline.md) to set the extension line as a centerline. This method corresponds to the extension line's shortcut menu item **Reset extension line style**, which appears after you select the extension line's shortcut menu item **Set extension line as centerline**.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)  
[IDisplayDimension::ExtensionLineExtendsFromCenterOfSet Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ExtensionLineExtendsFromCenterOfSet.md)  
[IDisplayDimension::ExtensionLineSameAsLeaderStyle Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ExtensionLineSameAsLeaderStyle.md)  
[IDisplayDimension::ExtensionLineUseDocumentDisplay Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ExtensionLineUseDocumentDisplay.md)
