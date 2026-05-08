# GetOverrideValue Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetOverrideValue`

Gets the value to display instead of the actual dimension value.
Gets the value to display instead of the actual dimension value.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetOverrideValue() As System.Double
```

```

Dim instance As IDisplayDimension
Dim value As System.Double
 
value = instance.GetOverrideValue()
```

```

System.double GetOverrideValue()
```

```

System.double GetOverrideValue(); 
```

#### Return Value

Value to display instead of the actual dimension value

Remarks

Use [IDisplayDimension::GetOverride](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetOverride.md) to get whether to display the actual dimension value or to override it with another value.

Use [IDisplayDimension::SetOverride](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetOverride.md) to set whether to override the actual dimension value with another value, and, if so, that value.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)
