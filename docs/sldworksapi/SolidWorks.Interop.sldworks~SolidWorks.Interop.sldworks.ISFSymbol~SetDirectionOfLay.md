# SetDirectionOfLay Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~SetDirectionOfLay`

Sets the direction of lay value for this surface finish symbol.
Sets the direction of lay value for this surface finish symbol.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetDirectionOfLay( _
   ByVal Direction As System.Integer _
) As System.Boolean
```

```

Dim instance As ISFSymbol
Dim Direction As System.Integer
Dim value As System.Boolean
 
value = instance.SetDirectionOfLay(Direction)
```

```

System.bool SetDirectionOfLay( 
   System.int Direction
)
```

```

System.bool SetDirectionOfLay( 
   System.int Direction
) 
```

#### Parameters

*Direction*
:   Direction of lay value as defined in [swSFLaySym\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSFLaySym_e.html)

#### Return Value

True if the direction of lay value is set, false if not

Remarks

If an invalid direction of lay value is specified, the symbol is not changed, and false is returned.

To see the model or drawing changes caused by running this method, you must redraw your window. See [IModelDoc2::GraphicsRedraw2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GraphicsRedraw2.md) for details.

To get the direction of lay value, use [ISFSymbol::GetDirectionOfLay](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetDirectionOfLay.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISFSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol.md)  
[ISFSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol_members.md)
