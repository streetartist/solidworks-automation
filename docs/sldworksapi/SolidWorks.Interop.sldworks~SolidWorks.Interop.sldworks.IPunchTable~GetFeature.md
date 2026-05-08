# GetFeature Method (IPunchTable)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable~GetFeature`

Gets the IFeature object for this punch table.
Gets the [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) object for this punch table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFeature() As Feature
```

```

Dim instance As IPunchTable
Dim value As Feature
 
value = instance.GetFeature()
```

```

Feature GetFeature()
```

```

Feature^ GetFeature(); 
```

#### Return Value

Pointer to the [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) object

Example

[Insert Punch Table (VBA)](Insert_Punch_Table_Example_VB.htm)  
[Insert Punch Table (VB.NET)](Insert_Punch_Table_Example_VBNET.htm)  
[Insert Punch Table (C#)](Insert_Punch_Table_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPunchTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable.md)  
[IPunchTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable_members.md)
