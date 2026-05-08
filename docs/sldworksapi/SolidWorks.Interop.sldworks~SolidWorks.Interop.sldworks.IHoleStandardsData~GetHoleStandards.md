# GetHoleStandards Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleStandardsData~GetHoleStandards`

Gets Hole Wizard standards.
Gets Hole Wizard standards.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetHoleStandards( _
   ByRef Indexes As System.Object, _
   ByRef Names As System.Object _
) As System.Boolean
```

```

Dim instance As IHoleStandardsData
Dim Indexes As System.Object
Dim Names As System.Object
Dim value As System.Boolean
 
value = instance.GetHoleStandards(Indexes, Names)
```

```

System.bool GetHoleStandards( 
   out System.object Indexes,
   out System.object Names
)
```

```

System.bool GetHoleStandards( 
   [Out] System.Object^ Indexes,
   [Out] System.Object^ Names
) 
```

#### Parameters

*Indexes*
:   Array of Hole Wizard standards as defined in [swWzdHoleStandards\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swWzdHoleStandards_e.html)

*Names*
:   Array of names of Hole Wizard standards

#### Return Value

True if Hole Wizard standards retrieved successfully, false if not

Example

See the [IHoleStandardsData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleStandardsData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IHoleStandardsData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleStandardsData.md)  
[IHoleStandardsData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleStandardsData_members.md)  
[IHoleStandardsData::GetFastenerTable Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleStandardsData~GetFastenerTable.md)  
[IHoleStandardsData::GetFastenerTableTypes Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleStandardsData~GetFastenerTableTypes.md)  
[IHoleStandardsData::GetFastenerTypes Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleStandardsData~GetFastenerTypes.md)
