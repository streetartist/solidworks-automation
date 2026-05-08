# GetUseDocBrokenLeader Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetUseDocBrokenLeader`

Gets whether this display dimension uses the document default setting for displaying leaders as broken.
Gets whether this display dimension uses the document default setting for displaying leaders as broken.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetUseDocBrokenLeader() As System.Boolean
```

```

Dim instance As IDisplayDimension
Dim value As System.Boolean
 
value = instance.GetUseDocBrokenLeader()
```

```

System.bool GetUseDocBrokenLeader()
```

```

System.bool GetUseDocBrokenLeader(); 
```

#### Return Value

True if this display dimension uses the document setting, false if it uses a specific setting

Remarks

SOLIDWORKS can display dimension text above a solid, unbroken leader line, or the dimension leader line can be broken with the text displayed either horizontal or aligned with the leader line. This method allows you to determine if this [IDisplayDimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md) is using the document default setting for this value or if the user has applied a  
specific setting to this specific IDisplayDimension.

Use [IDisplayDimension::SetBrokenLeader2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetBrokenLeader2.md) to set this value.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)  
[IDisplayDimension::GetBrokenLeader2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetBrokenLeader2.md)  
[IDisplayDimension::SolidLeader Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SolidLeader.md)
