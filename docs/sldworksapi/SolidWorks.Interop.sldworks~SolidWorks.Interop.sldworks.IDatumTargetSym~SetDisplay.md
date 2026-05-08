# SetDisplay Method (IDatumTargetSym)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~SetDisplay`

Sets the display characteristics of the datum target symbol.
Sets the display characteristics of the datum target symbol.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetDisplay( _
   ByVal Symbol As System.Boolean, _
   ByVal TargetArea As System.Boolean, _
   ByVal SizeOutside As System.Boolean _
) As System.Boolean
```

```

Dim instance As IDatumTargetSym
Dim Symbol As System.Boolean
Dim TargetArea As System.Boolean
Dim SizeOutside As System.Boolean
Dim value As System.Boolean
 
value = instance.SetDisplay(Symbol, TargetArea, SizeOutside)
```

```

System.bool SetDisplay( 
   System.bool Symbol,
   System.bool TargetArea,
   System.bool SizeOutside
)
```

```

System.bool SetDisplay( 
   System.bool Symbol,
   System.bool TargetArea,
   System.bool SizeOutside
) 
```

#### Parameters

*Symbol*
:   True displays the datum target symbol part of the annotation, false hides it

*TargetArea*
:   True displays the datum target area part of the annotation, false hides it

*SizeOutside*
:   True displays the datum target area size outside of the symbol, false displays it  
    inside

#### Return Value

True if the display characteristics were set successfully, false if not

Remarks

Use:

- [IDatumTargetSym::GetDisplaySymbol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetDisplaySymbol.md) to determine if the datum target symbol part of the annotation is displayed.
- [IDatumTargetSym::GetDisplayTargetArea](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetDisplayTargetArea.md) to determine if the datum target area part of the annotation is displayed.
- [IDatumTargetSym::GetDisplaySizeOutside](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetDisplaySizeOutside.md) to determine whether the target area size is displayed inside or outside of the symbol.

To see the model or drawing changes caused by running this method, use [IModelDoc2::GraphicsRedraw2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GraphicsRedraw2.md) to redraw your window.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDatumTargetSym Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym.md)  
[IDatumTargetSym Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym_members.md)
