# GetJogParameters Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetJogParameters`

Gets the jog in a linear dimension extension line.
Gets the jog in a linear dimension extension line.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetJogParameters( _
   ByVal WitnessIndex As System.Short, _
   ByRef Jogged As System.Boolean, _
   ByRef Offset1 As System.Double, _
   ByRef Offset2 As System.Double, _
   ByRef Offset1to2 As System.Double _
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
 
value = instance.GetJogParameters(WitnessIndex, Jogged, Offset1, Offset2, Offset1to2)
```

```

System.bool GetJogParameters( 
   System.short WitnessIndex,
   out System.bool Jogged,
   out System.double Offset1,
   out System.double Offset2,
   out System.double Offset1to2
)
```

```

System.bool GetJogParameters( 
   System.short WitnessIndex,
   [Out] System.bool Jogged,
   [Out] System.double Offset1,
   [Out] System.double Offset2,
   [Out] System.double Offset1to2
) 
```

#### Parameters

*WitnessIndex*
:   Index of linear dimension extension line whose jog to get

*Jogged*
:   True if the linear dimension extension line is jogged, false if not

*Offset1*
:   First line segment of the linear dimension extension line

*Offset2*
:   Second line segment of the linear dimension extension line; this is the line segment that is jogged

*Offset1to2*
:   Third line segment of the linear dimension extension line

#### Return Value

True if the operation succeeds, false if not

Example

[Add and Offset Dimension Extension Lines Jogs (VBA)](Add_and_Offset_Dimension_Extension_Lines_Jogs_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)  
[IDisplayDimension::SetJogParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetJogParameters.md)  
[IModelDocExtension::JogDimension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~JogDimension.md)
