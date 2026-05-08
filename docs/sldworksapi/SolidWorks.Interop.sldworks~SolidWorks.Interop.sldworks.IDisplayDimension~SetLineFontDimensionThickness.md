# SetLineFontDimensionThickness Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetLineFontDimensionThickness`

Sets the thickness of leaders of this display dimension.
Sets the thickness of leaders of this display dimension.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetLineFontDimensionThickness( _
   ByVal UseDoc As System.Boolean, _
   ByVal Style As System.Integer _
) As System.Boolean
```

```

Dim instance As IDisplayDimension
Dim UseDoc As System.Boolean
Dim Style As System.Integer
Dim value As System.Boolean
 
value = instance.SetLineFontDimensionThickness(UseDoc, Style)
```

```

System.bool SetLineFontDimensionThickness( 
   System.bool UseDoc,
   System.int Style
)
```

```

System.bool SetLineFontDimensionThickness( 
   System.bool UseDoc,
   System.int Style
) 
```

#### Parameters

*UseDoc*
:   True uses the document setting for the thickness of leaders, false uses the setting specified  
    in Style

*Style*
:   Leader thickness as defined in [swLineWeights\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineWeights_e.html); valid only if UseDoc = false

#### Return Value

True if the leader thickness is set, false if not

Remarks

After calling this method, call [IModelView::GraphicsRedraw](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GraphicsRedraw.md) to redraw the graphics window to see your changes.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)  
[IDisplayDimension::SetLineFontDimensionStyle Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetLineFontDimensionStyle.md)
