# IGetAll Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~IGetAll`

Gets all of the custom properties for this configuration.
Gets all of the custom properties for this configuration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub IGetAll( _
   ByVal Count As System.Integer, _
   ByRef PropNames As System.String, _
   ByRef PropTypes As System.Integer, _
   ByRef PropValues As System.String _
) 
```

```

Dim instance As ICustomPropertyManager
Dim Count As System.Integer
Dim PropNames As System.String
Dim PropTypes As System.Integer
Dim PropValues As System.String
 
instance.IGetAll(Count, PropNames, PropTypes, PropValues)
```

```

void IGetAll( 
   System.int Count,
   out System.string PropNames,
   out System.int PropTypes,
   out System.string PropValues
)
```

```

void IGetAll( 
   System.int Count,
   [Out] System.String^ PropNames,
   [Out] System.int PropTypes,
   [Out] System.String^ PropValues
) 
```

#### Parameters

*Count*
:   Number of custom properties

*PropNames*
:   Array of the names of custom properties

*PropTypes*
:   Array of property types as defined in [swCustomInfoType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCustomInfoType_e.html)

*PropValues*
:   Array of values of custom properties

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICustomPropertyManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager.md)  
[ICustomPropertyManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager_members.md)  
[ICustomPropertyManager::Get2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Get2.md)  
[ICustomPropertyManager::GetAll Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~GetAll.md)
