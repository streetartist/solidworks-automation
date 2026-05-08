# IGetAttributes Method (IBlockInstance)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockInstance~IGetAttributes`

Obsolete. Superseded by ISketchBlockInstance::IGetAttributes.
Obsolete. Superseded by [ISketchBlockInstance::IGetAttributes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~IGetAttributes.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetAttributes( _
   ByVal NumAttribs As System.Integer _
) As Note
```

```

Dim instance As IBlockInstance
Dim NumAttribs As System.Integer
Dim value As Note
 
value = instance.IGetAttributes(NumAttribs)
```

```

Note IGetAttributes( 
   System.int NumAttribs
)
```

```

Note^ IGetAttributes( 
   System.int NumAttribs
) 
```

#### Parameters

*NumAttribs*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBlockInstance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockInstance.md)  
[IBlockInstance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockInstance_members.md)
