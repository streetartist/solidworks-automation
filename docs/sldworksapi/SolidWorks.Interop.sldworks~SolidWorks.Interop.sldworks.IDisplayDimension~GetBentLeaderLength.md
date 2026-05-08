# GetBentLeaderLength Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetBentLeaderLength`

Gets the length of the bent leader to use when displaying this dimension.
Gets the length of the bent leader to use when displaying this dimension.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetBentLeaderLength() As System.Double
```

```

Dim instance As IDisplayDimension
Dim value As System.Double
 
value = instance.GetBentLeaderLength()
```

```

System.double GetBentLeaderLength()
```

```

System.double GetBentLeaderLength(); 
```

#### Return Value

Length of the bent leader in system units

Remarks

This method returns the length of the bent leader regardless of how the dimension is currently being displayed.  Even if the dimension is not currently being displayed with a bent leader, this method still returns the length.

If the dimension is using the document default setting for dimension bent leader length, this method returns that value. You can use [IDisplayDimension::GetUseDocBentLeaderLength](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetUseDocBentLeaderLength.md) to determine if this dimension is using the document default setting for dimension  
bent leader length or not.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)  
[IDisplayDimension::SetBentLeaderLength Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetBentLeaderLength.md)  
[IDisplayDimension::GetUseDocBentLeaderLength Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetUseDocBentLeaderLength.md)
