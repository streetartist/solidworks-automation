# ChamferPrecision Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ChamferPrecision`

Gets or sets the precision of the length and angle values in a chamfer display dimension.
Gets or sets the precision of the length and angle values in a chamfer display dimension.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ChamferPrecision( _
   ByVal Index As System.Integer _
) As System.Integer
```

```

Dim instance As IDisplayDimension
Dim Index As System.Integer
Dim value As System.Integer
 
instance.ChamferPrecision(Index) = value
 
value = instance.ChamferPrecision(Index)
```

```

System.int ChamferPrecision( 
   System.int Index
) {get; set;}
```

```

property System.int ChamferPrecision {
   System.int get(System.int Index);
   void set (System.int Index, System.int value);
}
```

#### Parameters

*Index*
:   0 for length, 1 for angle

#### Property Value

Number of decimal places to display for the value at the specified index

Example

[Get Chamfer Display Dimension (C#)](Get_Chamfer_Display_Dimension_Example_CSharp.htm)  
[Get Chamfer Display Dimension (VB.NET)](Get_Chamfer_Display_Dimension_Example_VBNET.htm)  
[Get Chamfer Display Dimension (VBA)](Get_Chamfer_Display_Dimension_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)  
[IDisplayDimension::GetChamferUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetChamferUnits.md)
