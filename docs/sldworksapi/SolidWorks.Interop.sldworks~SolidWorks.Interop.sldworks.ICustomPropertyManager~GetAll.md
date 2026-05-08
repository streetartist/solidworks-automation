# GetAll Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~GetAll`

Obsolete. Superseded by ICustomPropertyManager::GetAll2.
Obsolete. Superseded by [ICustomPropertyManager::GetAll2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~GetAll2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetAll( _
   ByRef PropNames As System.Object, _
   ByRef PropTypes As System.Object, _
   ByRef PropValues As System.Object _
) As System.Integer
```

```

Dim instance As ICustomPropertyManager
Dim PropNames As System.Object
Dim PropTypes As System.Object
Dim PropValues As System.Object
Dim value As System.Integer
 
value = instance.GetAll(PropNames, PropTypes, PropValues)
```

```

System.int GetAll( 
   out System.object PropNames,
   out System.object PropTypes,
   out System.object PropValues
)
```

```

System.int GetAll( 
   [Out] System.Object^ PropNames,
   [Out] System.Object^ PropTypes,
   [Out] System.Object^ PropValues
) 
```

#### Parameters

*PropNames*
:   Array of the names of custom properties

*PropTypes*
:   Array of property types as defined in [swCustomInfoType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCustomInfoType_e.html)

*PropValues*
:   Array of values of custom properties

#### Return Value

Number of custom properties

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICustomPropertyManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager.md)  
[ICustomPropertyManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager_members.md)  
[ICustomPropertyManager::Get2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Get2.md)  
[ICustomPropertyManager::IGetAll Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~IGetAll.md)  
[ICustomPropertyManager::Set Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Set.md)
