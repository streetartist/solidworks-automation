# InsertRecord Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~InsertRecord`

Inserts a record before the specified index in the Region parameters table of this variable-pitch helix.
Inserts a record before the specified index in the Region parameters table of this variable-pitch helix.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertRecord( _
   ByVal Index As System.Integer _
) As System.Boolean
```

```

Dim instance As IHelixFeatureData
Dim Index As System.Integer
Dim value As System.Boolean
 
value = instance.InsertRecord(Index)
```

```

System.bool InsertRecord( 
   System.int Index
)
```

```

System.bool InsertRecord( 
   System.int Index
) 
```

#### Parameters

*Index*
:   Index after which to insert a new record

#### Return Value

True if the record is inserted, false if not

Remarks

When inserting a record, the SOLIDWORKS software calculates the new region's parameters. You cannot add a record to the beginning of the Region parameters table. To add a record to the end of the Region parameters table, use [IHelixFeatureData::AddLastRecord](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~AddLastRecord.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IHelixFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData.md)  
[IHelixFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData_members.md)  
[IHelixFeatureData::VariablePitch Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~VariablePitch.md)  
[IHelixFeatureData::PitchCount Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~PitchCount.md)  
[IHelixFeatureData::DeleteRecord Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~DeleteRecord.md)  
[IHelixFeatureData::SetRegionParameterAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~SetRegionParameterAtIndex.md)  
[IHelixFeatureData::GetRegionParameterAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData~GetRegionParameterAtIndex.md)
