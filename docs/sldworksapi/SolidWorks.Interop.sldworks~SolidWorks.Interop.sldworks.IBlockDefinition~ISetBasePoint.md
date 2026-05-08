# ISetBasePoint Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockDefinition~ISetBasePoint`

Obsolete. Superseded by ISketchBlockDefinition::InsertionPoint.
Obsolete. Superseded by [ISketchBlockDefinition::InsertionPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~InsertionPoint.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ISetBasePoint( _
   ByRef BasePoint As System.Double _
) As System.Boolean
```

```

Dim instance As IBlockDefinition
Dim BasePoint As System.Double
Dim value As System.Boolean
 
value = instance.ISetBasePoint(BasePoint)
```

```

System.bool ISetBasePoint( 
   ref System.double BasePoint
)
```

```

System.bool ISetBasePoint( 
   System.double% BasePoint
) 
```

#### Parameters

*BasePoint*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockDefinition.md)  
[IBlockDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockDefinition_members.md)
