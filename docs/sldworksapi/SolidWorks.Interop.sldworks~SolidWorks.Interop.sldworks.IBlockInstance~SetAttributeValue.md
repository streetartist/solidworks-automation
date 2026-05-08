# SetAttributeValue Method (IBlockInstance)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockInstance~SetAttributeValue`

Obsolete. Superseded by ISKetchBlockInstance::SetAttributeValue.
Obsolete. Superseded by [ISKetchBlockInstance::SetAttributeValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~SetAttributeValue.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetAttributeValue( _
   ByVal TagName As System.String, _
   ByVal Value As System.String _
) As System.Boolean
```

```

Dim instance As IBlockInstance
Dim TagName As System.String
Dim Value As System.String
Dim value As System.Boolean
 
value = instance.SetAttributeValue(TagName, Value)
```

```

System.bool SetAttributeValue( 
   System.string TagName,
   System.string Value
)
```

```

System.bool SetAttributeValue( 
   System.String^ TagName,
   System.String^ Value
) 
```

#### Parameters

*TagName*

*Value*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBlockInstance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockInstance.md)  
[IBlockInstance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockInstance_members.md)
