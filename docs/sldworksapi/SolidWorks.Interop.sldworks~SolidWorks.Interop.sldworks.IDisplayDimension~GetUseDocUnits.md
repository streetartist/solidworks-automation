# GetUseDocUnits Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetUseDocUnits`

Gets whether this display dimension uses the document default setting for units.
Gets whether this display dimension uses the document default setting for units.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetUseDocUnits() As System.Boolean
```

```

Dim instance As IDisplayDimension
Dim value As System.Boolean
 
value = instance.GetUseDocUnits()
```

```

System.bool GetUseDocUnits()
```

```

System.bool GetUseDocUnits(); 
```

#### Return Value

True if this display dimension uses the document setting, false if it uses the local display dimension setting

Remarks

The unit display settings of a display dimension are controlled by a value stored in one of two places: on the owning document or on the individual display dimension. This method determines whether this display dimension uses the default document setting for units.

Use [IDisplayDimension::SetUnits](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetUnits.md) to set this value.

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
[IDisplayDimension::GetUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetUnits.md)
