# GetFastenerTable Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleStandardsData~GetFastenerTable`

Gets the Hole Wizard fastener table for the specified Hole Wizard standard, fastener ID, and fastener table type ID.
Gets the Hole Wizard fastener table for the specified Hole Wizard standard, fastener ID, and fastener table type ID.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFastenerTable( _
   ByVal StandardName As System.String, _
   ByVal FastenerID As System.Integer, _
   ByVal TableID As System.Integer, _
   ByRef HoleTable As System.Object _
) As System.Boolean
```

```

Dim instance As IHoleStandardsData
Dim StandardName As System.String
Dim FastenerID As System.Integer
Dim TableID As System.Integer
Dim HoleTable As System.Object
Dim value As System.Boolean
 
value = instance.GetFastenerTable(StandardName, FastenerID, TableID, HoleTable)
```

```

System.bool GetFastenerTable( 
   System.string StandardName,
   System.int FastenerID,
   System.int TableID,
   out System.object HoleTable
)
```

```

System.bool GetFastenerTable( 
   System.String^ StandardName,
   System.int FastenerID,
   System.int TableID,
   [Out] System.Object^ HoleTable
) 
```

#### Parameters

*StandardName*
:   Standard name (see **Remarks**)

*FastenerID*
:   Fastener ID (see **Remarks**)

*TableID*
:   Fastener table type ID (see **Remarks**)

*HoleTable*
:   [IHoleDataTable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleDataTable.md)

#### Return Value

True if fastener data table successfully retrieved, false if not

Remarks

To set:

- StandardName, use [IHoleStandardsData::GetHoleStandards](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleStandardsData~GetHoleStandards.md).
- FastenerID, use [IHoleStandardsData::GetFastenerTypes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleStandardsData~GetFastenerTypes.md).
- TableID, use [IHoleStandardsData::GetFastenerTableTypes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleStandardsData~GetFastenerTableTypes.md).

Example

See the [IHoleStandardsData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleStandardsData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IHoleStandardsData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleStandardsData.md)  
[IHoleStandardsData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleStandardsData_members.md)
