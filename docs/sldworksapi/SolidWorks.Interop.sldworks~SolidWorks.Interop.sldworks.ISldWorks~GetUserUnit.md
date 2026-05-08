# GetUserUnit Method (ISldWorks)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetUserUnit`

Gets an empty IUserUnit object of the specified type.
Gets an empty [IUserUnit](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit.md) object of the specified type.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetUserUnit( _
   ByVal UnitType As System.Integer _
) As System.Object
```

```

Dim instance As ISldWorks
Dim UnitType As System.Integer
Dim value As System.Object
 
value = instance.GetUserUnit(UnitType)
```

```

System.object GetUserUnit( 
   System.int UnitType
)
```

```

System.Object^ GetUserUnit( 
   System.int UnitType
) 
```

#### Parameters

*UnitType*
:   Unit type as defined in [swUserUnitsType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swUserUnitsType_e.html)

#### Return Value

IUserUnit

Remarks

The instance of IUserUnit returned by this method is read-write, not persistent, and not tied to any document. Use this instance as a template to store units properties at runtime.

Call [IModelDoc2::GetUserUnit](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetUserUnit.md) to get the user units of a document.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::IGetUserUnit Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetUserUnit.md)  
[IModelDoc2::IGetUserUnit Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetUserUnit.md)
