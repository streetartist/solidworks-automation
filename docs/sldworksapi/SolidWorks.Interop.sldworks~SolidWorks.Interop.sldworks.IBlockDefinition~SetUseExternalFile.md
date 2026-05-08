# SetUseExternalFile Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockDefinition~SetUseExternalFile`

Obsolete. Superseded by ISketchBlockDefinition::LinkToFile.
Obsolete. Superseded by [ISketchBlockDefinition::LinkToFile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~LinkToFile.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetUseExternalFile( _
   ByVal UseFile As System.Boolean _
) As System.Integer
```

```

Dim instance As IBlockDefinition
Dim UseFile As System.Boolean
Dim value As System.Integer
 
value = instance.SetUseExternalFile(UseFile)
```

```

System.int SetUseExternalFile( 
   System.bool UseFile
)
```

```

System.int SetUseExternalFile( 
   System.bool UseFile
) 
```

#### Parameters

*UseFile*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockDefinition.md)  
[IBlockDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockDefinition_members.md)
