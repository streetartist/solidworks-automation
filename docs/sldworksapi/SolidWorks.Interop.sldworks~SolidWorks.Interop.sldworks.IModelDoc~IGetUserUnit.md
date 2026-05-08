# IGetUserUnit Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~IGetUserUnit`

Obsolete. Superseded by IModelDoc2::IGetUserUnit.
Obsolete. Superseded by [IModelDoc2::IGetUserUnit](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetUserUnit.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetUserUnit( _
   ByVal UnitType As System.Integer _
) As UserUnit
```

```

Dim instance As IModelDoc
Dim UnitType As System.Integer
Dim value As UserUnit
 
value = instance.IGetUserUnit(UnitType)
```

```

UserUnit IGetUserUnit( 
   System.int UnitType
)
```

```

UserUnit^ IGetUserUnit( 
   System.int UnitType
) 
```

#### Parameters

*UnitType*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
