# Set Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Set`

Obsolete. Superseded by ICustomPropertyManager::Set2.
Obsolete. Superseded by [ICustomPropertyManager::Set2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Set2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Set( _
   ByVal FieldName As System.String, _
   ByVal FieldValue As System.String _
) As System.Integer
```

```

Dim instance As ICustomPropertyManager
Dim FieldName As System.String
Dim FieldValue As System.String
Dim value As System.Integer
 
value = instance.Set(FieldName, FieldValue)
```

```

System.int Set( 
   System.string FieldName,
   System.string FieldValue
)
```

```

System.int Set( 
   System.String^ FieldName,
   System.String^ FieldValue
) 
```

#### Parameters

*FieldName*
:   Name of the existing custom property

*FieldValue*
:   Value for the existing custom property

#### Return Value

- 0 if the value for the existing custom property is set
- 1 if the value for the existing custom property is not set
- -1 if the custom property does not exist

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICustomPropertyManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager.md)  
[ICustomPropertyManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager_members.md)  
[ICustomPropertyManager::Get2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Get2.md)
