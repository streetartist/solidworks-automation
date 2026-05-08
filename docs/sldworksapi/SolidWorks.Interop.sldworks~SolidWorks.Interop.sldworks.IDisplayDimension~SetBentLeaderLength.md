# SetBentLeaderLength Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetBentLeaderLength`

Sets the bent leader length to use for this dimension.
Sets the bent leader length to use for this dimension.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetBentLeaderLength( _
   ByVal UseDoc As System.Boolean, _
   ByVal Length As System.Double _
) As System.Boolean
```

```

Dim instance As IDisplayDimension
Dim UseDoc As System.Boolean
Dim Length As System.Double
Dim value As System.Boolean
 
value = instance.SetBentLeaderLength(UseDoc, Length)
```

```

System.bool SetBentLeaderLength( 
   System.bool UseDoc,
   System.double Length
)
```

```

System.bool SetBentLeaderLength( 
   System.bool UseDoc,
   System.double Length
) 
```

#### Parameters

*UseDoc*
:   True to use the document default setting for dimension bent leader, false to use the length argument for the bent leader length

*Length*
:   Length of the bent leader in system units

#### Return Value

True if the bent leader length is set, false if not

Remarks

The dimension bent leader length only applies to these types of dimensions: radial and linear. If this method is used on any other type of dimension, no action is taken, and the return value is false.

Use:

- [IDisplayDimension::GetUseDocBentLeaderLength](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetUseDocBentLeaderLength.md) to determine whether this dimension is using the document default setting for dimension bent leader length or not.
- [IDisplayDimension::GetBentLeaderLength](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetBentLeaderLength.md) to determine the bent leader length for this dimension.

After using this method, use [IModelDoc2::GraphicsRedraw2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GraphicsRedraw2.md) to redraw the graphics window to see your changes.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)
