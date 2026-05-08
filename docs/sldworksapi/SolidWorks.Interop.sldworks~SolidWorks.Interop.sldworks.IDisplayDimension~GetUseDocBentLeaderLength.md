# GetUseDocBentLeaderLength Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetUseDocBentLeaderLength`

Gets whether this dimension is using the document default for bent leader length or not.
Gets whether this dimension is using the document default for bent leader length or not.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetUseDocBentLeaderLength() As System.Boolean
```

```

Dim instance As IDisplayDimension
Dim value As System.Boolean
 
value = instance.GetUseDocBentLeaderLength()
```

```

System.bool GetUseDocBentLeaderLength()
```

```

System.bool GetUseDocBentLeaderLength(); 
```

#### Return Value

True if using the document default setting for dimension bent leader length, false if not

Remarks

This method returns whether the document default setting is being used or not, regardless of how the dimension is currently being displayed.  Even if the dimension is not currently being displayed with a bent leader, this method returns the value.

Use [IDisplayDimension::GetBentLeaderLength](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetBentLeaderLength.md) to determine the bent leader length for this dimension.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)  
[IDisplayDimension::SetBentLeaderLength Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetBentLeaderLength.md)
