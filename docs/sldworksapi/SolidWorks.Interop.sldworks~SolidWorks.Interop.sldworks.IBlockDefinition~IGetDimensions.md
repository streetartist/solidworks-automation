# IGetDimensions Method (IBlockDefinition)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockDefinition~IGetDimensions`

Obsolete. Superseded by ISketchBlockDefinition::GetDisplayDimensions.
Obsolete. Superseded by [ISketchBlockDefinition::GetDisplayDimensions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetDisplayDimensions.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetDimensions( _
   ByVal NumDimensions As System.Integer _
) As DisplayDimension
```

```

Dim instance As IBlockDefinition
Dim NumDimensions As System.Integer
Dim value As DisplayDimension
 
value = instance.IGetDimensions(NumDimensions)
```

```

DisplayDimension IGetDimensions( 
   System.int NumDimensions
)
```

```

DisplayDimension^ IGetDimensions( 
   System.int NumDimensions
) 
```

#### Parameters

*NumDimensions*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockDefinition.md)  
[IBlockDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockDefinition_members.md)
