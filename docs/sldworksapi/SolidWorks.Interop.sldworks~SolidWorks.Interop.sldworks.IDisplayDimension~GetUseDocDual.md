# GetUseDocDual Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetUseDocDual`

Gets whether this display dimension uses the document setting for positioning dual dimensions.
Gets whether this display dimension uses the document setting for positioning dual dimensions.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetUseDocDual() As System.Boolean
```

```

Dim instance As IDisplayDimension
Dim value As System.Boolean
 
value = instance.GetUseDocDual()
```

```

System.bool GetUseDocDual()
```

```

System.bool GetUseDocDual(); 
```

#### Return Value

True if this display dimension uses its dual dimension's top, bottom, right, or left document setting, false if the display dimension uses a setting opposite of the dual dimension's top, bottom, right, or left document setting

Remarks

Use [IDisplayDimension::SetDual](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetDual.md) to set the dual dimension's top, bottom, right, or left setting for this display dimension.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)  
[IDisplayDimension::Split Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~Split.md)
