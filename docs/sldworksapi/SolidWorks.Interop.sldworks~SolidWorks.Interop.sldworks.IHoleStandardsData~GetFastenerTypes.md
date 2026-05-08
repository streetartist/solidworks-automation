# GetFastenerTypes Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleStandardsData~GetFastenerTypes`

Gets the fasteners in the specified Hole Wizard standard.
Gets the fasteners in the specified Hole Wizard standard.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFastenerTypes( _
   ByVal StandardName As System.String, _
   ByRef FastenerIndexes As System.Object, _
   ByRef FastenerNames As System.Object _
) As System.Boolean
```

```

Dim instance As IHoleStandardsData
Dim StandardName As System.String
Dim FastenerIndexes As System.Object
Dim FastenerNames As System.Object
Dim value As System.Boolean
 
value = instance.GetFastenerTypes(StandardName, FastenerIndexes, FastenerNames)
```

```

System.bool GetFastenerTypes( 
   System.string StandardName,
   out System.object FastenerIndexes,
   out System.object FastenerNames
)
```

```

System.bool GetFastenerTypes( 
   System.String^ StandardName,
   [Out] System.Object^ FastenerIndexes,
   [Out] System.Object^ FastenerNames
) 
```

#### Parameters

*StandardName*
:   Standard name (see **Remarks**)

*FastenerIndexes*
:   Array of fastener indexes

*FastenerNames*
:   Array of fastener names

#### Return Value

True if fastener types successfully retrieved, false if not

Remarks

To set StandardName, use [IHoleStandardsData::GetHoleStandards](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleStandardsData~GetHoleStandards.md).

Example

See the [IHoleStandardsData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleStandardsData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IHoleStandardsData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleStandardsData.md)  
[IHoleStandardsData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleStandardsData_members.md)
