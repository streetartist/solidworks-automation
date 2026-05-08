# Add2 Method (ICustomPropertyManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Add2`

Obsolete. Superseded by ICustomPropertyManager::Add3.
Obsolete. Superseded by [ICustomPropertyManager::Add3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Add3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Add2( _
   ByVal FieldName As System.String, _
   ByVal FieldType As System.Integer, _
   ByVal FieldValue As System.String _
) As System.Integer
```

```

Dim instance As ICustomPropertyManager
Dim FieldName As System.String
Dim FieldType As System.Integer
Dim FieldValue As System.String
Dim value As System.Integer
 
value = instance.Add2(FieldName, FieldType, FieldValue)
```

```

System.int Add2( 
   System.string FieldName,
   System.int FieldType,
   System.string FieldValue
)
```

```

System.int Add2( 
   System.String^ FieldName,
   System.int FieldType,
   System.String^ FieldValue
) 
```

#### Parameters

*FieldName*
:   Name of custom property

*FieldType*
:   Type of custom property as defined in [swCustomInfoType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCustomInfoType_e.html)

*FieldValue*
:   Value of custom property

#### Return Value

- 1 if custom property is added
- 0 if custom property is not added
- -1 if the custom property already exists

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICustomPropertyManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager.md)  
[ICustomPropertyManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager_members.md)  
[ICustomerPropertyManager::Delete Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Delete.md)
