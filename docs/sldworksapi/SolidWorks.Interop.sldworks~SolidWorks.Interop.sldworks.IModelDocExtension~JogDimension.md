# JogDimension Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~JogDimension`

Gets or sets whether jog points are on or off on an interactively selected linear or ordinate dimension.
Gets or sets whether jog points are on or off on an interactively selected linear or ordinate dimension.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function JogDimension( _
   ByVal Jog As System.Boolean, _
   ByVal WitnessIndex As System.Short _
) As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim Jog As System.Boolean
Dim WitnessIndex As System.Short
Dim value As System.Boolean
 
value = instance.JogDimension(Jog, WitnessIndex)
```

```

System.bool JogDimension( 
   System.bool Jog,
   System.short WitnessIndex
)
```

```

System.bool JogDimension( 
   System.bool Jog,
   System.short WitnessIndex
) 
```

#### Parameters

*Jog*
:   True if jog points are on, false if not

*WitnessIndex*
:   Index, 0 or 1, of linear dimension extension line; ignored if an ordinate dimension

#### Return Value

True if operation succeeds, false if it fails

Remarks

This method is equivalent to clicking the right-mouse button on a linear or ordinate dimension in the SOLIDWORKS user-interface, selecting **Display** **Options** on the shortcut menu, and selecting **Jog**.

Call [IModelView::GraphicsRedraw](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GraphicsRedraw.md) after setting jog points to redraw the graphics area.

Example

[Add and Offset Dimension Extension Lines Jogs (VBA)](Add_and_Offset_Dimension_Extension_Lines_Jogs_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IDisplayDimension::GetJogParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetJogParameters.md)  
[IDisplayDimension::SetJogParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetJogParameters.md)  
[IDisplayDimension::Jogged Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~Jogged.md)  
[IModelDocExtension::AddOrdinateDimension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddOrdinateDimension.md)  
[IDisplayDimension::AutoJogOrdinate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~AutoJogOrdinate.md)
