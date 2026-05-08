# SetLineFontExtensionStyle Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetLineFontExtensionStyle`

Sets the line font style for the extension lines of this display dimension.
Sets the line font style for the extension lines of this display dimension.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetLineFontExtensionStyle( _
   ByVal UseDoc As System.Boolean, _
   ByVal Style As System.Integer _
) As System.Boolean
```

```

Dim instance As IDisplayDimension
Dim UseDoc As System.Boolean
Dim Style As System.Integer
Dim value As System.Boolean
 
value = instance.SetLineFontExtensionStyle(UseDoc, Style)
```

```

System.bool SetLineFontExtensionStyle( 
   System.bool UseDoc,
   System.int Style
)
```

```

System.bool SetLineFontExtensionStyle( 
   System.bool UseDoc,
   System.int Style
) 
```

#### Parameters

*UseDoc*
:   True uses the document setting for the font style of extension lines, false uses the setting specified  
    in Style

*Style*
:   Extension line font style as defined in [swLineStyles\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineStyles_e.html); valid only if UseDoc = false

#### Return Value

True if the extension line font style is set, false if not

Remarks

After calling this method, call [IModelView::GraphicsRedraw](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GraphicsRedraw.md) to redraw the graphics window to see your changes.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)  
[IDisplayDimension::SetLineFontExtensionThickness Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetLineFontExtensionThickness.md)  
[IDisplayDimension::ExtensionLineExtendsFromCenterOfSet Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ExtensionLineExtendsFromCenterOfSet.md)  
[IDisplayDimension::ExtensionLineSameAsLeaderStyle Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ExtensionLineSameAsLeaderStyle.md)  
[IDisplayDimension::ExtensionLineUseDocumentDisplay Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ExtensionLineUseDocumentDisplay.md)
