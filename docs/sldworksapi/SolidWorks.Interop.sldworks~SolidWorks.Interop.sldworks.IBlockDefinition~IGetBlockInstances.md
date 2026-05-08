# IGetBlockInstances Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockDefinition~IGetBlockInstances`

Obsolete. Superseded by ISketchBlockDefinition::GetInstances.
Obsolete. Superseded by [ISketchBlockDefinition::GetInstances](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetInstances.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetBlockInstances( _
   ByVal Count As System.Integer _
) As BlockInstance
```

```

Dim instance As IBlockDefinition
Dim Count As System.Integer
Dim value As BlockInstance
 
value = instance.IGetBlockInstances(Count)
```

```

BlockInstance IGetBlockInstances( 
   System.int Count
)
```

```

BlockInstance^ IGetBlockInstances( 
   System.int Count
) 
```

#### Parameters

*Count*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockDefinition.md)  
[IBlockDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockDefinition_members.md)
