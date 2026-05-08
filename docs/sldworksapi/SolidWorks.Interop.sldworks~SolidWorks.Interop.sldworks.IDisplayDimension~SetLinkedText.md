# SetLinkedText Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetLinkedText`

Sets the text to link to this display dimension.
Sets the text to link to this display dimension.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetLinkedText( _
   ByVal BstrLinkedText As System.String _
) As System.Integer
```

```

Dim instance As IDisplayDimension
Dim BstrLinkedText As System.String
Dim value As System.Integer
 
value = instance.SetLinkedText(BstrLinkedText)
```

```

System.int SetLinkedText( 
   System.string BstrLinkedText
)
```

```

System.int SetLinkedText( 
   System.String^ BstrLinkedText
) 
```

#### Parameters

*BstrLinkedText*
:   Text to link to this display dimension

#### Return Value

Error code as defined in [swLinkDimensionError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLinkDimensionError_e.html)

Remarks

- Dimension types must be the same, for example: linear to linea , angular to angular, and so on.
- Angular dimensions must be in the same quadrant.
- Dimensions cannot shared by another named group.
- Dimensions with dissimilar ranges cannot be shared.
- Dimensions cannot driven by equations, read-only, driven sketch dimensions, or reference dimensions.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)  
[IDisplayDimension::GetLinkedText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetLinkedText.md)  
[IDisplayDimension::Unlink Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~Unlink.md)  
[IDisplayDimension::IsLinked Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~IsLinked.md)
