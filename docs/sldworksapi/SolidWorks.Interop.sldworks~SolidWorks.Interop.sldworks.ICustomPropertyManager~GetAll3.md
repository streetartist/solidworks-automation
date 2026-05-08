# GetAll3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~GetAll3`

Gets all of the custom properties for this configuration.
Gets all of the custom properties for this configuration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetAll3( _
   ByRef PropNames As System.Object, _
   ByRef PropTypes As System.Object, _
   ByRef PropValues As System.Object, _
   ByRef Resolved As System.Object, _
   ByRef PropLink As System.Object _
) As System.Integer
```

```

Dim instance As ICustomPropertyManager
Dim PropNames As System.Object
Dim PropTypes As System.Object
Dim PropValues As System.Object
Dim Resolved As System.Object
Dim PropLink As System.Object
Dim value As System.Integer
 
value = instance.GetAll3(PropNames, PropTypes, PropValues, Resolved, PropLink)
```

```

System.int GetAll3( 
   out System.object PropNames,
   out System.object PropTypes,
   out System.object PropValues,
   out System.object Resolved,
   out System.object PropLink
)
```

```

System.int GetAll3( 
   [Out] System.Object^ PropNames,
   [Out] System.Object^ PropTypes,
   [Out] System.Object^ PropValues,
   [Out] System.Object^ Resolved,
   [Out] System.Object^ PropLink
) 
```

#### Parameters

*PropNames*
:   Array of the names of custom properties retrieved

*PropTypes*
:   Array of types of PropNames as defined in [swCustomInfoType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCustomInfoType_e.html)

*PropValues*
:   Array of evaluated values of PropNames

*Resolved*
:   Array of evaluation statuses of PropNames as defined in [swCustomInfoGetResult\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCustomInfoGetResult_e.html)

*PropLink*
:   Array of integers indicating whether PropNames are linked to their parent parts:

    1 = link

    0 = no link

#### Return Value

Number of custom properties returned

Example

See the **Get Custom Properties for Configuration** examples in [ICustomPropertyManager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICustomPropertyManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager.md)  
[ICustomPropertyManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager_members.md)  
[ICustomPropertyManager::Get6 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Get6.md)  
[ICustomPropertyManager::Set2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Set2.md)  
[ICustomPropertyManager::GetNames Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~GetNames.md)  
[ICustomPropertyManager::GetType2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~GetType2.md)
