# AlignToEdge Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~AlignToEdge`

Aligns this linear dimension with the specified edge.
Aligns this linear dimension with the specified edge.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AlignToEdge( _
   ByVal AlignmentEdge As System.Object _
) As System.Boolean
```

```

Dim instance As IDisplayDimension
Dim AlignmentEdge As System.Object
Dim value As System.Boolean
 
value = instance.AlignToEdge(AlignmentEdge)
```

```

System.bool AlignToEdge( 
   System.object AlignmentEdge
)
```

```

System.bool AlignToEdge( 
   System.Object^ AlignmentEdge
) 
```

#### Parameters

*AlignmentEdge*
:   [IEdge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)

#### Return Value

True if successful, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)  
[IDisplayDimension::SetHorizontal Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetHorizontal.md)  
[IDisplayDimension::SetVertical Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetVertical.md)
