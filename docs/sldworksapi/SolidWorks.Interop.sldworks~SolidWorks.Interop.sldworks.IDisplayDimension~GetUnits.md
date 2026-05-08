# GetUnits Method (IDisplayDimension)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetUnits`

Gets the units used by this display dimension.
Gets the units used by this display dimension.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetUnits() As System.Integer
```

```

Dim instance As IDisplayDimension
Dim value As System.Integer
 
value = instance.GetUnits()
```

```

System.int GetUnits()
```

```

System.int GetUnits(); 
```

#### Return Value

Units for this display dimension as defined in [swLengthUnit\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLengthUnit_e.html) or [swAngleUnit\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAngleUnit_e.html) (see **Remarks**)

Remarks

A display dimension's units are controlled by a value stored in one of two places:

- document setting.  
  - or -
- local display dimension setting.

Use [IDisplayDimension::GetUseDocUnits](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetUseDocUnits.md) to determine whether the display dimension's settings are from the document setting or local display dimension setting.

|  |  |
| --- | --- |
| **If the display dimension uses...** | **Then IDisplayDimension::GetUnits returns...** |
| Document setting | -1 |
| Local display dimension setting | swLengthUnit\_e or swAngleUnit\_e value |

Use [IDisplayDimension::SetUnits](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetUnits.md) to set the display dimension's unit setting.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)  
[IDisplayDimension::GetChamferUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetChamferUnits.md)
