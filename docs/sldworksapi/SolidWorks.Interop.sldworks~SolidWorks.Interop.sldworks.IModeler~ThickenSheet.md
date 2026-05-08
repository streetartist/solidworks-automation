# ThickenSheet Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ThickenSheet`

Thickens a sheet body.
Thickens a sheet body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ThickenSheet( _
   ByVal Sheet As Body2, _
   ByVal Thickness As System.Double, _
   ByVal Direction As System.Integer _
) As Body2
```

```

Dim instance As IModeler
Dim Sheet As Body2
Dim Thickness As System.Double
Dim Direction As System.Integer
Dim value As Body2
 
value = instance.ThickenSheet(Sheet, Thickness, Direction)
```

```

Body2 ThickenSheet( 
   Body2 Sheet,
   System.double Thickness,
   System.int Direction
)
```

```

Body2^ ThickenSheet( 
   Body2^ Sheet,
   System.double Thickness,
   System.int Direction
) 
```

#### Parameters

*Sheet*
:   Sheet body that defines the profile for the temporary thickened [body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

*Thickness*
:   Thickness of the temporary thickened body

*Direction*
:   Direction in which to thicken the sheet body as defined in [swThickenDirection\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swThickenDirection_e.html)

#### Return Value

Temporary thickened [body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

Remarks

If you set Direction to swThickenDirection\_Both, then the value set for Thickness is used in both directions.

Example

[Thicken Sheet Body (VBA)](Thicken_Sheet_Body_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)
