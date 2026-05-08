# GetOverride Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetOverride`

Gets whether to display the actual dimension value or to override it with another value.
Gets whether to display the actual dimension value or to override it with another value.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetOverride() As System.Boolean
```

```

Dim instance As IDisplayDimension
Dim value As System.Boolean
 
value = instance.GetOverride()
```

```

System.bool GetOverride()
```

```

System.bool GetOverride(); 
```

#### Return Value

True to display the override value, false to display the actual dimension value

Remarks

Use [IDisplayDimension::GetOverrideValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetOverrideValue.md) to get the override value.

Use [IDisplayDimension::SetOverride](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetOverride.md) to set whether to override the actual dimension value with another value and, if so, that value.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)
