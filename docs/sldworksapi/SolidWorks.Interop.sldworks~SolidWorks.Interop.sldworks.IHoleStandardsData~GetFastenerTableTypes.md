# GetFastenerTableTypes Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleStandardsData~GetFastenerTableTypes`

Gets the array of three fastener table type IDs for the given fastener in the given Hole Wizard standard.
Gets the array of three fastener table type IDs for the given fastener in the given Hole Wizard standard.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFastenerTableTypes( _
   ByVal StandardName As System.String, _
   ByVal FastenerID As System.Integer, _
   ByRef FastenerTableTypeIDs As System.Object _
) As System.Boolean
```

```

Dim instance As IHoleStandardsData
Dim StandardName As System.String
Dim FastenerID As System.Integer
Dim FastenerTableTypeIDs As System.Object
Dim value As System.Boolean
 
value = instance.GetFastenerTableTypes(StandardName, FastenerID, FastenerTableTypeIDs)
```

```

System.bool GetFastenerTableTypes( 
   System.string StandardName,
   System.int FastenerID,
   out System.object FastenerTableTypeIDs
)
```

```

System.bool GetFastenerTableTypes( 
   System.String^ StandardName,
   System.int FastenerID,
   [Out] System.Object^ FastenerTableTypeIDs
) 
```

#### Parameters

*StandardName*
:   Standard name (see **Remarks**)

*FastenerID*
:   Fastener ID (see **Remarks**)

*FastenerTableTypeIDs*
:   Array of three fastener table type IDs (see **Remarks**)

#### Return Value

True if the fastener table type IDs are successfully retrieved, false if not

Remarks

Each fastener in a given standard has three tables associated with it: size, thread data, and screw clearances. This method retrieves internal IDs of all three table types as defined in [swFastenerTableTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFastenerTableTypes_e.html) for FastenerID in StandardName.

To set:

- StandardName, use [IHoleStandardsData::GetHoleStandards](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleStandardsData~GetHoleStandards.md).
- FastenerID, use [IHoleStandardsData::GetFastenerTypes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleStandardsData~GetFastenerTypes.md).

Example

See the [IHoleStandardsData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleStandardsData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IHoleStandardsData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleStandardsData.md)  
[IHoleStandardsData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleStandardsData_members.md)
