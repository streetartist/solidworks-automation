# Delete Method (ICustomPropertyManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Delete`

Obsolete. Superseded by ICustomPropertyManager::Delete2.
Obsolete. Superseded by [ICustomPropertyManager::Delete2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Delete2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Delete( _
   ByVal FieldName As System.String _
) As System.Integer
```

```

Dim instance As ICustomPropertyManager
Dim FieldName As System.String
Dim value As System.Integer
 
value = instance.Delete(FieldName)
```

```

System.int Delete( 
   System.string FieldName
)
```

```

System.int Delete( 
   System.String^ FieldName
) 
```

#### Parameters

*FieldName*
:   Name of the custom property to delete

#### Return Value

0 if the custom property is deleted, 1 if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICustomPropertyManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager.md)  
[ICustomPropertyManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager_members.md)  
[ICustomerPropertyManager::Add2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Add2.md)
