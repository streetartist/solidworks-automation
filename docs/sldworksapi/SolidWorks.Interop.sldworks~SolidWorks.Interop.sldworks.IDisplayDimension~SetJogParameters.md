# SetJogParameters Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetJogParameters`

Set the linear dimension extension line to be jogged.
Set the linear dimension extension line to be jogged.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetJogParameters( _
   ByVal WitnessIndex As System.Short, _
   ByVal Jogged As System.Boolean, _
   ByVal Offset1 As System.Double, _
   ByVal Offset2 As System.Double, _
   ByVal Offset1to2 As System.Double _
) As System.Boolean
```

```

Dim instance As IDisplayDimension
Dim WitnessIndex As System.Short
Dim Jogged As System.Boolean
Dim Offset1 As System.Double
Dim Offset2 As System.Double
Dim Offset1to2 As System.Double
Dim value As System.Boolean
 
value = instance.SetJogParameters(WitnessIndex, Jogged, Offset1, Offset2, Offset1to2)
```

```

System.bool SetJogParameters( 
   System.short WitnessIndex,
   System.bool Jogged,
   System.double Offset1,
   System.double Offset2,
   System.double Offset1to2
)
```

```

System.bool SetJogParameters( 
   System.short WitnessIndex,
   System.bool Jogged,
   System.double Offset1,
   System.double Offset2,
   System.double Offset1to2
) 
```

#### Parameters

*WitnessIndex*
:   Index of the linear dimension extension line to jog

*Jogged*
:   True whether the linear dimension extension is jogged, false if not

*Offset1*
:   First line segment of the linear dimension extension line

*Offset2*
:   Second line segment of the linear dimension extension line; this is the line segment to jog

*Offset1to2*
:   Distance by which to offset Offset1 and Offset2 for the jog

Remarks

Call [IModelView::GraphicsRedraw](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GraphicsRedraw.md) after calling this method to redraw the graphics area.

Example

[Add and Offset Dimension Lines Jogs (VBA)](Add_and_Offset_Dimension_Extension_Lines_Jogs_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)  
[IModelDocExtension::JogDimension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~JogDimension.md)  
[IDisplayDimension::GetJogParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetJogParameters.md)
