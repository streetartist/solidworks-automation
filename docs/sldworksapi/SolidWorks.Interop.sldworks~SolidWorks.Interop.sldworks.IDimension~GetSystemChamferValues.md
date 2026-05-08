# GetSystemChamferValues Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetSystemChamferValues`

Gets the chamfer dimension values in system units.
Gets the chamfer dimension values in system units.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSystemChamferValues( _
   ByRef Length As System.Double, _
   ByRef Angle As System.Double _
) As System.Boolean
```

```

Dim instance As IDimension
Dim Length As System.Double
Dim Angle As System.Double
Dim value As System.Boolean
 
value = instance.GetSystemChamferValues(Length, Angle)
```

```

System.bool GetSystemChamferValues( 
   out System.double Length,
   out System.double Angle
)
```

```

System.bool GetSystemChamferValues( 
   [Out] System.double Length,
   [Out] System.double Angle
) 
```

#### Parameters

*Length*
:   Length of chamfer

*Angle*
:   Angle of chamfer

#### Return Value

True if the dimension is a chamfer dimension, false if not

Remarks

Unlike most other types of dimensions, the values returned for a chamfer dimension are not necessarily the values seen by the user in the displayed dimension text. The display dimension interprets these values and considers the type of chamfer display requested by the user and then creates an appropriate output string.

Example

[Get Chamfer Dimension (C#)](Get_Chamfer_Dimension_Example_CSharp.htm)  
[Get Chamfer Dimension (VB.NET)](Get_Chamfer_Dimension_Example_VBNET.htm)  
[Get Chamfer Dimension (VBA)](Get_Chamfer_Dimension_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.md)  
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.md)  
[IDrawingDoc::AddChamferDim Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AddChamferDim.md)  
[IDrawingDoc::IAddChamferDim Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IAddChamferDim.md)
