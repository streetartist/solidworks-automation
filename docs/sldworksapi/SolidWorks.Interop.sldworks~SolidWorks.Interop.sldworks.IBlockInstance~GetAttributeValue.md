# GetAttributeValue Method (IBlockInstance)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockInstance~GetAttributeValue`

Obsolete. Superseded by ISketchBlockInstance::GetAttributeValue.
Obsolete. Superseded by [ISketchBlockInstance::GetAttributeValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~GetAttributeValue.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetAttributeValue( _
   ByVal TagName As System.String _
) As System.String
```

```

Dim instance As IBlockInstance
Dim TagName As System.String
Dim value As System.String
 
value = instance.GetAttributeValue(TagName)
```

```

System.string GetAttributeValue( 
   System.string TagName
)
```

```

System.String^ GetAttributeValue( 
   System.String^ TagName
) 
```

#### Parameters

*TagName*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBlockInstance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockInstance.md)  
[IBlockInstance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockInstance_members.md)
